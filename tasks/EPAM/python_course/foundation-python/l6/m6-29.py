"""Exception arguments."""

#!/usr/bin/python
# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as e:
        print ("The argument does not contain numbers\n", e.args)

temp_convert("xyz")