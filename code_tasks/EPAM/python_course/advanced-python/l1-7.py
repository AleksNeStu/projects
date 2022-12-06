"""Arbitrary Argument Lists."""


__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


def join_items(separator, *items):
  return separator.join(str(i) for i in items)


# normal call with separate arguments
print range(3, 6)
print join_items(', ', 1, 2, 3, 4)


# call with arguments unpacked from a list
args = [3, 6]
print range(*args)
print join_items(',', *args)