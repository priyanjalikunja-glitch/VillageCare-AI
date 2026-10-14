
import os
import logging

from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai import errors

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Gemini API configuration
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


# Homepage
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Health check
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "message": "VillageCare AI API is running",
        "status": "ok"
    }), 200


# AI Assistant
@app.route("/api/ask", methods=["POST"])
def ask_assistant():
    if client is None:
        return jsonify({
            "error": "AI service is not configured. Check GEMINI_API_KEY."
        }), 503

    data = request.get_json(silent=True) or {}
    prompt = data.get("question") or data.get("message")

    if not isinstance(prompt, str) or not prompt.strip():
        return jsonify({
            "error": "Please enter a question."
        }), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "You are VillageCare AI, a helpful assistant for rural "
                "communities. Give clear, simple healthcare awareness "
                "information. Do not diagnose illnesses or replace "
                "a qualified healthcare professional. Encourage users "
                "to seek professional medical care when appropriate.\n\n"
                f"User question: {prompt.strip()}"
            )
        )

        answer = response.text

        if not answer:
            return jsonify({
                "error": "The AI returned an empty response. Please try again."
            }), 502

        return jsonify({"answer": answer}), 200

    except errors.APIError as exc:
        logger.exception("Gemini API request failed")

        if exc.code in (401, 403):
            return jsonify({
                "error": "AI authentication failed. Check GEMINI_API_KEY."
            }), 502

        if exc.code == 429:
            return jsonify({
                "error": "AI request limit reached. Please try again later."
            }), 429

        return jsonify({
            "error": "The AI service is temporarily unavailable. Please try again later."
        }), 502

    except Exception:
        logger.exception("Unexpected AI request failure")
        return jsonify({
            "error": "The AI service is temporarily unavailable. Please try again later."
        }), 502


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=False
    )
