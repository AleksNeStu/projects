# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two_digit_number
print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits togeter
two_digit_number = first_digit + second_digit

print(two_digit_number)





















#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
    file.write('def test_func():\n')
    with open('main.py', 'r') as original:
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
        self.run_test(given_answer='52', expected_print="<class 'str'>\n7\n")

    def test_2(self):
        self.run_test(given_answer='92', expected_print="<class 'str'>\n11\n")

    def test_3(self):
        self.run_test(given_answer='10', expected_print="<class 'str'>\n1\n")


print("\n\n\n.\n.\n.")
print('Checking if the code first prints the data type on one line \n and the sum of the two numbers below on a second line...')
print('Running some tests on the code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py")

