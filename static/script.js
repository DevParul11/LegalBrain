function sendMessage() {
    let inputBox = document.getElementById("user-input");
    let message = inputBox.value;

    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    // User message
    let userMsg = document.createElement("p");
    userMsg.innerHTML = "<strong>You:</strong> " + message;
    chatBox.appendChild(userMsg);

    // Send to backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        let botMsg = document.createElement("p");
        botMsg.innerHTML = "<strong>Legal Brain:</strong> " + data.reply;
        chatBox.appendChild(botMsg);
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    inputBox.value = "";
}

