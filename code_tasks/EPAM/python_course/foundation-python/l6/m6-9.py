"""Time & Tick."""
import time

# for Unix system, January 1, 1970, 00:00:00 at UTC is epoch
# (the point where time begins).
ticks = time.time()
print("Number of ticks passed since epoch", ticks)


# seconds passed since epoch
local_time = time.ctime(ticks)
print("Local time:", local_time)