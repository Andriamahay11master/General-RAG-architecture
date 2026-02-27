from loader import load_document
from chunker import chunk_text

doc = load_document("data/sample.txt")
chunks = chunk_text(doc, chunk_size=20)

print("Number of chunks:", len(chunks))
print("\nFirst chunk:\n", chunks[0])