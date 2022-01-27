import logging
from typing import Optional

import flask

from utils import py as py_utils
from utils import sec as sec_utils

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


def get_user_id_from_cookies(request: flask.Request) -> Optional[int]:
    auth_cookie_val = request.cookies.get(_AUTH_COOKIE_KEY)

    if not auth_cookie_val:
        logging.warning("No user id in cookies")
        return

    auth_cookie_val_p = auth_cookie_val.split(':::')
    if len(auth_cookie_val_p) != 2:
        logging.warning("User id in cookies has wrong format")
        return

    act_user_id, act_user_hash = auth_cookie_val_p
    exp_user_hash = sec_utils.txt_to_hash(act_user_id)
    if exp_user_hash != act_user_hash:
        logging.warning(
            f"Actual user id: {act_user_id} hash from cookies: {exp_user_hash}"
            f" is mismatched to expected")
        return

    return py_utils.str_to_int(act_user_id)