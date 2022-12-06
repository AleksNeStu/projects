import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆
chosen_name = names[random.randint(0, len(names) - 1)]
print(f'{chosen_name} is going to buy the meal today!')
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests



#SOLUTION
# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]
#
# print(person_who_will_pay + " is going to buy the meal today!")
#SOLUTION



































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
    file.write('def test_func():\n')
    with open('main.py', 'r') as original:
        f2 = original.readlines()[0:45]
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
        self.run_test(given_answer=['651651', "['Victoria Beckham', 'Cleopatra', 'Marie Curie', 'Princess Leia']"], expected_print="'Marie Curie' is going to buy the meal today!\n")

    def test_2(self):
        self.run_test(given_answer=['561', "['Victoria Beckham', 'Cleopatra', 'Marie Curie', 'Princess Leia']"], expected_print="'Cleopatra' is going to buy the meal today!\n")

    def test_3(self):
        self.run_test(given_answer=['561', "['Mario', 'Luigi', 'Bowser', 'Boo']"], expected_print="'Luigi' is going to buy the meal today!\n")


print('\n\n\n.\n.\n.')
print('Checking if your print statement matches the instructions. \nFor seed number 123 and the names - Loki, Lando, Leia, Luke, Luigi - your program should print this line *exactly*:\n')
print('Loki is going to buy the meal today!\n')
print('\nRunning some tests on your code with different name and seed combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py')


