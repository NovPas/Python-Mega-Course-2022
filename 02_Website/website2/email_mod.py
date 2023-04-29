import smtplib, ssl
import os


def send(receiver_email, topic, message):
    port = 465  # For SSL
    user = os.getenv('GMAIL_APP_USER')  # secret_data.EMAIL
    password = os.getenv('GMAIL_APP_PASSWORD')  # secret_data.APP_PASSWORD
    server_name = "smtp.gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()

    message_full = 'Subject: {}\n\nFrom: {}\nTopic: {}\n{}'.format('Streamlit App', receiver_email, topic, message)
    message_full = message_full.encode("UTF-8")

    with smtplib.SMTP_SSL(server_name, port, context=context) as server:
        server.login(user, password)
        server.sendmail(receiver_email, user, message_full)


if __name__ == "__main__":
    FROM = '1@1.com'
    Topic = 'Topic'
    message = 'Привет'
    send(FROM, Topic, message)
