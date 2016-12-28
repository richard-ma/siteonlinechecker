import smtplib

from loader import config

class Mailer(object):

    def __init__(self):
        self.mailer = smtplib.SMTP_SSL(
            config.get('smtp', 'host'),
            config.get('smtp', 'port'))
        self.mailer.login(
            config.get('smtp', 'username'),
            config.get('smtp', 'password'))
        print 'login'

    def send(self, toAddr, msg):
        self.mailer.sendmail(
            config.get('smtp', 'username'),
            toAddr,
            msg)
        print 'send'
        self.mailer.quit()
        print 'quit'

if __name__ == '__main__':
    m = Mailer()
    m.send('178613284@qq.com', 'test mail')
