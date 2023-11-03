"""Getting time."""
import time


localtime1 = time.localtime(time.time())
print("Local current time:", localtime1)
print("year:", localtime1.tm_year)
print("tm_hour:", localtime1.tm_hour)


localtime2 = time.asctime(localtime1)
print("Local current time :", localtime2)


import calendar
# Return a month's calendar string (multi-line).
cal = calendar.month(2018, 5)
print("Here is the calendar:")
print(cal)