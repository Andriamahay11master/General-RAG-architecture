import numpy as np
from embeddings import embed_texts


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def generate_answer(query, retrieved_chunks, top_n=3):
    """
    Improved answer generator:
    - Split chunks into sentences
    - Rank sentences by similarity to query
    - Return top sentences
    """

    if not retrieved_chunks:
        return "No relevant information found."

    # Split chunks into sentences
    sentences = []
    for chunk in retrieved_chunks:
        for sentence in chunk.split("."):
            sentence = sentence.strip()
            if len(sentence) > 20:  # avoid very short fragments
                sentences.append(sentence)

    if not sentences:
        return "No meaningful sentences found."

    # Embed query + sentences
    query_embedding = embed_texts([query])[0]
    sentence_embeddings = embed_texts(sentences)

    # Compute similarities
    scored_sentences = []
    for sentence, emb in zip(sentences, sentence_embeddings):
        score = cosine_similarity(query_embedding, emb)
        scored_sentences.append((sentence, score))

    # Sort by similarity
    scored_sentences.sort(key=lambda x: x[1], reverse=True)

    # Select top sentences
    best_sentences = [s[0] for s in scored_sentences[:top_n]]

    # Build final answer
    answer = " ".join(best_sentences)

    return answer