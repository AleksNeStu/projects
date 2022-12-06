"""Keyword Arguments in Dictionary."""


__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


def printargs(arg, **kwargs):
  print arg, kwargs


def test_var_args_call(arg1, arg2, arg3):
  print "arg1:", arg1
  print "arg2:", arg2
  print "arg3:", arg3


# normal call with separate arguments
test_var_args_call(1, 2, 3)
printargs('argument', rand_name=3, other_name=6)


# call with arguments unpacked from a dictionary
kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)
printargs('argument:', **kwargs)