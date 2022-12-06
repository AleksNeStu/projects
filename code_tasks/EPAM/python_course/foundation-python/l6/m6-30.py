"""Generating exceptions."""

def functionName(level):
    if level < 1:
        raise Exception("Invalid level! %s" % level)
        # The code below to this would not be executed
        # if we raise the exception

# raise [Exception [, args [, traceback]]]
#
# try:
#     ...
# except Exception as e:
#     Exception handling here...
# else:
#     Rest of the code here...



# raise KeyboardInterrupt
# raise MemoryError("This is an argument")
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!: {}".format(a))
except EOFError as ve:
    print(ve)
