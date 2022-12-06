"""Custom interpreters."""


__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


import code

interpretor = code.InteractiveConsole()

try:
  while(True):
    code_string = interpretor.raw_input(">>>")
    interpretor.push(code_string)
except EOFError:
  print("\nExiting\n")