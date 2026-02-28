from loader import load_document
from chunker import chunk_text
from retriever import Retriever

# Load + chunk
doc = load_document("data/sample.txt")
chunks = chunk_text(doc, chunk_size=20)

# Build retriever
retriever = Retriever(chunks)

# Ask a question
query = "What is machine learning?"
results = retriever.retrieve(query, k=2)

print("Question:", query)
print("\nTop relevant chunks:\n")

for r in results:
    print("-", r)