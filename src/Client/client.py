import smtplib
import email.utils
from email.mime.text import MIMEText

# Classe responsável por enviar os emails para o servidor
class EmailHandler:
    def __init__(self, server, receiver, receiver_mail, sender, sender_mail, subject, msg):
        self.server = server
        self.receiver = receiver_mail
        self.sender = sender_mail
        self.msg = MIMEText(msg)
        self.msg['To'] = email.utils.formataddr((receiver, receiver_mail))
        self.msg['From'] = email.utils.formataddr((sender, sender_mail))
        self.msg['Subject'] = subject
    
    # Utiliza o método sendmail para enviar dados ao servidor
    def send_email(self):
        try:
            self.server.sendmail(self.sender, [self.receiver], self.msg.as_string())
        finally:
            self.server.quit()


server = smtplib.SMTP()
server.connect('127.0.0.1', 1025)
server.set_debuglevel(True)  # show communication with the server

mail = EmailHandler(server, 'Carlos', 'carlos@email.com', 'Mary', 'mary@email.com', 'this is a test', 'this is the message')
mail.send_email()
