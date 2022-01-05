import flask

from infra.view_modifiers import response


blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
# @response(template_file='package/details.html')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)


@blueprint.route('/<int:rank>')
def popular_package(rank: int):
    # print(type(rank), rank)
    return "The details for {}th most popular package".format(rank)