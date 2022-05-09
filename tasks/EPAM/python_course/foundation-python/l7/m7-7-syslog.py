#1
from syslog import syslog

syslog('This is a debug message.')


# python debug.py
# cat /var/log/messages | tail


#2
import logging
import logging.handlers

log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
handler.setFormatter(formatter)

log.addHandler(handler)


def hello():
    log.debug('this is debug')
    log.critical('this is critical')

if __name__ == '__main__':
    hello()

# tail -n 2 /var/log/syslog