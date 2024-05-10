import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import uuid


def send_email(subject, message, sender_email, sender_password, receiver_email):
    smtp_server = 'smtp.servidor-correo.net'
    smtp_port = 587

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Message-ID'] = email.utils.make_msgid()

    text = message
    html = f"<html><body><p>{message}</p></body></html>"

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('email sent')
        # logging.info("Email sent successfully!")
    except smtplib.SMTPException as e:
        print('unable to send email')
        # logging.error("Error: Unable to send email", exc_info=True)
    finally:
        server.quit()


def send_email_complete(receivers_mail, context):
    subject = "Test Email"
    sender_password = "Asd.1234567890"
    sender_email = "sobhan@maxsens.es"

    send_email(subject, context, sender_email, sender_password, receivers_mail)


