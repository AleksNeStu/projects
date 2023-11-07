import flask
import flask_sijax

from infra.response_mod import response
from viewmodels.home.index_viewmodel import IndexViewModel

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

    # get query string example
    # DONOT uncomment to avoid loop back
    # requests.get('http://localhost:5000/?arg1=val1&arg2=val2')
    # req_data.arg1, req_data.arg2
    # get query string example

    vm = IndexViewModel(num_packages=3, num_releases=10)

    # releases ordered by relationship in data.models.package.Package
    latest_packages_map = [{
        'name': p.id,
        'latest_version': p.releases[0].version_text,
        'summary': p.summary,
    } for p in vm.latest_packages]

    # releases ordered by relationship in data.models.package.Package
    latest_releases_map = [{
        'r_name': r.package.id,
        'r_version': r.version_text,
        'r_summary': r.package.summary,
        'r_url': r.package.package_url,
    } for r in vm.latest_releases]

    return {
        'latest_releases_map': latest_releases_map,
        'package_count': vm.packages.count(),
        'release_count': vm.releases.count(),
        'user_count': vm.users.count(),
    }
    # return flask.render_template('home/index.html', packages=TEST_PACKAGES)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
    # from jinja2 import Template
    # return flask.render_template('home/about.html')

# # http://exploreflask.com/en/latest/views.html
# @blueprint.route('/examples/<string:param1>/<int:param2>/')
# @response(template_file=Template(
#     'Examples response params: {{ param1, param2 }}'))
# def examples(param1: str, param2: int):
#     return {
#         'param1': param1,
#         'param2': param2,
#     }

# http://exploreflask.com/en/latest/views.html
@blueprint.route('/examples/<string:param1>/<int:param2>/')
@response(template_file='home/examples.html')
def examples(param1: str, param2: int):
    return {
        'param1': param1,
        'param2': param2,
    }