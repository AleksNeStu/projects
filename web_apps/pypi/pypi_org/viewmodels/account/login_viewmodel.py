from viewmodels.shared.viewmodelbase import AccountModelBase


class LoginViewModel(AccountModelBase):

    def validate(self):
        self.validate_email_and_password()
