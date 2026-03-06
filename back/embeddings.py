from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    """
    Convert list of texts into embeddings
    """
    embeddings = model.encode(texts)
    return embeddings