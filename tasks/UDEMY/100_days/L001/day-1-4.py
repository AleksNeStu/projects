# 🚨 Don't change the code below 👇
import copy

a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
# https://www.programiz.com/python-programming/examples/swap-variables
# a, b = b, a
temp = a
a = b
b = temp

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)




















# Testing code

with open("testing_copy.py", "w") as file:
    file.write("def test_func():\n")
    with open("day-1-4.py", "r") as original:
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
        with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            testing_copy.test_func()
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_1(self):
        self.run_test(given_answer=['5', 'Y'], expected_print='a: Y\nb: 5\n')

    def test_2(self):
        self.run_test(given_answer=['97', '20'], expected_print='a: 20\nb: 97\n')

    def test_3(self):
        self.run_test(given_answer=['Python', 'Monty'], expected_print='a: Monty\nb: Python\n')

print("\n\n\n.\n.\n.")
print('Checking if you have printed the swapped values...')
print('Running some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py")
