import smtpd
import asyncore
import datetime
import os
from src.MailOutputHandler.mail_output_handler import MailOutputHandler

class SMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        mail = MailOutputHandler(mailfrom)
        mail.create_mail_folder(rcpttos[0])
        
        cwd = os.getcwd()
        mail.save_to_file(data, cwd)
        print('msg: ', data)