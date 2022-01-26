import flask
from werkzeug.datastructures import ImmutableMultiDict

from infra.view_modifiers import response

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
    #  name="email" value="">
    # key: name attribute of input tag
    # value: post data from end user (filed via UI)
    post_form: ImmutableMultiDict = r.form
    # ImmutableMultiDict([('name', '_n'), ('email', '_e'), ('password', '_p ')])
    post_form_dict: dict = post_form.to_dict()
    # {'name': '_n', 'email': '_e', 'password': '_p'}
    return {
        'name': post_form_dict.get('name'),
        'email': post_form_dict.get('email').lower().strip(),
        'password': post_form_dict.get('password').strip(),
    }


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
