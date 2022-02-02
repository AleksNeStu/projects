from typing import Optional, TypedDict, List

import flask
from flask import Request

from infra import auth
from infra.request_mod import request_data
from utils.py import DictToObj


class ViewModelBase():
    def __init__(self):
        self.req: Request =  flask.request
        self.req_data: DictToObj = request_data()

        self.errors: Optional[List[str]] = []
        self.user_id: Optional[int] = auth.get_user_id_from_cookies(self.req)

    def to_dict(self):
        return self.__dict__

    def validate(self):
        pass