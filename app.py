
import os

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/ask", methods=["POST"])
def ask_assistant():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "")

    if not isinstance(question, str) or not question.strip():
        return jsonify({"error": "Please enter your question."}), 400

    if len(question) > 1000:
        return jsonify({"error": "Question must be under 1000 characters."}), 400

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return jsonify({
            "error": "API key missing. Check your .env file."
        }), 503

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=(
                "You are VillageCare AI, a health education assistant "
                "for village communities. Give simple, general health "
                "information. Do not diagnose illnesses or prescribe "
                "medicines. Encourage users to consult a qualified doctor. "
                "For emergencies, advise immediate medical care. "
                "In India, call 112 for emergencies. "
                "Reply in the language used by the user when possible.\n\n"
                f"Question: {question.strip()}"
            ),
        )

        answer = response.text

        if not answer:
            answer = "Sorry, I could not generate an answer. Please try again."

        return jsonify({"answer": answer})

    except Exception:
        app.logger.exception("Gemini API request failed")
        return jsonify({
            "error": (
                "AI service unavailable. Check your API key, internet "
                "connection, and Gemini API quota."
            )
        }), 502


if __name__ == "__main__":
    app.run(debug=True)
