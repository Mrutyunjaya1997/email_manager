from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data
user_data = {
    "name": "John Doe",
    "profile_picture": "https://via.placeholder.com/50",
    "role": "Manager",
}

emails = [
    {"id": 1, "sender": "alice@example.com", "subject": "Project Update", "date": "2024-10-01", "priority": "High", "sentiment": "Neutral"},
    {"id": 2, "sender": "bob@example.com", "subject": "Meeting Reminder", "date": "2024-10-02", "priority": "Medium", "sentiment": "Positive"},
    {"id": 3, "sender": "charlie@example.com", "subject": "Invoice Submission", "date": "2024-10-03", "priority": "High", "sentiment": "Negative"},
]

@app.route("/")
def dashboard():
    query = request.args.get('query', '')
    filtered_emails = [email for email in emails if query.lower() in email["subject"].lower()]
    return render_template("dashboard.html", user=user_data, emails=filtered_emails, query=query)

@app.route("/compose")
def compose_email():
    return "Compose Email Page (Under Construction)"

@app.route("/priority/<priority>")
def priority_view(priority):
    filtered_emails = [email for email in emails if email["priority"] == priority]
    return render_template("priority_view.html", priority=priority, emails=filtered_emails)


if __name__ == "__main__":
    app.run(debug=True)
