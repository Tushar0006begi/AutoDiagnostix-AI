"""
AutoDiagnostix-AI Hybrid Retriever
Combines BM25 Lexical Matching with Dense Vector Cosine Similarity
and provides reciprocal rank / linear score fusion.
"""

import math
import re
from typing import List, Dict, Any, Tuple
from vector_store import HybridVectorStore, DocumentChunk
import config


class BM25Retriever:
    """Okapi BM25 Lexical Matching Engine."""
    def __init__(self, chunks: List[DocumentChunk], k1: float = 1.5, b: float = 0.75):
        self.chunks = chunks
        self.k1 = k1
        self.b = b
        self.doc_count = len(chunks)
        self.avg_doc_len = sum(len(c.tokens) for c in chunks) / max(self.doc_count, 1)
        self.doc_freqs: Dict[str, int] = {}
        self.doc_lens: List[int] = [len(c.tokens) for c in chunks]

        # Inverted index: token -> list of (doc_index, term_frequency)
        self.inverted_index: Dict[str, List[Tuple[int, int]]] = {}
        self._build_index()

    def _build_index(self):
        for idx, chunk in enumerate(self.chunks):
            term_counts: Dict[str, int] = {}
            for token in chunk.tokens:
                term_counts[token] = term_counts.get(token, 0) + 1

            for token, count in term_counts.items():
                self.doc_freqs[token] = self.doc_freqs.get(token, 0) + 1
                if token not in self.inverted_index:
                    self.inverted_index[token] = []
                self.inverted_index[token].append((idx, count))

    def get_scores(self, query: str) -> List[Tuple[DocumentChunk, float]]:
        query_tokens = DocumentChunk._tokenize(query)
        scores = [0.0] * self.doc_count

        for token in query_tokens:
            if token not in self.inverted_index:
                continue

            df = self.doc_freqs.get(token, 0)
            # Standard Lucene/BM25 IDF formula
            idf = math.log(1.0 + (self.doc_count - df + 0.5) / (df + 0.5))

            for doc_idx, tf in self.inverted_index[token]:
                doc_len = self.doc_lens[doc_idx]
                numerator = tf * (self.k1 + 1.0)
                denominator = tf + self.k1 * (1.0 - self.b + self.b * (doc_len / self.avg_doc_len))
                scores[doc_idx] += idf * (numerator / denominator)

        ranked = [(self.chunks[i], scores[i]) for i in range(self.doc_count) if scores[i] > 0]
        ranked.sort(key=lambda x: x[1], reverse=True)
        return ranked


class HybridRetriever:
    """Hybrid Retriever combining BM25 Lexical & Dense Vector Cosine Similarity."""
    def __init__(self, vector_store: HybridVectorStore, alpha: float = config.BM25_ALPHA, beta: float = config.DENSE_BETA):
        self.vector_store = vector_store
        self.bm25 = BM25Retriever(vector_store.chunks)
        self.alpha = alpha  # Weight for BM25
        self.beta = beta    # Weight for Dense

    def retrieve(self, query: str, top_k: int = config.DEFAULT_TOP_K) -> List[Dict[str, Any]]:
        dense_results = self.vector_store.query_dense_similarity(query, top_k=top_k * 2)
        bm25_results = self.bm25.get_scores(query)

        # Normalize dense scores
        dense_scores = {chunk.chunk_id: score for chunk, score in dense_results}
        max_dense = max(dense_scores.values()) if dense_scores and max(dense_scores.values()) > 0 else 1.0
        norm_dense = {cid: s / max_dense for cid, s in dense_scores.items()}

        # Normalize BM25 scores
        bm25_scores = {chunk.chunk_id: score for chunk, score in bm25_results}
        max_bm25 = max(bm25_scores.values()) if bm25_scores and max(bm25_scores.values()) > 0 else 1.0
        norm_bm25 = {cid: s / max_bm25 for cid, s in bm25_scores.items()}

        # Fuse scores
        fused_chunks: Dict[str, Tuple[DocumentChunk, float]] = {}
        all_chunk_ids = set(norm_dense.keys()).union(set(norm_bm25.keys()))

        chunk_lookup = {c.chunk_id: c for c in self.vector_store.chunks}

        for cid in all_chunk_ids:
            s_dense = norm_dense.get(cid, 0.0)
            s_bm25 = norm_bm25.get(cid, 0.0)
            hybrid_score = (self.beta * s_dense) + (self.alpha * s_bm25)
            fused_chunks[cid] = (chunk_lookup[cid], hybrid_score)

        ranked = sorted(fused_chunks.values(), key=lambda x: x[1], reverse=True)

        results = []
        for chunk, score in ranked[:top_k]:
            results.append({
                "chunk_id": chunk.chunk_id,
                "text": chunk.text,
                "metadata": chunk.metadata,
                "retrieval_score": round(score, 4),
                "citation": f"[Source: {chunk.metadata.get('document_title')}, Page: {chunk.metadata.get('page_number')}, Section: {chunk.metadata.get('section')}]"
            })

        return results
