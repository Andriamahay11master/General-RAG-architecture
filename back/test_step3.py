from loader import load_document
from chunker import chunk_text
from retriever import Retriever
from answer_engine import generate_answer

# Load + chunk document
doc = load_document("data/sample.txt")
chunks = chunk_text(doc, chunk_size=20)

# Build retriever
retriever = Retriever(chunks)

# Ask question
query = "What is deep learning?"

retrieved = retriever.retrieve(query, k=2)

answer = generate_answer(query, retrieved)

print(answer)