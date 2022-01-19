import flask

from infra.view_modifiers import response
from services import package_service, release_service, user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    packages = package_service.get_packages()
    latest_packages = package_service.get_latest_packages(3, packages)
    # releases ordered by relationship in data.models.package.Package
    latest_packages_map = [{
        'name': p.id,
        'latest_version': p.releases[0].version_text,
        'summary': p.summary,
    } for p in latest_packages]

    releases = release_service.get_releases()
    users = user_service.get_users()

    return {
        'latest_packages': latest_packages_map,
        'package_count': packages.count(),
        'release_count': releases.count(),
        'user_count': users.count(),
    }
    # return flask.render_template('home/index.html', packages=TEST_PACKAGES)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
    # return flask.render_template('home/about.html')