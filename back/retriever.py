from back.chunker import chunk_text
from back.loader import load_documents
from back.vectorstore import VectorStore

class Retriever:
    def __init__(self):

        documents = load_documents()

        chunks = []

        for doc in documents:
            split_chunks = chunk_text(doc["content"])

            for chunk in split_chunks:
                chunks.append({
                    "text": chunk,
                    "source": doc["source"]
                })

        self.vector_store = VectorStore()
        self.vector_store.build_index(chunks)

    def retrieve(self, query, k=3):
        return self.vector_store.search(query, k)