import smtplib, ssl
import secret_data


def send(receiver_email, message):
    port = 465  # For SSL
    user = secret_data.EMAIL
    password = secret_data.APP_PASSWORD
    server_name = "smtp.gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()

    message_full = 'Subject: {}\n\nFrom: {}\n{}'.format('Streamlit App', receiver_email, message)
    message_full = message_full.encode("UTF-8")

    with smtplib.SMTP_SSL(server_name, port, context=context) as server:
        server.login(user, password)
        server.sendmail(receiver_email, user, message_full)


if __name__ == "__main__":
    FROM = '1@1.com'
    message = 'Привет'
    send(FROM, message)
