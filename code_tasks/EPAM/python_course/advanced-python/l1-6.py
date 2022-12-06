"""Required and keywords arguments."""


__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


i = 5
def f(arg=i):
  print arg
i = 6
f()


def f(a, L=[]):
  L.append(a)
  return L


print f(1)
print f(2)
print f(3)
