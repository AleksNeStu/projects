import os
import sys

# TODO: Fix no module settings.py inside of docker and uwsgi
from pypi_org.app import app, main

# # add_module_to_sys_path
# directory = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, directory)


if __name__ == '__main__':
    main()