import secrets
import smtplib
import string

def generate_secure_code(email2):
   
    random_code = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(8))
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    email = "bongalos.justinejaeg8@gmail.com"
    server.login(email,"bpajpgtgaaofdoaq")
    server.sendmail(email,email2,random_code)
    return random_code
