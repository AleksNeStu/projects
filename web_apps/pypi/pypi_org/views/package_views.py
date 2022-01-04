import flask

from infra.view_modifiers import response


blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
# @response(template_file='package/details.html')
def package_details(package_name):
    return "Package details for {}".format(package_name)
    # return flask.render_template('home/index.html', packages=TEST_PACKAGES)