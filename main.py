import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, password, subject, body):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Create a secure SSL context and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

# Usage
sender = "Miguel.am.Gomez23@gmail.com"
receiver = "mgomez139@my.scccd.edu"
app_password = "qmkz yosx ddhn eeaz"  # Consider using a more secure method to store and retrieve this; from sender
subject = "11/22/23 Message to chris!"
body = """ This should go through at 11:28AM
Fall winter, sumer spring
"""

send_email(sender, receiver, app_password, subject, body)

