import os

DOCUMENT_FOLDER = "data"

def load_documents():
    documents = []

    for filename in os.listdir(DOCUMENT_FOLDER):
        if filename.endswith(".txt"):
            path = os.path.join(DOCUMENT_FOLDER, filename)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            documents.append({
                "source": filename,
                "content": text
            })

    return documents