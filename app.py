
import os

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)


# Homepage
@app.route("/")
def home():
    return render_template("dashboard.html")


# AI Healthcare Assistant page
@app.route("/assistant")
def assistant():
    return render_template("index.html")


# Ask the AI assistant
@app.route("/api/ask", methods=["POST"])
def ask_assistant():
    data = request.get_json(silent=True) or {}

    question = data.get("question", "").strip()
    language = data.get("language", "English").strip().lower()

    if not question:
        return jsonify({
            "error": "Please enter or speak your question."
        }), 400

    # Accept only the supported response languages.
    if language in ("telugu", "te", "te-in"):
        response_language = "Telugu"
    else:
        response_language = "English"

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        app.logger.error("GEMINI_API_KEY is not configured")
        return jsonify({
            "error": "AI service configuration is missing."
        }), 500

    prompt = f"""
You are VillageCare AI, a helpful healthcare information assistant
for people in villages and communities.

RESPONSE LANGUAGE:
Reply entirely in {response_language}.
If the response language is Telugu, use natural Telugu written in Telugu script.
Do not reply in English unless needed for a medical term.

IMPORTANT HEALTH SAFETY RULES:
1. Provide general health information only.
2. Do not claim to diagnose illnesses.
3. Do not prescribe medicines or dosages.
4. Encourage users to consult a qualified healthcare professional.
5. For serious or life-threatening emergencies in India,
   advise calling 112 or going to the nearest emergency department.
6. Use simple, clear, supportive language.
7. If the question is unrelated to health, politely explain that
   you mainly help with general healthcare information.

User question:
{question}
"""

    try:
        client = genai.Client(api_key=api_key)

        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )

        except Exception:
            app.logger.exception(
                "Primary Gemini model failed; trying fallback model"
            )

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        answer = response.text

        if not answer:
            raise ValueError("Gemini returned an empty response.")

        return jsonify({"answer": answer}), 200

    except Exception:
        app.logger.exception("Gemini API request failed")

        return jsonify({
            "error": (
                "AI service is temporarily unavailable. "
                "Please check the Flask terminal."
            )
        }), 502


if __name__ == "__main__":
    app.run(debug=True)
