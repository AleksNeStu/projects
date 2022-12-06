#Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")



# TEST
#Copy Paste your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇
import sys
from helpers import tests

expected_out = (
    "Day 1 - Python Print Function\n"
    "The function is declared like this:\n"
    "print('what to print')\n"
)
tests.TestBasic().test_print_out(
    testing_module_name=sys.argv[0],
    count_lines_to_read=7,
    expected_data=expected_out)