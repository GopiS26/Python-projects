import smtplib
from gesture import className

# Email configuration
sender_email = "gopi200826@gmail.com"
receiver_email = "gopi200026@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "gopi200826@gmail.com"
smtp_password = "vtyypuydgqqajkwc"

# Create email message
        
message = f"Detected Gesture: {className}\n\nHello,\n\nEmployees kindly perform {className} operation.\n\nRegards,\nGopi"

# Send email
try:
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
    smtp_obj.starttls()
    smtp_obj.login(smtp_username, smtp_password)
    smtp_obj.sendmail(sender_email, receiver_email, message)
    smtp_obj.quit()
    print(message)
    print("Email sent successfully.")
except Exception as e:
    print("Error sending email:", str(e))

