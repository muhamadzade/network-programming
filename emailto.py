import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr='muhamadzade@gmail.com'
##fromaddr='jmohmadz@alumni.ut.ac.ir'
toLs=['muhamadzade@gmail.com','j.mohammadzadeh@kiau.ac.ir',
      'kia_10900@gmail.com','jmohmadz@alumni.ut.ac.ir','kia10900@yahoo.com']
##to='muhamadzade@gmail.com'
##to='j.mohammadzadeh@kiau.ac.ir'
for to in toLs:
    msg=MIMEMultipart()
    msg['From']=fromaddr
    msg['To']=to
    msg['Subject']='test subject'
    body='This is just a message'
    msg.attach(MIMEText(body,'plain'))
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(fromaddr,'3agevelgard')
    text=msg.as_string()
    server.sendmail(fromaddr,to,text)
    print('Email send')
server.quit()

