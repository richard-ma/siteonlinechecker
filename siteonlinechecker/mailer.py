import smtplib

from loader import config
from email.mime.text import MIMEText

class Mailer(object):

    def __init__(self):
        self.mailer = None

    def send(self, subject, message,
            fromAddress = config.get('smtp', 'username'),
            toAddress = config.get('default', 'admin_email')):
        msg = MIMEText(message, _subtype='html')
        msg['Subject'] = subject
        msg['From'] = fromAddress
        msg['To'] = toAddress

        try:
            self.mailer = smtplib.SMTP_SSL(
                config.get('smtp', 'host'),
                config.get('smtp', 'port'))
            self.mailer.login(
                config.get('smtp', 'username'),
                config.get('smtp', 'password'))
            print 'login'

            self.mailer.sendmail(fromAddress, toAddress, msg.as_string())
            print 'send'
            self.mailer.quit()
            print 'quit'
            return True
        except Exception, e:
            print str(e)
            return False

if __name__ == '__main__':
    m = Mailer()
    m.send('test title', 'test content')
