#TODO: Refactor the same code parts
#TODO: Consider Flask-WTF
import flask

from infra import auth
from infra.response_mod import response
from services import user_service
from viewmodels.account.index_viewmodel import IndexViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
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
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
# Action method
def register_post():
    # View method
    vm = RegisterViewModel() # Imlicit request usage infra.request_mod.request_data
    # Get user from DB
    vm.validate() # Pull from request.form

    if vm.errors:
        return vm.to_dict()

    try:
        # Create a new user
        vm.user = user_service.create_user(vm.name, vm.email, vm.password)
        # vm.user_session.login(vm.user.id) # Implicit response.set_cookies()
    except Exception as err:
        vm.errors.append(f'The account can not be created. Reason: "{err}". ')
        return vm.to_dict()

    resp = flask.redirect('/account')
    auth.set_auth_cookie(resp, vm.user.id)

    return resp


# LOGIN
@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    vm = LoginViewModel()
    vm.validate()

    if vm.errors:
        return vm.to_dict()

    # Validate user existing
    user = user_service.get_user(vm.email, vm.password)
    if not user:
        # Do not check exact error due to sec purposes
        vm.errors.append(
            'The account does not exist or the password is wrong. ')
        return vm.to_dict()

    resp = flask.redirect('/account')
    auth.set_auth_cookie(resp, user.id)

    return resp


# LOGOUT
@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    auth.del_auth_cookie(resp)

    return resp
