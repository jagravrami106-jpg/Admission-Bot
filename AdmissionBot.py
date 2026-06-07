from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Admission AI Bot</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:100px;">

    <h1>🤖 Admission AI Assistant</h1>

    <input type="text" id="msg" placeholder="Ask anything..."
           style="width:400px; height:40px; font-size:18px;">

    <button onclick="sendMsg()"
            style="height:45px; font-size:18px;">
        Send
    </button>

    <div id="chat" style="margin-top:20px; font-size:18px;"></div>

<script>
async function sendMsg() {

    let msg = document.getElementById("msg").value;

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: msg
        })
    });

    let data = await response.json();

    document.getElementById("chat").innerHTML +=
        "<p><b>You:</b> " + msg + "</p>" +
        "<p><b>Bot:</b> " + data.reply + "</p>";

    document.getElementById("msg").value = "";
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"].lower()

    if "hi" in message or "hello" in message or "hey" in message:
        reply = "👋 Welcome to our Admission Assistant. How can I help you?"

    elif "institute" in message:
        reply = "🏫 Our institute name is IIMS Ahmedabad."

    elif "course" in message:
        reply = "📚 We offer AI, Machine Learning, Data Analytics, Cloud Computing and Cyber Security."

    elif "ai" in message:
        reply = "🤖 Our AI course includes Python, Machine Learning and live projects."

    elif "fees" in message:
        reply = "💰 Please contact our admission team for fee details."

    elif "internship" in message:
        reply = "🎓 We provide internship opportunities with live projects."

    elif "contact" in message or "phone" in message:
        reply = "📞 Contact: +91 7574090919"

    elif "location" in message or "address" in message:
        reply = "📍 Ahmedabad, Gujarat"

    elif "admission" in message:
        reply = "📝 For admission, please contact our admission team."

    elif "thank" in message:
        reply = "😊 You're welcome."

    elif "bye" in message:
        reply = "👋 Thank you for visiting."

    else:
        reply = "Sorry, I didn't understand. Please ask about courses, fees, internship, admission or contact information."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    print("Starting Flask...")
    app.run(debug=True)


