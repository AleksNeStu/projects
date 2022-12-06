#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
#This code prints the number of characters in a user's name.
print(
    len(input("What is your name? "))
)



# TEST
#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
    file.write('def test_func():\n')
    with open('day-1-3.py', 'r') as original:
        f2 = original.readlines()[0:7]
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
        self.run_test(given_answer='Jack', expected_print='4\n')

    def test_2(self):
        self.run_test(given_answer='Philipp', expected_print='7\n')

    def test_3(self):
        self.run_test(given_answer='Ernest Hemingway', expected_print='16\n')

print("\n\n\n.\n.\n.")
print('Checking if your code works with several names...')
print('Running some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py")


