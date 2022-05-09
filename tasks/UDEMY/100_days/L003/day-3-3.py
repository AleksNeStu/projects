# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
is_year_divisible_by = lambda d: (year % d == 0)
is_leap_year = (
    is_year_divisible_by(4) and
    (not is_year_divisible_by(100) or
     (is_year_divisible_by(100) and is_year_divisible_by(400)))
)
print("Leap year." if is_leap_year else "Not leap year.")
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#SOLUTION
#Refer to the flow chart here: https://bit.ly/36BjS2D
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
#SOLUTION







































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
    file.write('def test_func():\n')
    with open('day-3-3.py', 'r') as original:
        f2 = original.readlines()[0:40]
        for x in f2:
            file.write("    " + x)

import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
    def run_test(self, given_answer, expected_print):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            testing_copy.test_func()
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_1(self):
        self.run_test(given_answer='2016', expected_print='Leap year.\n')

    def test_2(self):
        self.run_test(given_answer='2018', expected_print='Not leap year.\n')

    def test_3(self):
        self.run_test(given_answer='1999', expected_print='Not leap year.\n')

    def test_4(self):
        self.run_test(given_answer='2020', expected_print='Leap year.\n')

    def test_5(self):
        self.run_test(given_answer='2000', expected_print='Leap year.\n')

    def test_6(self):
        self.run_test(given_answer='1900', expected_print='Not leap year.\n')


print("\n\n\n.\n.\n.")
print('Checking what your code prints for several different years.\nYour code needs to either print "Leap year." or "Not leap year." *exactly* (that includes the full stop).\n')
print('\nRunning some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py")

