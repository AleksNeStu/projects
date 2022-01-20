import flask

from infra.view_modifiers import response
from services import package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    if not package_name:
        return flask.abort(status=404)

    package_id = package_name.strip().lower()
    package = package_service.get_package(id=package_id)
    if not package:
        return flask.abort(status=404)

    latest_release = None
    is_latest = True
    latest_version = "0.0.0"
    if package.releases:
        latest_release = package.releases[0]
        latest_version = latest_release.version_text

    return {
        'package': package,
        'latest_release': latest_release,
        'latest_version': latest_version,
        'release_version': latest_version,
        'is_latest': is_latest,
    }
    # return flask.redirect(package.package_url)
    # return "Package details for {}".format(package.id)


@blueprint.route('/<int:rank>')
def popular_package(rank: int):
    # print(type(rank), rank)
    return "The details for {}th most popular package".format(rank)