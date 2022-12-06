#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
data_to_print = [
    "Day 1 - String Manipulation",
    "String Concatenation is done with the \"+\" sign.",
    "e.g. print(\"Hello \" + \"world\")",
    "New lines can be created with a backslash and n.",
]
for line in data_to_print:
    print(line)



# TEST
#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇
import sys
from helpers import tests

expected_out = (
    'Day 1 - String Manipulation\nString Concatenation is done with the "+" '
    'sign.\ne.g. print("Hello " + "world")\nNew lines can be created with a '
    'backslash and n.\n'
)
tests.TestBasic().test_print_out(
    testing_module_name=sys.argv[0],
    count_lines_to_read=11,
    expected_data=expected_out)


