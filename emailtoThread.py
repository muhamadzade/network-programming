import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from threading import Thread



class EmailThread(Thread):
    def __init__(self, email_to):
        self.email_to = email_to
        Thread.__init__(self)

    def run (self):
        body = "your html abc body"
        text = "your plain abc body"
        message = MIMEMultipart("alternative")
        message["Subject"] = "subject" 
        message["From"] = "kasra"
        message["To"] = self.email_to
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(body, "html")
        message.attach(part1)
        message.attach(part2)
        to= self.email_to
        fromaddr="infinity.xd85@gmail.com"
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr,'kiakasraarash321')
        text=message.as_string()
        server.sendmail(fromaddr,to,text)
        print('Email send')



if __name__=="__main__":
    EmailThread("infinity.xd85@gmail.com").start()    
    EmailThread("muhamadzade@gmail.com").start()
    EmailThread("j.mohammadzadeh@gmail.com").start()
