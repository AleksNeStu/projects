import flask

from services import package_service
from viewmodels.shared.viewmodelbase import ViewModelBase


#TODO: Consider pytlon libs:
# https://github.com/inveniosoftware/flask-sitemap
# https://pypi.org/project/ultimate-sitemap-parser/
# https://pypi.org/search/?q=sitemap
class SiteMapViewModel(ViewModelBase):
    def __init__(self, limit: int):
        super().__init__()
        self.packages = package_service.get_latest_packages(limit)
        self.last_updated_text = "2022-02-04"
        self.site = f'{flask.request.scheme}://{flask.request.host}'
