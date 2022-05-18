from viewmodels.shared.viewmodelbase import ViewModelBase


class PackageDetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str):
        super().__init__()
        self.package_name = package_name
        #TODO: Add init and validate logic
