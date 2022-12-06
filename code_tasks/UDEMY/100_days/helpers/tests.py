#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests."""

__author__ = "AleksNeStu"
__maintainer__ = "AleksNeStu"
__copyright__ = "©AleksNeStu"
__license__ = "The GNU General Public License v3.0"
__version__ = "0.0.1"
__contact__ = "https://github.com/AleksNeStu"
__status__ = "Prototype"

import inspect
import io
import unittest
from unittest import mock

from helpers import utils


class TestBasic(unittest.TestCase):

    def test_print_out(self, testing_module_name, count_lines_to_read,
                       expected_data):
        func_name = inspect.stack()[0][3]
        print("Unit test '{}' is started.".format(func_name))

        with mock.patch('sys.stdout', new=io.StringIO()) as actual_out:
            temp_testing_file = utils.testing_code_to_test_file(
                testing_module_name, count_lines_to_read)

            temp_testing_file_name = temp_testing_file.name.replace(
                '.py', '')
            __import__(temp_testing_file_name).temp_test_func()

            self.assertEquals(expected_data, actual_out.getvalue())

            utils.del_test_file()

        print("Unit test '{}' is finished.".format(func_name))