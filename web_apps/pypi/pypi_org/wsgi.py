import os
import sys


# # add_module_to_sys_path
# directory = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), ''))
# sys.path.insert(0, directory)

from app import app, main


if __name__ == '__main__':
    main()