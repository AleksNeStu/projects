import flask
import flask_sijax

from infra.response_mod import response
from services import package_service, release_service, user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@flask_sijax.route(blueprint, '/')
@response(template_file='home/index.html')
def index():
    # sijax example
    if flask.g.sijax.is_sijax_request:
        flask.g.sijax.register_callback(
            'SIJAX', lambda resp: resp.alert('SIJAX'))
        return flask.g.sijax.process_request()
    # sijax example

    packages = package_service.get_packages()
    latest_packages = package_service.get_latest_packages(3, packages)
    # releases ordered by relationship in data.models.package.Package
    latest_packages_map = [{
        'name': p.id,
        'latest_version': p.releases[0].version_text,
        'summary': p.summary,
    } for p in latest_packages]

    releases = release_service.get_releases()
    latest_releases = release_service.get_latest_releases(10, releases)
    # releases ordered by relationship in data.models.package.Package
    latest_releases_map = [{
        'r_name': r.package.id,
        'r_version': r.version_text,
        'r_summary': r.package.summary,
        'r_url': r.package.package_url,
    } for r in latest_releases]

    users = user_service.get_users()

    return {
        'latest_releases_map': latest_releases_map,
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