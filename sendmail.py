import smtplib as sm
import ssl
import os

def send_email(message):
    host="smtp.gmail.com"
    port=465
    username="hgagra12@gmail.com"
    password=os.getenv("PASSWORD")

    reciever="hgagra12@gmail.com"

    context=ssl.create_default_context()

    with sm.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,reciever,message)


