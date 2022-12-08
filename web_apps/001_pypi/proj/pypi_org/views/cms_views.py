import flask

from infra.response_mod import response
from services import cms_service
from viewmodels.cms.page_viewmodel import PageViewModel

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    # print("Getting CMS page for '/{}' URL".format(full_url))
    vm = PageViewModel(full_url)
    vm.validate()

    if vm.errors:
        return flask.abort(404)

    return vm.page