import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_llm_answer(query, retrieved_chunks):
    if not retrieved_chunks:
        return "No relevant information found."

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an AI assistant.

Answer the question using ONLY the information provided in the context below.
Do not add external knowledge.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()