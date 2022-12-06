"""Time tuple."""
import time

# def localtime(seconds=None): # real signature unknown; restored from __doc__
#     """
#     localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
#                               tm_sec,tm_wday,tm_yday,tm_isdst)
#
#     Convert seconds since the Epoch to a time tuple expressing local time.
#     When 'seconds' is not passed in, convert the current time instead.

localtime = time.localtime(time.time())
print("Local current time :", localtime)