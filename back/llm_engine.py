from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_llm_answer(query, retrieved_chunks):
    if not retrieved_chunks:
        return "No relevant information found."

    # Extract text from retrieved chunks
    context = "\n\n".join(
        f"Source: {chunk['source']}\n{chunk['text']}"
        for chunk in retrieved_chunks
    )

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
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content.strip()

    # Extract unique sources
    sources = list(set(chunk["source"] for chunk in retrieved_chunks))

    source_text = "\n".join(f"- {s}" for s in sources)

    final_answer = f"{answer}\n\nSources:\n{source_text}"

    return final_answer