document.getElementById('sendButton').addEventListener('click', function() {
    sendMessage();
});

document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    let userInput = document.getElementById('userInput').value.trim();
    if (userInput !== "") {
        addUserMessage(userInput);
        document.getElementById('userInput').value = '';
        fetchBotResponse(userInput);
    }
}

function addUserMessage(message) {
    let chatbox = document.getElementById('chatbox');
    let userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = message;
    chatbox.appendChild(userMessage);
    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to bottom
}

function addBotMessage(message) {
    let chatbox = document.getElementById('chatbox');
    let botMessage = document.createElement('div');
    botMessage.className = 'message bot-message';
    botMessage.innerHTML = message;  // Use innerHTML to render HTML content
    chatbox.appendChild(botMessage);
    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to bottom
}

function fetchBotResponse(userInput) {
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ userInput: userInput })
    })
    .then(response => response.json())
    .then(data => {
        addBotMessage(data.botResponse);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
