import os
import sys

# TODO: Fix no module settings.py inside of docker and uwsgi
from pypi_org.app import app


if __name__ == '__main__':
    app.main()