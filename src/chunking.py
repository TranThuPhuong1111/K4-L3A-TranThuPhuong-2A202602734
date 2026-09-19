from __future__ import annotations

import math
import re


class FixedSizeChunker:
    """
    Split text into fixed-size chunks with optional overlap.

    Rules:
        - Each chunk is at most chunk_size characters long.
        - Consecutive chunks share overlap characters.
        - The last chunk contains whatever remains.
        - If text is shorter than chunk_size, return [text].
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50) -> None:
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> list[str]:
        if not text:
            return []
        if len(text) <= self.chunk_size:
            return [text]

        step = self.chunk_size - self.overlap
        chunks: list[str] = []
        for start in range(0, len(text), step):
            chunk = text[start : start + self.chunk_size]
            chunks.append(chunk)
            if start + self.chunk_size >= len(text):
                break
        return chunks


class SentenceChunker:
    """
    Split text into chunks of at most max_sentences_per_chunk sentences.

    Sentence detection: split on ". ", "! ", "? " or ".\n".
    Strip extra whitespace from each chunk.
    """

    def __init__(self, max_sentences_per_chunk: int = 3) -> None:
        self.max_sentences_per_chunk = max(1, max_sentences_per_chunk)

    def chunk(self, text: str) -> list[str]:
        if not text or not text.strip():
            return []

        sentences = [part.strip() for part in re.split(r'(?<=[.!?])\s+', text.strip()) if part and part.strip()]
        if not sentences:
            return []

        chunks: list[str] = []
        for start in range(0, len(sentences), self.max_sentences_per_chunk):
            group = sentences[start : start + self.max_sentences_per_chunk]
            chunk = " ".join(group).strip()
            if chunk:
                chunks.append(chunk)
        return chunks


class RecursiveChunker:
    """
    Recursively split text using separators in priority order.

    Default separator priority:
        ["\n\n", "\n", ". ", " ", ""]
    """

    DEFAULT_SEPARATORS = ["\n\n", "\n", ". ", " ", ""]

    def __init__(self, separators: list[str] | None = None, chunk_size: int = 500) -> None:
        self.separators = self.DEFAULT_SEPARATORS if separators is None else list(separators)
        self.chunk_size = chunk_size

    def __init__(self, separators: list[str] | None = None, chunk_size: int = 500) -> None:
        self.separators = self.DEFAULT_SEPARATORS if separators is None else list(separators)
        self.chunk_size = max(1, chunk_size)

    def chunk(self, text: str) -> list[str]:
        if not text or not text.strip():
            return []

        cleaned = text.strip()
        if len(cleaned) <= self.chunk_size:
            return [cleaned]

        chunks = self._split(cleaned, list(self.separators))
        if not chunks:
            return [cleaned[: self.chunk_size]]

        merged: list[str] = []
        current = ""
        for part in chunks:
            if not part:
                continue
            if not current:
                current = part
                continue
            if len(current) + 1 + len(part) <= self.chunk_size:
                current = f"{current} {part}".strip()
            else:
                merged.append(current)
                current = part
        if current:
            merged.append(current)

        return merged if merged else [cleaned[: self.chunk_size]]

    def _split(self, current_text: str, remaining_separators: list[str]) -> list[str]:
        current_text = current_text.strip()
        if not current_text:
            return []

        if len(current_text) <= self.chunk_size:
            return [current_text]

        if not remaining_separators:
            if self.chunk_size <= 0:
                return [current_text]
            return [current_text[i : i + self.chunk_size] for i in range(0, len(current_text), self.chunk_size) if current_text[i : i + self.chunk_size]]

        separator = remaining_separators[0]
        if separator == "":
            return [current_text[i : i + self.chunk_size] for i in range(0, len(current_text), self.chunk_size) if current_text[i : i + self.chunk_size]]

        if separator not in current_text:
            return self._split(current_text, remaining_separators[1:])

        parts = [part.strip() for part in current_text.split(separator) if part and part.strip()]
        if not parts:
            return [current_text]

        split_parts: list[str] = []
        for part in parts:
            if len(part) <= self.chunk_size:
                split_parts.append(part)
            else:
                split_parts.extend(self._split(part, remaining_separators[1:]))

        merged: list[str] = []
        current = ""
        for part in split_parts:
            if not current:
                current = part
                continue
            if len(current) + len(separator) + len(part) <= self.chunk_size:
                current = f"{current}{separator}{part}".strip()
            else:
                merged.append(current)
                current = part
        if current:
            merged.append(current)

        return merged if merged else split_parts


class HeadingChunker:
    """Split Markdown into heading-led sections, recursively splitting long sections."""

    def __init__(self, chunk_size: int = 800) -> None:
        self.chunk_size = max(1, chunk_size)
        self._recursive = RecursiveChunker(chunk_size=self.chunk_size)

    def chunk(self, text: str) -> list[str]:
        if not text or not text.strip():
            return []

        lines = text.strip().splitlines()
        sections: list[tuple[str, list[str]]] = []
        current_heading = ""
        current_lines: list[str] = []

        for line in lines:
            if re.match(r"^#{1,6}\s+", line):
                if current_lines:
                    sections.append((current_heading, current_lines))
                current_heading = line.strip()
                current_lines = []
            else:
                current_lines.append(line)
        if current_lines:
            sections.append((current_heading, current_lines))

        chunks: list[str] = []
        for heading, section_lines in sections:
            body = "\n".join(section_lines).strip()
            section = "\n".join(part for part in (heading, body) if part).strip()
            if not section:
                continue
            if len(section) <= self.chunk_size:
                chunks.append(section)
                continue

            child_chunks = self._recursive.chunk(body or heading)
            for child in child_chunks:
                if heading and child != heading:
                    chunks.append(f"{heading}\n\n{child}".strip())
                else:
                    chunks.append(child)
        return chunks


def _dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def compute_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """
    Compute cosine similarity between two vectors.

    cosine_similarity = dot(a, b) / (||a|| * ||b||)

    Returns 0.0 if either vector has zero magnitude.
    """
    if not vec_a or not vec_b or len(vec_a) != len(vec_b):
        return 0.0

    norm_a = math.sqrt(sum(v * v for v in vec_a))
    norm_b = math.sqrt(sum(v * v for v in vec_b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    return _dot(vec_a, vec_b) / (norm_a * norm_b)


class ChunkingStrategyComparator:
    """Run all built-in chunking strategies and compare their results."""

    def compare(self, text: str, chunk_size: int = 200) -> dict:
        strategies = {
            "fixed_size": FixedSizeChunker(chunk_size=chunk_size).chunk(text),
            "by_sentences": SentenceChunker(max_sentences_per_chunk=3).chunk(text),
            "recursive": RecursiveChunker(chunk_size=chunk_size).chunk(text),
        }

        result: dict[str, dict[str, object]] = {}
        for name, chunks in strategies.items():
            if not chunks:
                result[name] = {"count": 0, "avg_length": 0.0, "chunks": []}
                continue
            avg_length = sum(len(chunk) for chunk in chunks) / len(chunks)
            result[name] = {"count": len(chunks), "avg_length": avg_length, "chunks": chunks}
        return result
