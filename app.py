from flask import Flask, render_template, request, jsonify
from back.loader import load_document
from back.chunker import chunk_text
from back.retriever import Retriever
from back.llm_engine import generate_llm_answer

app = Flask(__name__)

# Load and prepare document at startup
doc = load_document("data/sample.txt")
chunks = chunk_text(doc, chunk_size=150)
retriever = Retriever(chunks)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    retrieved = retriever.retrieve(question, k=3)
    answer = generate_llm_answer(question, retrieved)

    return jsonify({
        "answer": answer
    })

def index():
    answer = None
    question = None

    if request.method == "POST":
        question = request.form["question"]
        retrieved = retriever.retrieve(question, k=3)
        answer = generate_llm_answer(question, retrieved)

    return render_template(
        "index.html",
        answer=answer,
        question=question
    )

if __name__ == "__main__":
    app.run(debug=True)