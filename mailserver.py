import smtpd
import asyncore
import os

class MailOutputHandler:

    def save_to_file(self, file_name, msg):
        with open(file_name, 'w') as outfile:
            outfile.write(msg)

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        mail = MailOutputHandler()
        cwd = os.getcwd()
        outfile_name = os.path.join(cwd, 'message.eml')
        mail.save_to_file(outfile_name, data)
        print('msg: ', data)


server = CustomSMTPServer(('localhost', 1025), None)

asyncore.loop()