# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart



subject = 'python email test'

sendfile = open('/Users/guoshuairan/Documents/GitHub/SeleniumStudy/mytestpro-master/126.py','rb').read()

att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"]="application/octet-stream"
att["Content-Disposition"] = 'attachment;filename = "126.py"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)


smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()


for study git hub

