// Check if JS is loaded
console.log("JS Loaded ✅");

// Get Question
async function getQuestion() {
    console.log("Start button clicked");

    const topic = document.getElementById("topic").value;

    if (!topic) {
        alert("Please enter a topic");
        return;
    }

    // Show loading
    document.getElementById("question").innerText = "AI is thinking... 🤖";

    try {
        const res = await fetch(`http://127.0.0.1:8000/question?topic=${topic}`);
        const data = await res.json();

        console.log("Question API:", data);

        document.getElementById("question").innerText = data.question;
    } catch (error) {
        console.error("Error fetching question:", error);
        document.getElementById("question").innerText = "Error loading question ❌";
    }
}


// Submit Answer
async function submitAnswer() {
    console.log("Submit button clicked");

    const answer = document.getElementById("answer").value;

    if (!answer) {
        alert("Please write an answer");
        return;
    }

    // Show loading
    document.getElementById("result").innerText = "Evaluating... ⏳";

    try {
        const res = await fetch("http://127.0.0.1:8000/evaluate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ answer: answer })
        });

        const data = await res.json();

        console.log("Evaluation API:", data);

        document.getElementById("result").innerText =
            `Score: ${data.score}/10\n\n` +
            `Feedback: ${data.feedback}\n\n` +
            `Improvements:\n- ${data.improvement.join("\n- ")}`;

    } catch (error) {
        console.error("Error evaluating answer:", error);
        document.getElementById("result").innerText = "Error evaluating answer ❌";
    }
}