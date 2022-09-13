import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

load_dotenv()

# Creating inputs of email
from_addr = os.environ.get("FROM_ADDR")
if not from_addr:
    raise TypeError('env variable not set: FROM_ADDR')
to_addr = os.environ.get("TO_ADDR")

if not to_addr:
    raise TypeError('env variable not set: TO_ADDR')

subject = 'This is an email with an attachment sent from python'
content = 'Heuritech sign in form'
email_password = os.environ.get("EMAIL_PASSWORD")
if not email_password:
    raise TypeError('env variable not set: EMAIL_PASSWORD')

# Create multipart email and set headers
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

# Add body to email
body = MIMEText(content, 'plain')
msg.attach(body)
filename = 'test_yaml.yml'

# Open file
with open(filename, 'r') as f:
    attachment = MIMEApplication(f.read(), Name=basename(filename))
    attachment['Content-Disposition'] = 'attachment; filename = "{}"'.format(basename(filename))

# Add attachment
msg.attach(attachment)

# Log into server
server = smtplib.SMTP('mail.gandi.net', 587)
server.login(from_addr, email_password)

# Send email with attachment
server.send_message(msg, from_addr, to_addr)
