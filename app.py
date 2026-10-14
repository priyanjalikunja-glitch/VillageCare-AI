
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

    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        app.logger.error("GEMINI_API_KEY is not configured")
        return jsonify({
            "error": "AI service configuration is missing."
        }), 500

    prompt = f"""
You are VillageCare AI, a helpful healthcare information assistant
for people in villages and communities.

IMPORTANT RULES:
1. Always respond in English, regardless of the language used by the user.
2. Use simple, clear English that is easy to understand.
3. Provide general health information only.
4. Do not diagnose illnesses or prescribe medicines.
5. Encourage users to consult a qualified healthcare professional.
6. For serious or life-threatening emergencies in India, advise calling 112
   or going to the nearest emergency department.
7. Be polite, supportive, and concise.

User question: {question}
"""

    try:
        client = genai.Client(api_key=api_key)

        # Try the primary model first.
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )

        except Exception:
            app.logger.exception(
                "Primary Gemini model failed; trying fallback model"
            )

            # Try the fallback model.
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
                "Please try again later."
            )
        }), 502


if __name__ == "__main__":
    app.run(debug=True)
