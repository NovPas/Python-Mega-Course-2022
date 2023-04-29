import smtplib, ssl
from email.message import EmailMessage

def send(receiver_email, message):
    port = 465  # For SSL
    user = "novpas@gmail.com"
    password = "mvphixgpzgoumljf"
    server_name = "smtp.gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(server_name, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver_email, message)


if __name__ == "__main__":
    SUBJECT = 'test'
    TEXT = 'test message'
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    send('novpas@gmail.com', message)
