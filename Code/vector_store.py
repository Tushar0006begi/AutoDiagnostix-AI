"""
AutoDiagnostix-AI Vector Store Implementation
Provides self-contained dense vector indexing, cosine similarity calculation,
and metadata-preserved chunk storage.
"""

import math
import re
import json
from typing import List, Dict, Any, Tuple


class DocumentChunk:
    def __init__(
        self,
        chunk_id: str,
        text: str,
        metadata: Dict[str, Any]
    ):
        self.chunk_id = chunk_id
        self.text = text
        self.metadata = metadata
        self.tokens = self._tokenize(text)
        self.embedding = None

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        # Retain alphanumeric tokens, hyphens, and codes like P0300, 2.0L, 50kW
        return re.findall(r'[a-zA-Z0-9_\-]+', text.lower())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chunk_id": self.chunk_id,
            "text": self.text,
            "metadata": self.metadata
        }


class HybridVectorStore:
    def __init__(self):
        self.chunks: List[DocumentChunk] = []
        self.vocabulary: Dict[str, int] = {}
        self.idf: Dict[str, float] = {}
        self.doc_vectors: List[Dict[int, float]] = []

    def add_documents(self, raw_documents: List[Dict[str, Any]]) -> int:
        """
        Parses JSON manual documents, chunks them by section/diagnostic steps,
        and adds them to the vector index.
        """
        new_count = 0
        for doc in raw_documents:
            doc_id = doc.get("document_id", "DOC-UNK")
            title = doc.get("document_title", "Unknown Manual")
            chapter = doc.get("chapter", "")
            section = doc.get("section", "")
            page = doc.get("page_number", 0)
            diagram_id = doc.get("diagram_id", "N/A")
            vehicle_models = doc.get("vehicle_models", [])
            subsystem = doc.get("subsystem", "General")
            content = doc.get("content", "")

            # If content is large, split into paragraphs or steps
            paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
            if not paragraphs:
                paragraphs = [content.strip()]

            for idx, para in enumerate(paragraphs):
                chunk_id = f"{doc_id}_P{page}_{idx+1}"
                meta = {
                    "document_id": doc_id,
                    "document_title": title,
                    "chapter": chapter,
                    "section": section,
                    "page_number": page,
                    "diagram_id": diagram_id,
                    "vehicle_models": vehicle_models,
                    "subsystem": subsystem
                }
                chunk = DocumentChunk(chunk_id=chunk_id, text=para, metadata=meta)
                self.chunks.append(chunk)
                new_count += 1

        self._build_index()
        return new_count

    def _build_index(self):
        """Builds vocabulary and IDF statistics for TF-IDF dense-sparse vectorization."""
        N = len(self.chunks)
        if N == 0:
            return

        doc_freq = {}
        for chunk in self.chunks:
            unique_tokens = set(chunk.tokens)
            for token in unique_tokens:
                doc_freq[token] = doc_freq.get(token, 0) + 1

        # Calculate Smooth IDF
        self.vocabulary = {token: idx for idx, token in enumerate(doc_freq.keys())}
        self.idf = {token: math.log((N + 1) / (df + 1)) + 1.0 for token, df in doc_freq.items()}

        # Build Normalized TF-IDF Vectors
        self.doc_vectors = []
        for chunk in self.chunks:
            vec = {}
            token_counts = {}
            for t in chunk.tokens:
                token_counts[t] = token_counts.get(t, 0) + 1

            doc_len = len(chunk.tokens) if chunk.tokens else 1
            norm_sq = 0.0
            for t, count in token_counts.items():
                if t in self.vocabulary:
                    tf = count / doc_len
                    weight = tf * self.idf[t]
                    col = self.vocabulary[t]
                    vec[col] = weight
                    norm_sq += weight * weight

            norm = math.sqrt(norm_sq) if norm_sq > 0 else 1.0
            # Unit normalize vector for efficient cosine similarity
            normalized_vec = {col: w / norm for col, w in vec.items()}
            self.doc_vectors.append(normalized_vec)

    def query_dense_similarity(self, query: str, top_k: int = 5) -> List[Tuple[DocumentChunk, float]]:
        """Computes Cosine Similarity between query vector and indexed document vectors."""
        query_tokens = DocumentChunk._tokenize(query)
        if not query_tokens:
            return []

        q_counts = {}
        for t in query_tokens:
            q_counts[t] = q_counts.get(t, 0) + 1

        q_len = len(query_tokens)
        q_vec = {}
        norm_sq = 0.0
        for t, count in q_counts.items():
            if t in self.vocabulary and t in self.idf:
                tf = count / q_len
                weight = tf * self.idf[t]
                col = self.vocabulary[t]
                q_vec[col] = weight
                norm_sq += weight * weight

        if norm_sq == 0.0:
            return []

        q_norm = math.sqrt(norm_sq)
        normalized_q_vec = {col: w / q_norm for col, w in q_vec.items()}

        scores = []
        for idx, doc_vec in enumerate(self.doc_vectors):
            dot_product = 0.0
            for col, w in normalized_q_vec.items():
                if col in doc_vec:
                    dot_product += w * doc_vec[col]
            scores.append((self.chunks[idx], dot_product))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
