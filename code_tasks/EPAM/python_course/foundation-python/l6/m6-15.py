"""stdin (input)"""

# input([prompt])
_raw_input = input("Enter your raw input: ")  # raw Python3
print("Received raw input is : ", _raw_input)

_input = eval(input("Enter your input: "))
print("Received input is : ", _input)

print('done')



