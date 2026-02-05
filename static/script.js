function sendMessage() {
  const input = document.getElementById("userInput");
  const msg = input.value.trim();
  if (!msg) return;

  const chatBox = document.getElementById("chatBox");

  const userDiv = document.createElement("div");
  userDiv.className = "user-message";
  userDiv.innerText = msg;
  chatBox.appendChild(userDiv);

  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: msg })
  })
  .then(res => res.json())
  .then(data => {
    const botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.innerText = data.answer;
    chatBox.appendChild(botDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}
