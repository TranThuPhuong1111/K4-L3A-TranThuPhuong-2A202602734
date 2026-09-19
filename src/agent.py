from typing import Callable

from .store import EmbeddingStore


class KnowledgeBaseAgent:
    """
    An agent that answers questions using a vector knowledge base.

    Retrieval-augmented generation (RAG) pattern:
        1. Retrieve top-k relevant chunks from the store.
        2. Build a prompt with the chunks as context.
        3. Call the LLM to generate an answer.
    """

    def __init__(self, store: EmbeddingStore, llm_fn: Callable[[str], str]) -> None:
        self.store = store
        self.llm_fn = llm_fn

    def answer(self, question: str, top_k: int = 3) -> str:
        records = self.store.search(question, top_k=top_k)
        if not records:
            return "No relevant information was found in the knowledge base."

        context_parts = []
        for index, record in enumerate(records, start=1):
            metadata = record.get("metadata", {})
            source = (
                metadata.get("source_url")
                or metadata.get("source")
                or metadata.get("doc_id")
                or record.get("id", "unknown")
            )
            context_parts.append(f"[{index}] Source: {source}\n{record.get('content', '')}")

        prompt = (
            "Answer the question using only the context below. "
            "If the context does not contain the answer, say that it was not found. "
            "Cite the supporting chunk numbers in your answer, such as [1] or [2].\n\n"
            f"Context:\n{chr(10).join(context_parts)}\n\n"
            f"Question: {question}\n"
            "Answer:"
        )
        return self.llm_fn(prompt)
