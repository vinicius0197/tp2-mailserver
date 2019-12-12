import unittest
import os.path
import os
import shutil


from src.MailOutputHandler.mail_output_handler import MailOutputHandler

class MailOutputHandlerTests(unittest.TestCase):
  def test_create_mail_name(self):
    mail = MailOutputHandler('teste_name')
    mail.create_mail_name()
    self.assertTrue(mail.mail_name != 'teste_name')
  
  def test_create_mail_folder(self):
    mail = MailOutputHandler('teste_name')
    mail.create_mail_name()
    mail.create_mail_folder('teste@email.com')
    cwd = os.getcwd()
    full_path = cwd + '/mails/teste@email.com/'
    self.assertTrue(os.path.exists(full_path))
    shutil.rmtree(full_path, ignore_errors=True) # remove a pasta após conclusão do teste

  def test_save_to_file(self):
    mail = MailOutputHandler('teste_name')
    mail.create_mail_name()
    mail.create_mail_folder('teste@email.com')
    cwd = os.getcwd()
    full_path = cwd + '/mails/teste@email.com/'
    mail.save_to_file('teste message', cwd)
    self.assertTrue(len(os.listdir(full_path) ) != 0)
    shutil.rmtree(full_path, ignore_errors=True) # remove a pasta após conclusão do teste

if __name__ == '__main__':
    unittest.main()