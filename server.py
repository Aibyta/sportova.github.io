from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

app = Flask(__name__)

CORS(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        date = data.get('date')
        slot = data.get('slot')

        sender = os.environ.get("EMAIL_ADDRESS")
        password = os.environ.get("EMAIL_PASSWORD")

        if not sender or not password:
            return jsonify({
                "status": "error",
                "message": "Email credentials not configured"
            }), 500

        subject = f"🎾 Booking Confirmed for {date}"
        html = f"""
        <html>
        <body>
            <h2>Hi {name},</h2>
            <p>✅ Your booking for <b>{slot}</b> on <b>{date}</b> is confirmed!</p>
            <p>🏸 See you at the Court!</p>
            <br><p style='color:gray;'>- SPORTOVA Team</p>
        </body>
        </html>
        """

        msg = MIMEMultipart("alternative")
        msg["From"] = sender
        msg["To"] = email
        msg["Subject"] = subject
        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, email, msg.as_string())

        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)