#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
















# Tests
import unittest
from unittest.mock import patch
from io import StringIO

class MyTest(unittest.TestCase):
    # Testing Print output
    def test_1(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            prime_checker(87)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_2(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            prime_checker(97)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_3(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            prime_checker(66)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_4(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            prime_checker(47)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)


print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)