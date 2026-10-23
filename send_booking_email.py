import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_booking_email(name, email, slot, date):
    sender_email = "aibytatech@gmail.com"
    sender_password = "lhky eqtt jaow hfvo"  # Use app password from Gmail
    receiver_email = email

    subject = f"🎾 Booking Confirmation for {date}"
    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">
      <h2>Hi {name},</h2>
      <p>Your booking for the slot <b>{slot}</b> on <b>{date}</b> is confirmed! 🎉</p>
      <hr />
      <p>See you soon at the Court.</p>
      <p style="color:gray;">- SPORTOVA Team</p>
    </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
        return True
    except Exception as e:
        print("❌ Error sending email:", e)
        return False
