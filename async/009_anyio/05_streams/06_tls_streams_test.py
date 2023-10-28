# Creating self-signed certificates on the fly
import ssl

import pytest
import trustme
import os
import ssl

from anyio import connect_tcp, run
from anyio import create_tcp_listener
from anyio.streams.tls import TLSListener

from common.utils import get_dir

@pytest.fixture(scope='session')
def ca():
    return trustme.CA()


@pytest.fixture(scope='session')
def server_context(ca):
    server_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ca.issue_cert('localhost').configure_cert(server_context)
    return server_context


@pytest.fixture(scope='session')
def client_context(ca):
    client_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ca.configure_trust(client_context)
    return client_context

# You can then pass the server and client contexts from the above fixtures to TLSListener, wrap() or whatever you use on either side.