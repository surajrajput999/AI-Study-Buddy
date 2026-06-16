async function askAI(endpoint) {
    const text = document.getElementById('inputText').value;
    
    if (!text) {
        alert('Please enter some text or study notes first!');
        return;
    }
    
    document.getElementById('outputText').innerText = "AI is thinking... 🤔";
    
    try {
        // endpoint variable decide karega ki summarize karna hai ya flashcard banana hai
        const response = await fetch(`http://127.0.0.1:5000/api/${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        document.getElementById('outputText').innerText = data.result;
        
    } catch (error) {
        console.error("Error:", error);
        document.getElementById('outputText').innerText = "Oops! Could not connect to the backend server.";
    }
}

// Dono buttons ko unke endpoints se jod diya
document.getElementById('summarizeBtn').addEventListener('click', () => askAI('summarize'));
document.getElementById('flashcardBtn').addEventListener('click', () => askAI('flashcards'));