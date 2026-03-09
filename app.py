from flask import Flask, render_template, request, jsonify
from back.retriever import Retriever
from back.llm_engine import generate_llm_answer

app = Flask(__name__)

retriever = Retriever()

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000)) 
    app.run(host="0.0.0.0", port=port)