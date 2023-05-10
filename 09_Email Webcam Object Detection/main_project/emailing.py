import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email(filename):
    # Replace with your email address and password
    EMAIL_ADDRESS = os.getenv('GMAIL_APP_USER')
    EMAIL_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')

    # Replace with the email address you want to send the email to
    TO_EMAIL_ADDRESS = 'novpas@gmail.com'

    # Create the message container
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL_ADDRESS
    msg['Subject'] = 'Camera detection!!!'

    # Add body text to the email
    body = 'Screen from web-camera'
    msg.attach(MIMEText(body, 'plain'))

    # Add an attachment to the email
    part = MIMEBase('application', 'octet-stream')
    with open(filename, 'rb') as attachment:
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filename))
    msg.attach(part)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, TO_EMAIL_ADDRESS, msg.as_string())
        print('Email sent successfully.')

    os.remove(filename)


if __name__ == '__main__':
    send_email('images/1.png')
