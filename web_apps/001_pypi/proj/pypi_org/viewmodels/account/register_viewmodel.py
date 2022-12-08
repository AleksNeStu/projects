from services import user_service
from utils.validation import is_email_valid
from viewmodels.shared.viewmodelbase import AccountModelBase


class RegisterViewModel(AccountModelBase):
    def __init__(self):
        super().__init__()
        # <input type="text" class="form-control" placeholder=" Email"
        #  name="email" value="{{ email }}">
        # key: name attribute of input tag
        # value: email = post_form_dict.get('email', '') post data from end user (filed via UI)
        # value_resp: value_got (email) returned
        # ImmutableMultiDict([('name', '_n'), ('email', '_e'), ('password', '_p ')])
        # {'name': '_n', 'email': '_e', 'password': '_p'
        self.name = self.req_data.name
        self.age = self.req_data.age.strip()
        self.user = user_service.get_user(self.email) if self.email else None

    def validate(self):
        # Validate user existing
        if self.user:
            self.errors.append(
                f'A user with an email: {self.email} is already exists.')
        else:
            # Validate required fields
            # name
            if not self.name or not self.name.strip():
                self.errors.append('User name is required. ')

        self.validate_email_and_password()