import flask

from infra.response_mod import response
from viewmodels.seo.sitemap_viewmodel import SiteMapViewModel

blueprint = flask.Blueprint('seo', __name__, template_folder='templates')


# Sitemap
@blueprint.route('/sitemap.xml')
@response(mimetype='application/xml', template_file='seo/sitemap.html')
def sitemap():
    vm = SiteMapViewModel(1000)

    return vm.to_dict()


# Robots
@blueprint.route('/robots.txt')
@response(mimetype='text/plain', template_file='seo/robots.txt')
def robots():
    return {}
