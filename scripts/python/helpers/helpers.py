import os
import sys


# 1) Get names
module_name = os.path.basename(sys.modules[__name__].__file__).split(".")[0]
# instance.__class__.__name__
# class.__name__


# 2) Add module to sys path
directory = os.path.abspath(os.path.join(os.path.dirname(__file__)))
# directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, directory)