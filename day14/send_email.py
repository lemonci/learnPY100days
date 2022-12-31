from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    # Please change sender and password info
    sender = 'abcdefg@126.com'
    receivers = ['uvwxyz@qq.com', 'uvwxyz@126.com']
    message = MIMEText('Use Python to send a email.', 'plain', 'utf-8')
    message['From'] = Header('Alice', 'utf-8')
    message['To'] = Header('Bob', 'utf-8')
    message['Subject'] = Header('Test email', 'utf-8')
    smtper = SMTP('smtp.126.com', 587)
    smtper.ehlo()
    smtper.starttls()
    smtper.ehlo()
    smtper.login(sender, 'password')
    smtper.sendmail(sender, receivers, message.as_string())
    print('Email is sent.')

if __name__ == '__main__':
    main()