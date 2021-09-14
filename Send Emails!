#code for a Python Gmail sender created and written by Bahram Esmailian

import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df
import numpy as np
import smtplib
from email.mime.text import MIMEText

#if you have multiple recievers please use the form ['recipient1','recipient2']
sender = 'your_email_here@gmail.com'
receivers = ['']

#the body of the messasge is written using HTML code
body = """<br>
        LOVE from,<br>
        BAHI"""
msg = MIMEText(body, 'html')

#change the subject name here 
msg['Subject'] = '<3'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#this code currently uses Gmail to send code! you can send using other services by looking up their host port and server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)

#login using your username and credentials
s.login(user = '', password = '')

#this sends the message to EACH recipient 1 time but can be increased by changing the range
#WARNING: This was not intended to send spam. Any illegal use of this code is NOT intended or reccomended. This code is for educational purposes ONLY.
#sending too many messages too quickly can result in a permanent or temporary ban by Google's spam detection. Use at your own risk.
for i in range(1):
    s.sendmail(sender, receivers, msg.as_string())
s.quit()
