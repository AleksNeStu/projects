# """Exceptions."""
#
#
# # try:
# #     #You do your operations here;
# #     ......................
# # except ExceptionI:
# # #If there is ExceptionI, then execute this block.
# # except ExceptionII:
# #     #If there is ExceptionII, then execute this block.
# #     ......................
# # else:
# # #If there is no exception then execute this block.
# # finally:
# # #This would always be executed.
#
#
# # #else
# # try:
# #     x = x + 3 # x = x + 3 or x = 3 + 3
# # except:
# #     x = 4 + 4
# # else:
# #     x += 1
# # finally:
# #     print("do something else with x which equals: {}".format(x))
# #     y = x
#
#
#
# # import module sys to get the type of exception
# import sys
#
# randomList = ['a', 0, 2]
#
# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops!",sys.exc_info()[0],"occured.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", entry, "is", r)
#

# Catching Specific Exceptions
try:
    # do something
    pass
except ValueError:
    # handle ValueError exception
    pass
except (TypeError, ZeroDivisionError):
    # handle multiple exceptions
    # TypeError and ZeroDivisionError
    pass
except:
    # handle all other exceptions
    pass
finally:
    pass