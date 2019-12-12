import smtpd
import asyncore
import datetime
import os
from src.MailOutputHandler.mail_output_handler import MailOutputHandler
from src.SMTPServer.smtp_server import SMTPServer

server = SMTPServer(('localhost', 1025), None)
asyncore.loop()