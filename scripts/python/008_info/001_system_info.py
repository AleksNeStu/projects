import platform
import sys


#1) Python version
py_sys_ver = sys.version_info
sys_ver = f"{py_sys_ver.major}.{py_sys_ver.minor}.{py_sys_ver.micro}"

pl_ver = platform.python_version()

assert sys_ver == pl_ver
print("Python version:", pl_ver)


#2) Package version
# Deprecated

# import pkg_resources
# ver1 = pkg_resources.get_distribution("anyio").version


# Actual
from importlib.metadata import version
pac_name = "anyio"
ver2 = version(pac_name)

print(f"{pac_name} version:", ver2)