# TODO: 1)Add unit, functional, integration tests with dir structure
# 2) Add tests runner script
# 3) Cover by tests core cases
# Consider Flask-Testing extension
from unittest import mock

import pytest

from viewmodels.account.register_viewmodel import RegisterViewModel
from views.account_views import register_post


class TestRegister:

    @pytest.mark.parametrize(
        'form_data', [
            {
                'name': 'user_name',
                'email': 'user_name@gmail.com',
                'password': '@' * 8
            },
        ],
        ids=['Nominal']
    )
    @mock.patch('services.user_service.get_user')
    def test_valid(self, get_user_mock, form_data, flask_app):
        get_user_mock.return_value = None

        with flask_app.test_request_context(
                path='/account/register', data=form_data):
            vm = RegisterViewModel()
            vm.validate()
            assert vm.errors == []
            # TODO: add test cases
            resp = register_post()
            # resp.status_code
            # resp.location
            # resp.data

            # TODO: Add tests with test_client
        # with flask_app.test_client() as c:
        #     resp = c.get('/?arg1=77')
        #     assert request.args['arg1'] == '77'
