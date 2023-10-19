import platform
import sys

py_sys_ver = sys.version_info
sys_ver = f"{py_sys_ver.major}.{py_sys_ver.minor}.{py_sys_ver.micro}"

pl_ver = platform.python_version()

assert sys_ver == pl_ver
print("Python version:", pl_ver)