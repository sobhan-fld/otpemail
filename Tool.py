import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import uuid


def send_email(subject, message, sender_email, sender_password, receiver_email):
    # Server details
    smtp_server = 'smtp.servidor-correo.net'
    smtp_port = 587
    sender_email = sender_email
    sender_password = sender_password
    receiver_email = receiver_email

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Message-ID'] = email.utils.make_msgid()
    print("This is Message ID (For header) {}".format(msg['Message-ID']))

    # Create the body of the message (a plain-text and an HTML version).
    text = message
    html = """\
    <html>
      <body>
        <p>{}</p>
      </body>
    </html>
    """.format(message)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error: Unable to send email -", e)
    finally:
        server.quit()


def send_email_complete(receivers_mail, context):
    subject = "Test Email"
    sender_password = "Asd.1234567890"
    sender_email = "sobhan@maxsens.es"

    send_email(subject, context, sender_email, sender_password, receivers_mail)



# send_email_complete('sobhan.fld2@gmail.com','hello')
# # fields we need to send the mail
# if __name__ == "__main__":
#     subject = "Test Email"
#     message = "This is a test email using sobhan laptop yes."
#     sender_email = "sobhan@maxsens.es"
#     sender_password = "Asd.1234567890"
#     receiver_email = "sobhan.fld2@gmail.com"  # Change to the recipient's email address
#     send_email(subject, message, sender_email, sender_password, receiver_email)
