"""Directories."""

import os

dir_name = 'dir_24'

t1 = os.mkdir(dir_name)
t2 = os.chdir(dir_name)
t3 = os.getcwd()
t4 = os.rmdir(dir_name)