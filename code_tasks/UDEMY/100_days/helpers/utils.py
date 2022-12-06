#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Utils."""

__author__ = "AleksNeStu"
__maintainer__ = "AleksNeStu"
__copyright__ = "©AleksNeStu"
__license__ = "The GNU General Public License v3.0"
__version__ = "0.0.1"
__contact__ = "https://github.com/AleksNeStu"
__status__ = "Prototype"

import os


def testing_code_to_test_file(testing_module_name, count_lines_to_read):
    with open("temp_testing_file.py", "w") as temp_testing_file:
        temp_testing_file.write("def temp_test_func():\n")
        with open(testing_module_name, "r") as testing_module:
            for code_line in testing_module.readlines()[
                             0:count_lines_to_read]:
                temp_testing_file.write("    " + code_line)

    return temp_testing_file


def del_test_file():
    os.remove("temp_testing_file.py")