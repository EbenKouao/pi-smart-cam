"""
Improve Password Security (Application)
=============================================
Use .env variables.
Access to less secure apps is turned on
- Use a dedicated email address
- Enable 2FA and use App Password to avoid storing your password in plain text.
https://support.google.com/accounts/answer/185833?hl=en

Note: Check the Spam folder (as it may automatically route alerts there)
"""

import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Send Email Function to target email address
def sendMessage(pi_email, pi_app_password, pi_port, pi_host, image):
    # Receiver (Email to send camera activity to) 
    notification_recipient = "<to-email>"
    
    try:
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'Pi Smart Cam: New Activity Detected'
        msgRoot['From'] = pi_email
        msgRoot['To'] = notification_recipient
        msgRoot.preamble = 'New Activity Detected'

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
        msgText = MIMEText('Motion Captured:')
        msgAlternative.attach(msgText)

        msgText = MIMEText('<img src="cid:image1">', 'html')
        msgAlternative.attach(msgText)
        
        msgImage = MIMEImage(image)
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        server = smtplib.SMTP_SSL(pi_host, pi_port)
        server.login(pi_email, pi_app_password)
        print("Sending Notification.")
        server.sendmail(pi_email, notification_recipient, msgRoot.as_string())
        server.quit()
        print("Notification Sent.")

    except:
        print("Notification not sent: Invalid email credentials")
        return "Invalid email credentials"

