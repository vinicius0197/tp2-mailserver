import unittest

from src.MailOutputHandler.mail_output_handler import MailOutputHandler

class Test(unittest.TestCase):
  def test_create_mail_name(self):
    mail = MailOutputHandler('teste_name')
    mail.create_mail_name()
    self.assertTrue(mail.mail_name != 'teste_name')

if __name__ == '__main__':
    unittest.main()