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
    app.app.config.update({
        'TESTING': True,
        # Default port is 5000
        'LIVESERVER_PORT': 7777,
        # Default timeout is 5 seconds
        'LIVESERVER_TIMEOUT': 10,
    })
    try:
        app.main(for_testing=True)
        app.register_blueprints()
    except Exception as err:
        logging.error(f'Error: "{err}" on try to init flask app')
        raise err

    yield app