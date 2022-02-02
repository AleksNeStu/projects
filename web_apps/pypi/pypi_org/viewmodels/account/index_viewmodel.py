from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.get_user_by_id(self.user_id)

    def validate(self):
        if not self.user_id:
            self.errors.append('No user id. ')
        if self.user_id and not self.user:
            self.errors.append('No user. ')