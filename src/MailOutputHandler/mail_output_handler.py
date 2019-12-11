import smtpd
import asyncore
import datetime
import os

# Classe responsável por salvar os e-mails recebidos no servidor de modo
# que o usuário possa acessá-los novamente.
class MailOutputHandler:

    def __init__(self, mail_name):
        self.mail_name = mail_name
        self.user_path = ''

    # Cria um nome para o email ser salvo no filesystem
    def create_mail_name(self):
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.mail_name = date_now + ' - ' + self.mail_name

    # Caso um determinado usuário já tenho recebido emails, salva e-mails nessa pasta
    def create_mail_folder(self, user_path):
        self.user_path = '/mails/' + user_path
        if not os.path.exists('mails/' + user_path):
            os.makedirs('mails/' + user_path)

    # Salva o email como um arquivo .eml no filesystem
    def save_to_file(self, msg, path):
        self.create_mail_name()
        outfile_name = path + self.user_path + '/' + self.mail_name + '.eml'
        with open(outfile_name, 'w') as outfile:
            outfile.write(msg)