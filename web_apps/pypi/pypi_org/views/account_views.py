#TODO: Refactor the same code parts
#TODO: Consider Flask-WTF
import flask

from infra import auth
from infra.request_mod import request_data
from infra.response_mod import response
from services import user_service
from viewmodels.account.index_viewmodel import IndexViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# INDEX
@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    vm.validate()

    if vm.errors:
        return flask.redirect('/account/login')

    return vm.to_dict()


# REG
@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.errors:
        return vm.to_dict()

    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        # TODO: add reason
        vm.errors.append('The account can not be created.')
        return vm.to_dict()

    # sqlalchemy.orm.exc.DetachedInstanceError: Instance <User at 0x7f5dc0a5afe0> is not bound to a Session; attribute refresh operation cannot proceed (Background on this error at: https://sqlalche.me/e/14/bhk3)
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
