document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chatBox = document.getElementById('chat-box');

    function appendMessage(text, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
        messageDiv.textContent = text;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const text = userInput.value.trim();
        if (text === "") return;

        // Display user message
        appendMessage(text, true);
        userInput.value = '';

        try {
            const response = await fetch('/get_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();
            
            // Display bot response
            appendMessage(data.answer, false);
        } catch (error) {
            console.error('Error:', error);
            appendMessage("Sorry, something went wrong. Please check your connection.", false);
        }
    }

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});
