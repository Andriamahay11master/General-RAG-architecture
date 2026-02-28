import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_vectors(self, vectors):
        vectors = np.array(vectors).astype("float32")
        self.index.add(vectors)

    def search(self, query_vector, k=3):
        query_vector = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_vector, k)
        return indices[0]