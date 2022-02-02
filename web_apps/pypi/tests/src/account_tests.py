# TODO: 1)Add unit, functional, integration tests with dir structure
# 2) Add tests runner script
# 3) Cover by tests core cases
# Consider Flask-Testing extension
from unittest import mock

from flask import Response

from data.generated_all_db_models import User
# from tests.src.conftest import client

import pytest
import flask

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
        app = flask_app.app

        with app.test_request_context(
                path='/account/register', data=form_data):
            # Test view model
            vm = RegisterViewModel()
            vm.validate()
            assert vm.errors == []

            # Test view method
            reg_resp = register_post()
            # resp.status_code
            # resp.location
            # resp.data

            # Test views
            # projects/web_apps/pypi/pypi_org/data/models


        # Integrated tests
        with app.test_client() as client:
            resp: Response = client.get('/')
            assert resp.status_code == 200
            assert b'Find, install and publish Python packages' in resp.data

            resp: Response = client.get('/account')
            assert resp.status_code == 200
            assert resp.location == 'http://localhost/None'
