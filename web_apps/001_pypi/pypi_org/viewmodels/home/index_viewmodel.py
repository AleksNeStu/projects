from services import release_service, package_service, user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, num_packages: int, num_releases: int):
        super().__init__()
        self.packages = package_service.get_packages()
        self.latest_packages = package_service.get_latest_packages(
            num_packages, self.packages)

        self.releases = release_service.get_releases()
        self.latest_releases = release_service.get_latest_releases(
            num_releases, self.releases)

        self.users = user_service.get_users()