import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = 'your name'
email["to"] = 'email'
email['subject'] = "subject"

email.set_content("your message")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your', "your pass")
    smtp.send_message(email)
    print("all good boss!")
