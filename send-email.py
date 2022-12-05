import smtplib
import ssl
import os


##### ENV
port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("NOTI_USERNAME")
USER_PASSWORD = os.environ.get("NOTI_PASS")
DESTINATION_EMAIL = os.environ.get("DESTINATION_EMAIL")

##### EMAIL INFO
from_addr = USER_EMAIL
to_addr = DESTINATION_EMAIL
subj = "Failed email checking"
body = "Dear sir,\nEmail checking rule has been violated!"
msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (from_addr, to_addr, subj, body)


try:
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context=context)
    server.login(USER_EMAIL, USER_PASSWORD)
    server.sendmail(from_addr, to_addr, msg)
    print("Email have been sent successfully!")
except smtplib.SMTPException as error:
    print(error)
