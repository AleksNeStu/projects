"""Visibility: Global vs Local."""

total = 0 # Global

def sum1(arg1, arg2):
    "Add both the parameters and return them."
    total = arg1 + arg2 # Local
    print("Inside the function : {0}".format(total))
    return total

sum1(10, 20)
print("Outside the function : %s" % total)