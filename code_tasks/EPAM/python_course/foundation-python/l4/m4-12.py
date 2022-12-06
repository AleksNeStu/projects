"""Decorators' arguments."""

import time

def pause(t):

    def wrapper(f):

        def tmp(*args, **kwargs):
            time.sleep(t)
            return f(*args, **kwargs)
        return tmp

    return wrapper

@pause(4)
def func(x, y):
    return x + y

print(func(1, 2))