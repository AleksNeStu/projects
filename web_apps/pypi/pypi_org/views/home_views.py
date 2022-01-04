import flask

from infra.view_modifiers import response
from services import package_service


blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    return {
        'packages': package_service.get_latest_packages()
    }
    # return flask.render_template('home/index.html', packages=TEST_PACKAGES)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
    # return flask.render_template('home/about.html')