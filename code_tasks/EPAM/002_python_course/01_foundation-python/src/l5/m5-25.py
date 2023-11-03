"""Isinstance."""

class A:
    pass

a = A()
o = object()

print(isinstance(a, A))
print(isinstance(o, A))
# True
# False