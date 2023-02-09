#send and email with python
    #go over to our gmail account and setup 2 factor authentication
    #generate app pasword
    # create a function to send the mail

## existe una clase llamada app2.py donde esta la contraseña. password = "contraseña"
from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'pablitomdl1@gmail.com' #email personal
email_password = password
email_receiver = 'ditepe8617@ekcsoft.com' #dirección de correo temporal generada en esta página https://temp-mail.org/es/

subject = "prueba"
body = """
esto es un mensaje de prueba
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

#otra forma 
# from email.message import EmailMessage
# import smtplib

# remitente = "pablitomdl1@gmail.com"
# destinatario = "ditepe8617@ekcsoft.com"
# mensaje = "¡Hola, mundo!"


# email = EmailMessage()
# email["From"] = remitente
# email["To"] = destinatario
# email["Subject"] = "Correo de prueba"
# email.set_content(mensaje)

# smtp = smtplib.SMTP_SSL("smtp.gmail.com")
# smtp.login(remitente, password)
# smtp.sendmail(remitente, destinatario, email.as_string())
# smtp.quit()