from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# =========================
# LEGAL BRAIN – MASTER DATA
# =========================

LEGAL_BRAIN = [

    {
        "topic": "Helmet Rule",
        "keywords": ["helmet", "headgear", "without helmet", "pillion helmet"],
        "answer": "As per Section 129 of the Motor Vehicles Act, wearing protective headgear is mandatory for both rider and pillion rider. Violation attracts a fine of ₹1000 and suspension of driving licence.",
        "section": "Section 129 – Wearing of protective headgear"
    },

    {
        "topic": "Drunk Driving",
        "keywords": ["drunk", "alcohol", "drink and drive", "drunk driving"],
        "answer": "Driving under the influence of alcohol is a punishable offence. Penalty includes a fine up to ₹10,000 or imprisonment up to 6 months.",
        "section": "Section 185 – Driving by a drunken person"
    },

    {
        "topic": "Driving Licence",
        "keywords": ["licence", "license", "dl", "driving licence", "without licence"],
        "answer": "No person shall drive a motor vehicle in a public place without holding a valid driving licence.",
        "section": "Section 3 – Necessity for driving licence"
    },

    {
        "topic": "Speed Limit",
        "keywords": ["speed", "overspeed", "over speeding", "speed limit"],
        "answer": "Drivers must comply with speed limits prescribed for the road or vehicle category. Violation is punishable under law.",
        "section": "Section 112 – Limits of speed"
    },

    {
        "topic": "Red Light / Signal Violation",
        "keywords": ["red light", "signal jump", "traffic signal"],
        "answer": "Drivers must obey traffic signs and signals. Violation of traffic signals is a punishable offence.",
        "section": "Section 119 – Duty to obey traffic signs"
    },

    {
        "topic": "Insurance",
        "keywords": ["insurance", "vehicle insurance", "without insurance"],
        "answer": "Using a motor vehicle without a valid insurance policy is a punishable offence.",
        "section": "Section 146 – Necessity for insurance against third party risk"
    },

    {
        "topic": "Accident Duty",
        "keywords": ["accident", "hit and run", "road accident"],
        "answer": "In case of an accident, the driver must stop the vehicle and provide medical assistance to the injured person.",
        "section": "Section 134 – Duty of driver in case of accident"
    }

]

# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()

    for rule in LEGAL_BRAIN:
        for keyword in rule["keywords"]:
            if keyword in user_msg:
                return jsonify({
                    "reply": f"{rule['answer']} (Source: {rule['section']})"
                })

    return jsonify({
        "reply": "Legal Brain provides answers only related to Traffic Rules and the Motor Vehicles Act, 1988. Please ask a relevant traffic-related question."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

