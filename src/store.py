from __future__ import annotations

import re
from typing import Any, Callable

from .chunking import _dot
from .embeddings import _mock_embed
from .models import Document


class EmbeddingStore:
    """
    A vector store for text chunks.

    Stores embedded documents in memory.

    The embedding_fn parameter allows injection of mock embeddings for tests.
    """

    def __init__(
        self,
        collection_name: str = "documents",
        embedding_fn: Callable[[str], list[float]] | None = None,
    ) -> None:
        self._embedding_fn = embedding_fn or _mock_embed
        self._collection_name = collection_name
        self._use_chroma = False
        self._store: list[dict[str, Any]] = []
        self._next_index = 0

    def _make_record(self, doc: Document) -> dict[str, Any]:
        metadata = dict(doc.metadata or {})
        metadata.setdefault("doc_id", doc.id.split("#", 1)[0])
        return {
            "id": doc.id,
            "content": doc.content,
            "metadata": metadata,
            "embedding": self._embedding_fn(doc.content),
        }

    def _search_records(self, query: str, records: list[dict[str, Any]], top_k: int) -> list[dict[str, Any]]:
        if top_k <= 0 or not records:
            return []

        query_embedding = self._embedding_fn(query)
        ranked = sorted(
            (
                (
                    self._combined_score(query, query_embedding, record),
                    record,
                )
                for record in records
            ),
            key=lambda item: item[0],
            reverse=True,
        )
        return [
            {
                "id": record["id"],
                "content": record["content"],
                "metadata": dict(record["metadata"]),
                "score": score,
            }
            for score, record in ranked[:top_k]
        ]

    @staticmethod
    def _similarity(query_embedding: list[float], document_embedding: list[float]) -> float:
        if not query_embedding or not document_embedding:
            return 0.0
        query_norm = sum(value * value for value in query_embedding) ** 0.5
        document_norm = sum(value * value for value in document_embedding) ** 0.5
        if query_norm == 0.0 or document_norm == 0.0:
            return 0.0
        return _dot(query_embedding, document_embedding) / (query_norm * document_norm)

    @staticmethod
    def _lexical_score(query: str, content: str) -> float:
        query_terms = set(re.findall(r"\w+", query.casefold()))
        content_terms = set(re.findall(r"\w+", content.casefold()))
        if not query_terms:
            return 0.0
        return len(query_terms & content_terms) / len(query_terms)

    @classmethod
    def _combined_score(
        cls,
        query: str,
        query_embedding: list[float],
        record: dict[str, Any],
    ) -> float:
        semantic_score = cls._similarity(query_embedding, record["embedding"])
        lexical_score = cls._lexical_score(query, record["content"])
        return 0.15 * semantic_score + 0.85 * lexical_score

    def add_documents(self, docs: list[Document]) -> None:
        """
        Embed each document's content and store it.

        Store each document as an in-memory record.
        """
        self._store.extend(self._make_record(doc) for doc in docs)

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        """
        Find the top_k most similar documents to query.

        Compute similarity against all stored records.
        """
        return self._search_records(query, self._store, top_k)

    def get_collection_size(self) -> int:
        """Return the total number of stored chunks."""
        return len(self._store)

    def search_with_filter(self, query: str, top_k: int = 3, metadata_filter: dict = None) -> list[dict]:
        """
        Search with optional metadata pre-filtering.

        First filter stored chunks by metadata_filter, then run similarity search.
        """
        if not metadata_filter:
            return self._search_records(query, self._store, top_k)

        candidates = [
            record
            for record in self._store
            if all(record["metadata"].get(key) == value for key, value in metadata_filter.items())
        ]
        return self._search_records(query, candidates, top_k)

    def delete_document(self, doc_id: str) -> bool:
        """
        Remove all chunks belonging to a document.

        Returns True if any chunks were removed, False otherwise.
        """
        original_size = len(self._store)
        self._store = [
            record for record in self._store
            if record["metadata"].get("doc_id") != doc_id
        ]
        return len(self._store) < original_size
