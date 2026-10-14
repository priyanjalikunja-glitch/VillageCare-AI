
import os
import logging

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

# Reject excessively large HTTP request bodies.
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

logging.basicConfig(level=logging.INFO)


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/assistant")
def assistant():
    return render_template("index.html")


@app.errorhandler(413)
def request_too_large(error):
    return jsonify({
        "error": "Request is too large. Please shorten your question."
    }), 413


@app.route("/api/ask", methods=["POST"])
def ask_assistant():
    # Accept JSON requests only.
    if not request.is_json:
        return jsonify({
            "error": "Please send your question as JSON."
        }), 415

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid request. Please try again."
        }), 400

    question = data.get("question")

    if not isinstance(question, str) or not question.strip():
        return jsonify({
            "error": "Please enter your question."
        }), 400

    question = question.strip()

    if len(question) > 1000:
        return jsonify({
            "error": "Your question must be 1000 characters or fewer."
        }), 400

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        app.logger.error("GEMINI_API_KEY is not configured")
        return jsonify({
            "error": "AI service is not configured. Please try again later."
        }), 503

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "You are VillageCare AI, a health education assistant "
                "for village communities. Provide simple, general health "
                "information. Do not diagnose diseases or prescribe "
                "medicines. Encourage users to consult qualified healthcare "
                "professionals. For emergencies, advise immediate medical "
                "care and mention India's emergency number, 112. "
                "Reply in the user's language when possible.\n\n"
                f"Question: {question}"
            ),
        )

        answer = response.text

        if not isinstance(answer, str) or not answer.strip():
            app.logger.warning("Gemini returned an empty response")
            return jsonify({
                "error": "No answer was generated. Please try again."
            }), 502

        return jsonify({"answer": answer.strip()})

    except Exception:
        # Keep technical details in server logs, not in the public response.
        app.logger.exception("AI request failed")
        return jsonify({
            "error": (
                "The AI service is temporarily unavailable. "
                "Please try again later."
            )
        }), 502


if __name__ == "__main__":
    # Debug mode is disabled to avoid exposing debugger details.
    app.run(debug=False)
