# Suppose you’ve written a Python package that you want to be able to pip install locally.
# Additionally, you also want to be able to run one of the scripts in the package via its name, without the .py extension and without explicitly using the Python interpreter to launch it. In other words, you want to be able to run standalone_script instead of
# python /path/to/my/package/standalone_script.py


# This way, each time you want to use the mypackage module, capitalize() becomes available. But you would need to go through the very tedious and error-prone approach of manually adding the path to mypackage every time you want to use it:

# some_script.py
# without setuptools
import sys
import os
# sys.path.append('/path/to/mypackage')

directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "mypackage"))
sys.path.insert(0, directory)

# from mypackage import capitalize

# print(capitalize('this'))

# That’s it! Now the package may be installed with pip as shown above and the capitalize script becomes available system-wide in the current Python environment. You might want to read the next