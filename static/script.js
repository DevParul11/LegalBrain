const inputField = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = sender === "user" ? "user-message" : "bot-message";
  msg.innerText = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  const userText = inputField.value.trim();
  if (!userText) return;

  addMessage(userText, "user");
  inputField.value = "";

 fetch("/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ message: userText }),
})
.then((res) => res.json())
.then((data) => {
  addMessage(data.reply, "bot");
});

}
