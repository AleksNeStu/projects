import asyncio
import inspect
import pathlib
import sys
from contextlib import contextmanager
from importlib.metadata import version as pk_version
from pprint import pprint
from typing import Union, Callable, Dict, Type, Optional

from codetiming import Timer
from deepdiff import DeepDiff
from packaging import version


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


def pk_ver(pk_name: str) -> version.Version:
    ver_str = pk_version(pk_name)
    ver = version.parse(ver_str)
    return ver


def pk_ver_diff(pk_name: str, exp_ver: str = None, eq: bool = None, more: bool = None, less: bool = None) -> bool:
    act_ver_parsed = pk_ver(pk_name)
    exp_ver_parsed = version.parse(exp_ver)
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
    if eq:
        return bool(act_ver_parsed == exp_ver_parsed)

def get_dir(file = None) -> pathlib.Path:
    if not file:
        # Get the caller's frame (the frame one level above the current frame)
        caller_frame = inspect.currentframe().f_back
        # Get the file path from the frame
        file = caller_frame.f_globals['__file__']

    dir = pathlib.Path(file).resolve().parent
    return dir


def sys_path_insert(dir_path: pathlib.PosixPath | pathlib.Path = None):
    if not dir_path:
        dir_path = get_dir()
    dir_path_posix = dir_path.as_posix()
    if dir_path.is_dir():
        if dir_path_posix not in sys.path:
            sys.path.insert(0, dir_path_posix)
    else:
        raise ValueError(f"{dir_path_posix} is not exists, failed to sys path insert")