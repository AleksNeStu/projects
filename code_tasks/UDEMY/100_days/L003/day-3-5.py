# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
merged_name = (name1 + name2).upper()
firs_d = sum([merged_name.count(l_f) for l_f in 'TRUE'])
second_d = sum([merged_name.count(l_f) for l_f in 'LOVE'])
love_score = int(f'{firs_d}{second_d}')
if love_score < 10 or love_score > 90:
  msg = f'Your score is {love_score}, you go together like coke and mentos.'
elif 40 <= love_score <= 50:
  msg = f'Your score is {love_score}, you are alright together.'
else:
  msg = f'Your score is {love_score}.'
print(msg)
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#SOLUTION
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
#SOLUTION





















































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
    file.write('def test_func():\n')
    with open('main.py', 'r') as original:
        f2 = original.readlines()[0:60]
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
        self.run_test(given_answer=['David Beckham', 'Victoria Beckham'], expected_print='Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n')

    def test_2(self):
        self.run_test(given_answer=['Han Solo', 'Princess Leia Organa'], expected_print='Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n')

    def test_3(self):
        self.run_test(given_answer=['Pierre Curie', 'Marie Curie'], expected_print='Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n')

    def test_4(self):
        self.run_test(given_answer=['Mark Antony', 'Cleopatra'], expected_print='Welcome to the Love Calculator!\nYour score is 54.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n')
print('Your score is 43, you are alright together.\n')
print('\nRunning some tests on your code with different name combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py')
