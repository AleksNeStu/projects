"""Different ways to execute Python code."""


__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


STR_SUM = "sum([1, 2])"

exec("print %s" % STR_SUM)

print eval(STR_SUM)

# raw_input(">>>")

import ast
s = ast.literal_eval("[1, 2]")
print sum(s)

import code, codeop
print "\n".join([help(code), help(codeop)])
