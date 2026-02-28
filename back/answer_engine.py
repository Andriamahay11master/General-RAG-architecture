def generate_answer(query, retrieved_chunks):
    """
    Simple answer generator:
    - Combine relevant chunks
    - Return structured answer
    """

    if not retrieved_chunks:
        return "No relevant information found in the document."

    context = "\n\n".join(retrieved_chunks)

    answer = f"""
Question:
{query}

Answer (based only on the document):

{context}
"""

    return answer.strip()