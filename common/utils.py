import asyncio
import inspect
from contextlib import contextmanager
from typing import Union, Callable

from codetiming import Timer


@contextmanager
def w_err(*exception_types, func_name: str = None):
    try:
        if not func_name:
            st = inspect.stack()
            st_locals = [st.frame.f_locals for st in st]
            funcs_set = {i["func"] for i in st_locals if i.get("func")}
            if len(funcs_set) == 1:
                func_name = list(funcs_set)[0].__name__
        yield
    except exception_types as ex:
        print(f"Func: {func_name}, exception: {repr(ex)}")

def timer_dc(func):
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

def timer_cm(text: Union[str, Callable[[float], str]] = "Context manager operation elapsed time: {:.6f} s", *args, **kwargs):
    return Timer(text=text, *args, **kwargs)