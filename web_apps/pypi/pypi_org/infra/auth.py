from datetime import timedelta
from typing import Optional

import flask

from utils import sec as sec_utils
from utils import py as py_utils

AUTH_COOKIE_NAME = 'pypi_user'


def set_auth_cookie_to_resp(response: flask.Response, user_id: int):
    hash_val = sec_utils.txt_to_hash(str(user_id))
    val = "{}:::{}".format(user_id, hash_val)
    # response.headers._list
    # ('Set-Cookie', 'pypi_user=86:::HASH; HttpOnly; Path=/; SameSite=Lax')]
    response.set_cookie(
        key=AUTH_COOKIE_NAME, value=val, secure=False, httponly=True,
        samesite='Lax')
