import asyncio
from contextlib import contextmanager
from contextlib import suppress
from typing import Union, Callable

from codetiming import Timer


class Temp:
    def exception_handler(func):
        def inner_function(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as ex:
                print(f"Func: {func.__name__}, exception: {repr(ex)}")
        return inner_function

    @contextmanager
    def skip_exceptions(*exceptions):
        try:
            yield
        except exceptions as ex:
            f = 1
            print(f"Func: {'sd'}, exception: {repr(ex)}")
            pass

    # with skip_exceptions(Exception):
    #     d = {}
    #     d1 = d["sdsd"]
    #     d2 = d["lol2"]


    class suppress_new(suppress):

        def __init__(self, *exceptions):
            super().__init__(*exceptions)

        def __exit__(self, exctype, excinst, exctb):
            # Unlike isinstance and issubclass, CPython exception handling
            # currently only looks at the concrete type hierarchy (ignoring
            # the instance and subclass checking hooks). While Guido considers
            # that a bug rather than a feature, it's a fairly hard one to fix
            # due to various internal implementation details. suppress provides
            # the simpler issubclass based semantics, rather than trying to
            # exactly reproduce the limitations of the CPython interpreter.
            #
            # See http://bugs.python.org/issue12029 for more details
            return exctype is not None and issubclass(exctype, self._exceptions)


    with suppress_new(KeyError):
        d = {}
        d1 = d["sdsd"]


def timer_d(func):
    async def async_wrapper(*args, **kwargs):
        with Timer(text=f"Async func `{func.__name__}` elapsed time: {{:.6f}} s"):
            return await func(*args, **kwargs)

    def sync_wrapper(*args, **kwargs):
        with Timer(text=f"Sync func `{func.__name__}` elapsed time: {{:.6f}} s"):
            return func(*args, **kwargs)

    def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return async_wrapper(*args, **kwargs)
        else:
            return sync_wrapper(*args, **kwargs)

    return wrapper


def timer_c(text: Union[str, Callable[[float], str]] = "Context manager operation elapsed time: {:.6f} s", *args, **kwargs):
    return Timer(text=text, *args, **kwargs)

# TODO: Consider to extend Timer class behaviour