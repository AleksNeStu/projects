"""Keyword Arguments in Dictionary."""


__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


def make_incrementor(n):
  return lambda x: x + n


f = make_incrementor(42)
help(f) # f - is a function
print f(0)
print f(1)


f = make_incrementor(0)
print f(0)
print f(1)