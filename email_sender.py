import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = 'Ali'
email["to"] = 'mircea.mitroi10@gmail.com'
email['subject'] = "this email was sent automatically"

email.set_content(
    "This email is sent from python \n PS we're still up for gta later")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ali.kanameh@gmail.com', "0214300322")
    smtp.send_message(email)
    print("all good boss!")
