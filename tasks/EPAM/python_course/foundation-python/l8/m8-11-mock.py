from mock import MagicMock

class A:
    def method(self, a, b, c, key):
        return 666

thing = A()
thing.method = MagicMock(return_value=13)
print(thing.method(3, 4, 5, key='value'))  # returns 13

thing.method.assert_called_with(3, 4, 5, key='value')

#2
from mock import patch
@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    assert MockClass1 is not MockClass2

#3
from nose.tools import assert_equal
from parameterized import parameterized

import unittest
import math

@parameterized([
    (2, 2, 4),
    (2, 3, 8),
    (1, 9, 1),
    (0, 9, 0),
])
def test_pow(base, exponent, expected):
   assert_equal(math.pow(base, exponent), expected)

class TestMathUnitTest(unittest.TestCase):
   @parameterized.expand([
       ("negative", -1.5, -2.0),
       ("integer", 1, 1.0),
       ("large fraction", 1.6, 1),
   ])
   def test_floor(self, name, input, expected):
       assert_equal(math.floor(input), expected)