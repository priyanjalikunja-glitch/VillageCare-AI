
const askButton = document.getElementById("askButton");
const questionInput = document.getElementById("question");
const answerBox = document.getElementById("answer");

askButton.addEventListener("click", async function () {
    const question = questionInput.value.trim();

    if (!question) {
        answerBox.textContent = "Please enter your question first.";
        return;
    }

    askButton.disabled = true;
    askButton.textContent = "Thinking...";
    answerBox.textContent = "VillageCare AI is preparing your answer...";

    try {
        const response = await fetch("/api/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to get an answer.");
        }

        answerBox.textContent = data.answer;
    } catch (error) {
        answerBox.textContent =
            error.message || "Something went wrong. Please try again.";
    } finally {
        askButton.disabled = false;
        askButton.textContent = "Ask Assistant →";
    }
});
