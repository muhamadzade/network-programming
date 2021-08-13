import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from threading import Thread

# fromaddr='infinity.xd85@gmail.com'
# ##fromaddr='jmohmadz@alumni.ut.ac.ir'
# toLs=['muhamadzade@gmail.com','amirkasrakaka@gmail.com','infinity.xd85@gmail.com']
# ##to='muhamadzade@gmail.com'
# ##to='j.mohammadzadeh@kiau.ac.ir'
# for to in toLs:
#     msg=MIMEMultipart()
#     msg['From']=fromaddr
#     msg['To']=to
#     msg['Subject']='test subject'
#     body='This is just a message'
#     msg.attach(MIMEText(body,'plain'))
#     server=smtplib.SMTP('smtp.gmail.com:587')
#     server.starttls()
#     server.login(fromaddr,'kiakasraarash321')
#     text=msg.as_string()
#     server.sendmail(fromaddr,to,text)
#     print('Email send')
# server.quit()
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