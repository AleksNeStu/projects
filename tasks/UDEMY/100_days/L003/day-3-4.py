# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
# setup cfg
size, add_pepperoni, extra_cheese = [
    var.title() for var in [size, add_pepperoni, extra_cheese]]
input_data_w_requirements = {
    # main
    'size': {
        'val': size,
        'ops': ['S', 'M', 'L'],
        'cost': {'S': 15, 'M': 20, 'L': 25},
    },
    # extra
    'add_pepperoni': {
        'val': add_pepperoni,
        'ops': ['Y', 'N'],
        'cost': {'S': 2, 'M': 3}, # 'L' is not existing
    },
    'extra_cheese': {
        'val': extra_cheese,
        'ops': ['Y', 'N'],
        'cost': {'S': 1, 'M': 1, 'L': 1},
    },
}

# error handling
violations = []
for param_var, req in input_data_w_requirements.items():
    param_val = req['val']
    param_ops = req['ops']
    if param_val not in param_ops:
        violations.append(
            f'For option "{param_var}" was provided not valid value '
            f'"{param_val}" which is not in a list "{param_ops}".')
    elif param_var == 'add_pepperoni' and param_val == 'Y' and size == 'L':
        violations.append(
            f'The option "{param_var}" is not existing for size "{size}".')

# calculation
if violations:
    raise Exception(f'Some violation are appeared: "{violations}".')
else:
    pizza_cost = input_data_w_requirements['size']['cost'][size]
    for extra_param_var in ['add_pepperoni', 'extra_cheese']:
        extra_param_req = input_data_w_requirements[extra_param_var]
        if extra_param_req['val'] == 'Y':
            pizza_cost += extra_param_req['cost'][size]
    print(f'Your final bill is: ${pizza_cost}.')

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#SOLUTION
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")
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
        self.run_test(given_answer=['S', 'N', 'Y'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $16.\n')

    def test_2(self):
        self.run_test(given_answer=['L', 'N', 'N'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $25.\n')

    def test_3(self):
        self.run_test(given_answer=['M', 'Y', 'N'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $23.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor a small pepperoni pizza with extra cheese your program should print this line *exactly*:\n')
print('Your final bill is: $18.\n')
print('\nRunning some tests on your code with different pizza combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py')
