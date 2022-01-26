import flask
from werkzeug.datastructures import ImmutableMultiDict

from infra.view_modifiers import response
from services import user_service

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################### INDEX #################################
@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    return {}


# ################### REGISTER #################################
@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    r: flask.Request = flask.request

    # <input type="text" class="form-control" placeholder=" Email"
    #  name="email" value="{{ email }}">
    # key: name attribute of input tag
    # value: email = post_form_dict.get('email', '') post data from end user (filed via UI)
    # value_resp: value_got (email) returned
    post_form: ImmutableMultiDict = r.form
    # ImmutableMultiDict([('name', '_n'), ('email', '_e'), ('password', '_p ')])
    post_form_dict: dict = post_form.to_dict()
    # {'name': '_n', 'email': '_e', 'password': '_p'}

    # Registration error
    name = post_form_dict.get('name', '')
    email = post_form_dict.get('email', '').lower().strip()
    password = post_form_dict.get('password', '').strip()
    resp_dict = {
        'name': name,
        'email': email,
        'password': password,
    }
    empty_reg_fields = [
        name for name, value in resp_dict.items() if not value]
    #TODO: add email format validation and password strong policy
    if empty_reg_fields:
        resp_dict.update({
            'error': f'{empty_reg_fields} are empty, but should be filled to'
                     f' pass the registration procedure.',
        })
        return resp_dict

    # Success registration
    user = user_service.create_user(name, email, password)
    #TODO: login in browser as a session
    return flask.redirect('/account')


# ################### LOGIN #################################
@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    return {}


# ################### LOGOUT #################################
@blueprint.route('/account/logout')
def logout():
    return {}
