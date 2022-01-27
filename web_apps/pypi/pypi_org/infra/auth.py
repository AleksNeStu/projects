from datetime import timedelta
from typing import Optional

import flask

from utils import sec as sec_utils
from utils import py as py_utils

_AUTH_COOKIE_KEY = 'pypi_user'
_AUTH_COOKIE_VAL_FORMAT = "{}:::{}" # user_id, user_hash


def set_auth_cookie(response: flask.Response, user_id: int):
    user_hash = sec_utils.txt_to_hash(str(user_id))
    auth_cookie_val = _AUTH_COOKIE_VAL_FORMAT.format(user_id, user_hash)
    # response.headers._list
    # ('Set-Cookie', 'pypi_user=86:::HASH; HttpOnly; Path=/; SameSite=Lax')]
    response.set_cookie(
        key=_AUTH_COOKIE_KEY, value=auth_cookie_val, secure=False,
        httponly=True, samesite='Lax')


def del_auth_cookie(response: flask.Response):
    response.delete_cookie(_AUTH_COOKIE_KEY)