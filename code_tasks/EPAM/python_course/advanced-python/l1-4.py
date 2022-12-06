"""Required and keywords arguments."""


__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


def hello(name, ending):
  print "Hello", name, ending

hello("Python", "!")

# # required argument missing
# hello()
#
# # non-keyword argument after a keyword argument
# hello(ending="!", "Python")
#
# # duplicate value for the same argument
# hello("Python", name="?")
#
# # unknown keyword argument
# hello(subject=123)