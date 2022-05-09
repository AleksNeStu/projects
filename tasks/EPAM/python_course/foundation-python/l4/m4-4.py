# """Visibility: Global vs Local."""
#
# total = 0 # Global
#
# def sum1(arg1, arg2):
#     "Add both the parameters and return them."
#     total = arg1 + arg2 # Local
#     print("Inside the function : {0}".format(total))
#     return total
#
# sum1(10, 20)
# print("Outside the function : %s" % total)


# x = "global"
#
# def foo():
#     print("x inside :", x)
#
# foo()
# print("x outside:", x)
x = 12

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
