import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = 'sayanproject@gmail.com'
SENDER_PASSWORD = 'wwww zzzz xxxx yyyy'  

def send_email(subject, recipients, content):    

    msg = MIMEMultipart()
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg.attach(MIMEText(content, 'html'))

    try:
        with smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT) as client:
            client.starttls()  # Enable encryption
            client.login(SENDER_EMAIL, SENDER_PASSWORD)
            client.send_message(msg)
            client.quit()
            print("Email sent successfully.")
    except smtplib.SMTPRecipientsRefused as e:
        print(f"Some recipients were refused: {e}")
    except Exception as e:
        print(f"Error sending email: {e}")



