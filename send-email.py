import smtplib
import ssl
import os


##### ENV
port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("NOTI_USERNAME")
USER_PASSWORD = os.environ.get("NOTI_PASS")
DESTINATION_EMAIL = os.environ.get("DESTINATION_EMAIL")
GITHUB_RUNID = os.environ.get("GITHUB_RUNID")
GITHUB_REPO = os.environ.get("GITHUB_REPO")

##### EMAIL INFO
from_addr = USER_EMAIL
to_addr = DESTINATION_EMAIL #"dev-ops@whydah.xyz"
subj = "Failed email checking"
repo = GITHUB_REPO
ref = f"https://github.com/{GITHUB_REPO}/actions/runs/{GITHUB_RUNID}"
body = f"Dear sir,\nEmail checking rule has been violated!\nPlease check it out at: {ref}"
msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (from_addr, to_addr, subj, body)


try:
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context=context)
    server.login(USER_EMAIL, USER_PASSWORD)
    server.sendmail(from_addr, to_addr, msg)
    print("Email have been sent successfully!")
except smtplib.SMTPException as error:
    print(error)
