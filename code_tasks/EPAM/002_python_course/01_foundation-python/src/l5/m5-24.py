"""issubclass."""


class A:
    pass


class B(A):
    pass


class C:
    pass


print(issubclass(B, A))
print(issubclass(A, B))
print(issubclass(A, C))
# True
# False
# False