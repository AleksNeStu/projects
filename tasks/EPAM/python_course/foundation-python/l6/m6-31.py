"""Usage of exceptions."""

class Networkerror(RuntimeError):
    def __init__(self, message):
        self.message = message

try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print(e.message)


