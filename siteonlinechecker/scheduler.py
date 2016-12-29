from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import apscheduler
import logging

from loader import config, data
from mailer import Mailer
from checker import Checker

def run():
    failed_list = Checker().checkCases(data)
    if len(failed_list) > 0:
        message = '\n'.join(failed_list)
        m = Mailer().send('Error Site - (%d)' % len(failed_list), message)

if __name__ == '__main__':
    log = logging.getLogger('apscheduler.executors.default')
    log.setLevel(logging.INFO)
    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)

    s = BlockingScheduler()
    s.add_job(run, 'interval', seconds=5)

    try:
        s.start()
    except (KeyboardInterrupt, SystemExit), e:
        print e
