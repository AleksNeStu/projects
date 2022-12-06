# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
bmi = weight / (height ** 2)
if bmi < 18.5:
    conclusion_part = "are underweight"
if 18.5 <= bmi < 25:
    conclusion_part = "have a normal weight"
elif 25 <= bmi < 30:
    conclusion_part = "are slightly overweight"
elif 30 <= bmi < 35:
    conclusion_part = "are slightly overweight"
else:
    conclusion_part = "are clinically obese"
print(f"Your BMI is {round(bmi)}, you {conclusion_part}.")
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests


#SOLUTI`ON
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")
#SOLUTION































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
        with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            testing_copy.test_func()
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_1(self):
        self.run_test(given_answer=['1.7', '75'], expected_print='Your BMI is 26, you are slightly overweight.\n')

    def test_2(self):
        self.run_test(given_answer=['1.5', '65'], expected_print='Your BMI is 29, you are slightly overweight.\n')

    def test_3(self):
        self.run_test(given_answer=['1.5', '51'], expected_print='Your BMI is 23, you have a normal weight.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions: \n For 1.7m and 75kg it should print this line *exactly*:\n')
print('Your BMI is 26, you are slightly overweight.')
print('\nRunning some tests on your code with different combinations for height and weight:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py')

