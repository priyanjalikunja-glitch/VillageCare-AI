
// =====================================
// VillageCare AI - Assistant JavaScript
// =====================================

const askButton = document.getElementById("askButton");
const questionInput = document.getElementById("question");
const answerBox = document.getElementById("answer");
const languageSelect = document.getElementById("languageSelect");
const voiceButton = document.getElementById("voiceButton");
const speakButton = document.getElementById("speakButton");

const languageNames = {
    "en-US": "English",
    "te-IN": "Telugu",
    "hi-IN": "Hindi"
};

// Read the AI answer aloud
function speakText(text) {
    if (!("speechSynthesis" in window)) {
        answerBox.textContent =
            "Speech playback is not supported in this browser.";
        return;
    }

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = languageSelect.value;
    speech.rate = 0.9;

    window.speechSynthesis.speak(speech);
}

// Ask the AI Assistant
async function askAssistant() {
    const question = questionInput.value.trim();

    if (!question) {
        answerBox.textContent =
            "Please type or speak a question first.";
        return;
    }

    askButton.disabled = true;
    askButton.textContent = "Thinking...";
    answerBox.textContent =
        "VillageCare AI is preparing your answer...";

    try {
        const response = await fetch("/api/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question,
                language:
                    languageNames[languageSelect.value] || "English"
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.error || "Unable to get an answer."
            );
        }

        if (!data.answer) {
            throw new Error("The AI returned an empty answer.");
        }

        answerBox.textContent = data.answer;

    } catch (error) {
        console.error("VillageCare AI error:", error);

        answerBox.textContent =
            "Unable to generate an answer: " + error.message;

    } finally {
        askButton.disabled = false;
        askButton.textContent = "Ask Assistant →";
    }
}

// Ask Assistant button
if (askButton) {
    askButton.addEventListener("click", askAssistant);
}

// Voice input button
if (voiceButton) {
    voiceButton.addEventListener("click", function () {
        const SpeechRecognition =
            window.SpeechRecognition ||
            window.webkitSpeechRecognition;

        if (!SpeechRecognition) {
            answerBox.textContent =
                "Voice input is not supported. Please try Google Chrome.";
            return;
        }

        const recognition = new SpeechRecognition();

        recognition.lang = languageSelect.value;
        recognition.continuous = false;
        recognition.interimResults = false;

        voiceButton.disabled = true;
        voiceButton.textContent = "Listening...";

        recognition.onresult = function (event) {
            questionInput.value =
                event.results[0][0].transcript;
        };

        recognition.onerror = function (event) {
            answerBox.textContent =
                "Microphone error: " + event.error +
                ". Check microphone permission and try again.";
        };

        recognition.onend = function () {
            voiceButton.disabled = false;
            voiceButton.textContent = "🎤 Speak Question";
        };

        try {
            recognition.start();
        } catch (error) {
            voiceButton.disabled = false;
            voiceButton.textContent = "🎤 Speak Question";

            answerBox.textContent =
                "Unable to start the microphone. Please try again.";
        }
    });
}

// Read Answer button
if (speakButton) {
    speakButton.addEventListener("click", function () {
        const text = answerBox.textContent.trim();

        if (
            !text ||
            text === "Your answer will appear here." ||
            text === "VillageCare AI is preparing your answer..."
        ) {
            answerBox.textContent =
                "Please ask a question first.";
            return;
        }

        speakText(text);
    });
}
