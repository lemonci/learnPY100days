from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    # Create an email object with attachment
    message = MIMEMultipart()
    # Create text file
    text_content = MIMEText('The attachment contains this month\'s data. \r\n Please check.', 'plain', 'utf-8')
    message['Subject'] = Header('Monthly data', 'utf-8')
    message['From'] = Header('abcdefg@126.com', 'utf-8')
    message['To'] = Header('Bob', 'utf-8')
    message.attach(text_content)
    # Read the file and attach it to the message
    with open('xxx/r.pdf', 'rb') as f:
        pdf = MIMEText(f.read(), 'base64', 'utf-8')
        pdf['Content-Type'] = 'application/pdf'
        pdf['Content-Disposition'] = 'attachment; filename=r.pdf'
        message.attach(pdf)

    # Create SMTP object
    smtper = SMTP('smtp.126.com', 587)
    smtper.ehlo()
    smtper.starttls()
    smtper.ehlo()
    sender = 'abcdefg@126.com'
    receivers = ['uvwxyz@qq.com']
    smtper.login(sender, 'secretpass')
    #send email
    smtper.sendmail(sender, receivers, message.as_string())
    # disconnect
    smtper.quit()
    print('Sending is finished!')

if __name__ == '__main__':
    main()