import logging
from functools import wraps

import flask
import werkzeug
import werkzeug.wrappers

from infra import auth


def response(*, mimetype: str = None, template_file: str = None, **kwargs):
    def response_inner(func):
        logging.info("Wrapping in response func: {}".format(func.__name__))

        @wraps(func)
        def view_method(*args, **kwargs):
            resp_val = func(*args, **kwargs)

            # resp_val = flask.make_response(
            #     flask.render_template('any.html'))
            if isinstance(resp_val,
                          (werkzeug.wrappers.Response, flask.Response)):
                return resp_val

            is_resp_val_dict = isinstance(resp_val, dict)
            if is_resp_val_dict:
                resp_val.update(kwargs)

            model = resp_val if resp_val else {}

            if template_file:
                # TODO: consider flask session
                # https://pythonise.com/series/learning-flask/flask-session-object
                # set user_id param from cookies to every template for auth purposes
                resp_val['user_id'] = auth.get_user_id_from_cookies()
                if is_resp_val_dict:
                    resp_val = flask.render_template(
                        template_file, **resp_val)
                else:
                    raise Exception(
                        "Invalid return type {}, expected a dict.".format(
                            type(resp_val)))

            resp = flask.make_response(resp_val)
            resp.model = model
            if mimetype:
                resp.mimetype = mimetype

            return resp

        return view_method

    return response_inner


def template(template_file: str = None):
    def template_inner(f):
        @wraps(f)
        def view_method(*args, **kwargs):
            data_dict = f(*args, **kwargs)
            if not isinstance(data_dict, dict):
                raise Exception(
                    "Invalid return type {}, expected a dict.".format(
                        type(data_dict)))

            return flask.render_template(template_file, **data_dict)

        return view_method

    return template_inner
