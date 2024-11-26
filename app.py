from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample Data (replace with actual email data from API integration)
emails = [
    {"id": 1, "sender": "alice@example.com", "subject": "Project Update", "body": "Please review the attached file.", "priority": "High", "sentiment": "Neutral"},
    {"id": 2, "sender": "bob@example.com", "subject": "Meeting Reminder", "body": "Reminder for our meeting tomorrow.", "priority": "Medium", "sentiment": "Positive"},
    {"id": 3, "sender": "charlie@example.com", "subject": "Invoice Due", "body": "Please process the attached invoice.", "priority": "High", "sentiment": "Negative"},
]

@app.route("/")
def dashboard():
    return render_template("dashboard.html", emails=emails)

@app.route("/email/<int:email_id>")
def email_view(email_id):
    email = next((email for email in emails if email["id"] == email_id), None)
    if email:
        return render_template("email_view.html", email=email)
    return "Email not found", 404

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)
