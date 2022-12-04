import os
import sys

module_name = os.path.basename(sys.modules[__name__].__file__).split(".")[0]
# instance.__class__.__name__
# class.__name__