from embeddings import embed_texts
from vectorstore import VectorStore

class Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.embeddings = embed_texts(chunks)
        dimension = self.embeddings.shape[1]
        self.store = VectorStore(dimension)
        self.store.add_vectors(self.embeddings)

    def retrieve(self, query, k=3):
        query_vector = embed_texts([query])[0]
        indices = self.store.search(query_vector, k)
        return [self.chunks[i] for i in indices]