from loader import load_document
from chunker import chunk_text
from retriever import Retriever
from llm_engine import generate_llm_answer

doc = load_document("data/sample.txt")
chunks = chunk_text(doc, chunk_size=20)

retriever = Retriever(chunks)

query = "Explain machine learning."
retrieved = retriever.retrieve(query, k=3)

answer = generate_llm_answer(query, retrieved)

print(answer)