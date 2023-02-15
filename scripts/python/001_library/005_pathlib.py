# https://docs.python.org/3/library/pathlib.html
import os
from pathlib import Path

# Get the Full Path of the Current Working Directory
d1 = os.path.abspath(os.getcwd())
d2 = os.path.dirname(os.path.abspath(__file__))

d3 = Path(__file__).resolve().parent.absolute()
d4 = Path().absolute()

assert d1 == d2 == str(d3) == str(d4)

p = d4

# Listing subdirectories:
all_dirs = [x for x in p.iterdir() if x.is_dir()]

# Listing Python source files in this directory tree:
py_files = list(p.glob('**/*.py'))