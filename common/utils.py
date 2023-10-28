import asyncio
import inspect
from contextlib import contextmanager

from pprint import pprint
from typing import Union, Callable, Dict, Type, Optional

from codetiming import Timer
from deepdiff import DeepDiff

from packaging import version
from importlib.metadata import version as pk_version

def get_diff(act, exp, is_assert: bool = True):
    diff = DeepDiff(act, exp)
    if diff:
        pprint(diff, indent=4)

    if is_assert:
        assert not diff
    else:
        return diff


# TODO: Consider to use exception_types with exp messages, to have extra assertion, for now return err for futher processing
@contextmanager
def w_err(exceptions: Dict[Type[Exception], Optional[str]] = None, func_name: str = None):
    try:
        if not func_name:
            st = inspect.stack()
            st_locals = [st.frame.f_locals for st in st]
            funcs_set = {i["func"] for i in st_locals if i.get("func")}
            if len(funcs_set) == 1:
                func_name = list(funcs_set)[0].__name__
        yield
    except Exception as ex:
        act_ex = ex.__class__
        act_msg = repr(ex)
        if exceptions:
            exp_msg = exceptions.get(act_ex, False)
            if exp_msg is not False:
                if exp_msg is not None:
                    diff = get_diff(act_msg, exp_msg, is_assert=False)
                    if diff:
                        raise ex
            else:
                raise ex

        print(f"Func: `{func_name}`, exception: `{act_msg}` was caught, not raised")


def timer_dc(func):
    # TypeError: '_GeneratorContextManager' object does not support the asynchronous context manager protocol
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


def timer_cm(text: Union[str, Callable[[float], str]] = "Context manager operation elapsed time: {:.6f} s", *args,
             **kwargs):
    return Timer(text=text, *args, **kwargs)


def get_pk_ver(pk_name: str) -> version.Version:
    ver_str = pk_version(pk_name)
    ver = version.parse(ver_str)
    return ver


def compare_pk_ver(pk_name: str, exp_ver: str = None, eq: bool = None, more: bool = None, less: bool = None) -> bool:
    act_ver_parsed = get_pk_ver(pk_name)
    exp_ver_parsed = version.parse(exp_ver)
    if eq:
        return bool(act_ver_parsed == exp_ver_parsed)
    if more:
        if eq:
            return bool(act_ver_parsed >= exp_ver_parsed)
        else:
            return bool(act_ver_parsed > exp_ver_parsed)
    if less:
        if eq:
            return bool(act_ver_parsed <= exp_ver_parsed)
        else:
            return bool(act_ver_parsed < exp_ver_parsed)