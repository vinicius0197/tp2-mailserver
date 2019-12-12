import unittest
import os.path
import os
import shutil

from src.SMTPServer.smtp_server import SMTPServer

class ServerTests(unittest.TestCase):
  def test_create_mail_name(self):
    server = SMTPServer(('localhost', 1025), None)
    server.process_message('teste', 'teste', ['teste'], 'this is some data')
    cwd = os.getcwd()
    path = cwd + '/mails/teste/'
    self.assertTrue(os.path.exists(path))
    self.assertTrue(len(os.listdir(path) ) != 0)
    shutil.rmtree(path, ignore_errors=True)
    server.close()


if __name__ == '__main__':
    unittest.main()