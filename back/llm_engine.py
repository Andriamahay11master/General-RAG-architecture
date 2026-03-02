from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_llm_answer(query, retrieved_chunks):
    if not retrieved_chunks:
        return "No relevant information found."

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an AI assistant.

Answer the question using ONLY the context below.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()