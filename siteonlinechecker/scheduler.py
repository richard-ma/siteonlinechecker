from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick %s' % datetime.now())

if __name__ == '__main__':
    s = BlockingScheduler()
    s.add_job(tick, 'interval', minutes=3)

    try:
        s.start()
    except (KeyboardInterrupt, SystemExit):
        pass
