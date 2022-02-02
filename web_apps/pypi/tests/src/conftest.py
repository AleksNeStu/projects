import logging
import os

import pytest
import sys

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../pypi_org'))
sys.path.insert(0, directory)

import app

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@pytest.yield_fixture(scope="session")
def flask_app():
    flask_app = app.app
    flask_app.config.update({
        'TESTING': True,
    })
    try:
        app.main(for_testing=True)
    except Exception as err:
        logging.error(f'Error: "{err}" on try to init flask app')
        raise err

    yield flask_app