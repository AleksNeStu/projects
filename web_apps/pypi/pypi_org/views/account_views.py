#TODO: Refactor the same code parts
import flask
from werkzeug.datastructures import ImmutableMultiDict

from infra import auth
from infra.request_mod import request_data
from infra.response_mod import response
from services import user_service

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# INDEX
@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    req: flask.Request = flask.request
    # No user auth cookies
    user_id = auth.get_user_id_from_cookies(req)
    if not user_id:
        return flask.redirect('/account/login')

    # User id from auth cookies not in DB
    user = user_service.get_user_by_id(user_id)
    if not user:
        return flask.redirect('/account/login')

    return {
        'user': user,
    }


# REG
@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    req_data = request_data()

    # <input type="text" class="form-control" placeholder=" Email"
    #  name="email" value="{{ email }}">
    # key: name attribute of input tag
    # value: email = post_form_dict.get('email', '') post data from end user (filed via UI)
    # value_resp: value_got (email) returned
    # ImmutableMultiDict([('name', '_n'), ('email', '_e'), ('password', '_p ')])
    # {'name': '_n', 'email': '_e', 'password': '_p'}
    name = req_data.name
    email = req_data.email.lower().strip()
    password = req_data.password.strip()
    resp_dict = {
        'name': name,
        'email': email,
        'password': password,
    }

    # Validate required fields
    empty_reg_fields = [
        name for name, value in resp_dict.items() if not value]
    #TODO: add email format validation and password strong policy
    if empty_reg_fields:
        resp_dict['error'] = (
            f'{empty_reg_fields} are empty, but should be filled to '
            f'pass the registration procedure.')
        return resp_dict

    # Validate user existing
    user = user_service.create_user(name, email, password)
    if not user:
        resp_dict['error'] = (
            f'A user with an email: {email} is already exists.')
        return resp_dict

    resp = flask.redirect('/account')
    auth.set_auth_cookie(resp, user.id)

    return resp


# LOGIN
@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    req_data = request_data()

    email = req_data.email.lower().strip()
    password = req_data.password.strip()
    resp_dict = {
        'email': email,
        'password': password,
    }

    # Validate required fields
    empty_reg_fields = [
        name for name, value in resp_dict.items() if not value]
    if empty_reg_fields:
        resp_dict['error'] = (
            f'{empty_reg_fields} are empty, but should be filled to '
            f'pass the login procedure.')
        return resp_dict

    # Validate user existing
    user = user_service.get_user(email, password)
    if not user:
        # Do not check exact error due to sec purposes
        resp_dict['error'] = (
            f'The account does not exist or the password is wrong.')
        return resp_dict

    resp = flask.redirect('/account')
    auth.set_auth_cookie(resp, user.id)

    return resp


# LOGOUT
@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    auth.del_auth_cookie(resp)

    return resp
