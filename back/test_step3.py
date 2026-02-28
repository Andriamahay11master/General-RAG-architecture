from loader import load_document
from chunker import chunk_text
from retriever import Retriever
from answer_engine import generate_answer

doc = load_document("data/sample.txt")
chunks = chunk_text(doc, chunk_size=20)

retriever = Retriever(chunks)

query = "What is sweeties?"
retrieved = retriever.retrieve(query, k=3)

answer = generate_answer(query, retrieved)

print("Question:", query)
print("\nAnswer:\n")
print(answer)