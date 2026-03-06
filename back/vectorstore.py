import faiss
import numpy as np
from back.embeddings import embed_texts

class VectorStore:

    def __init__(self):
        self.index = None
        self.chunks = []

    def build_index(self, chunks):
        """
        Build FAISS index from text chunks
        """

        texts = [c["text"] for c in chunks]

        embeddings = embed_texts(texts)
        embeddings = np.array(embeddings).astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        self.chunks = chunks

    def search(self, query, k=3, threshold=1.2):
        """
        Retrieve top-k chunks
        """

        query_embedding = embed_texts([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for dist, idx in zip(distances[0], indices[0]):

            # Filter irrelevant chunks
            if dist < threshold:
                results.append(self.chunks[idx])

        return results