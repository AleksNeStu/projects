"""Time module."""
import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
print('t: {}\n'.format(t))

t2 = time.clock()
print('clock: {}\n'.format(t2))

t3 = time.ctime()
print('ctime: {}\n'.format(t3))

t4 = time.gmtime()
print('gmtime: {}\n'.format(t4))

t5 = time.mktime(t)
print('mktime: {}\n'.format(t5))

t6 = time.sleep(1)

_t7 = time.localtime() # get struct_time
t7 = time.strftime("%m/%d/%Y, %H:%M:%S", _t7)
print('strftime: {}\n'.format(t7))

_t8 = "21 June, 2018"
t8 = time.strptime(_t8, "%d %B, %Y")
print('strptime: {}\n'.format(t8))

t9 = time.tzset()
print('tzset: {}\n'.format(t9))

