from typing import Optional, List, Union

import bson
import flask
from flask import Request

from infra import auth
from infra.request_mod import request_data
from utils.py import DictToObj
from utils.validation import is_email_valid


class ViewModelBase():
    def __init__(self):
        self.req: Request =  flask.request
        self.req_data: DictToObj = request_data()

        self.errors: Optional[List[str]] = []
        self.user_id: Union[
            int, bson.ObjectId, None] = auth.get_user_id_from_cookies(self.req)

    def to_dict(self):
        return self.__dict__

    def validate(self):
        pass


class AccountModelBase(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.email = self.req_data.email.lower().strip()
        self.password = self.req_data.password.strip()

    def validate_email_and_password(self):
        # email
        if not self.email or not self.email.strip():
            self.errors.append('Email is required. ')
        elif not is_email_valid(self.email):
            self.errors.append('Email has not valid format. ')
        # elif not is_email_valid(self.email, check_if_email_existing=True):
        #     self.errors.append('Email is not registered on the Internet '
        #                        'mail servers. ')

        # password
        if not self.password:
            self.errors.append('Password is required. ')
        elif len(self.password.strip()) < 8:
            self.errors.append('Password must be at least 8 characters. ')
