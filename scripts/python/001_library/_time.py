import time

def measure_time(func):
    def inner(*args, **kwargs):
        ex_time = None
        start_time = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            ex_time = time.time() - start_time
            print(f'Execution time: {ex_time:.15f} seconds')
    return inner

@measure_time
def g(i):
    return i ^ 222222222


# measure_time(g)(777)
g(33)

#==============================================================================
from dataclasses import dataclass

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float

from pympler import asizeof
simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
res = asizeof.asizesof(simple, slot)
print(res)

from timeit import timeit
t1 = timeit('slot.name',
            setup="slot=SlotPosition('Oslo', 10.8, 59.9)",
            globals=globals())
# 0.05882283499886398
print(t1)
t2 = timeit('simple.name',
            setup="simple=SimplePosition('Oslo', 10.8, 59.9)",
            globals=globals())
# 0.09207444800267695
print(t2)