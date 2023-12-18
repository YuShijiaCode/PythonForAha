import smtplib
from email.mime.text import MIMEText
from email.header import Header

# send email with SMTP
def send_email(sender, receivers, report):

    mail_host = "smtp.163.com"
    mail_user = "15642543250@163.com"
    mail_pass = "XXXXXXXXXX"  #password

    message = report
    message['From'] = Header("Joshua", 'utf-8')
    message['To'] = Header("Test", 'utf-8')

    subject = 'Report'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Send successfully")
    except smtplib.SMTPException:
        print("Error: Can not send email")

