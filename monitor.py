import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    sender_email = input("Enter your email address: ")
    receiver_email = input("Enter recipient's email address: ")
    password = input("Enter your email password: ")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, message.as_string())

def get_system_info():
    # ... (بقیه کد همانند قبل)

if __name__ == "__main__":
    while True:
        system_info = get_system_info()
        send_email("System Information", system_info)
        # اجرای اسکریپت هر 8 ساعت یکبار
        time.sleep(28800)