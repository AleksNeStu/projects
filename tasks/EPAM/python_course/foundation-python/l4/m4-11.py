"""Decorators."""

import time

def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Function execution time: %f" % (time.time()-t))
        return res

    return tmp

@timer
def func(x, y):
    return x + y

h = func(1, 2)
print(h)
