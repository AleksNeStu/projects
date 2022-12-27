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


# 3) lists of lists to list
import itertools
list2d = [[1,2,3], [4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d))


list2d2 = [[1,2,3], [4,5,6], [7], [8,9]]
merged2 = list(itertools.chain.from_iterable(list2d2))