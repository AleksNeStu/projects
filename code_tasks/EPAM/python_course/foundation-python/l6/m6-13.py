"""Other modules for working with 'time'."""

# datetime
import datetime

datetime_now = datetime.datetime.now()
date_now = datetime.date.today()
print("datetime_now: {}, date_now: {}\n".format(
    datetime_now, date_now))


# pytz
import pytz

tz_NY = pytz.timezone('America/New_York')
datetime_now_NY = datetime.datetime.now(tz_NY)
print("NY time:", datetime_now_NY.strftime("%H:%M:%S"))


#dateutil
from dateutil.easter import *
from dateutil import relativedelta
from dateutil import parser
from dateutil import rrule

now = parser.parse("Sat Oct 11 17:13:46 UTC 2003")
today = datetime.datetime.now().date()
year = rrule.rrule(
    rrule.YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=rrule.FR)[0].year
rdelta = relativedelta.relativedelta(easter(year), today)
print("Today is: %s" % today)
print("Year with next Aug 13th on a Friday is: %s" % year)
print("How far is the Easter of that year: %s" % rdelta)
print("And the Easter of that year is: %s" % (today + rdelta))