from sentence_transformers import SentenceTransformer

# Load lightweight but powerful embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts)