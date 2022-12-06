"""Inheritance."""


class Ancestor:
    def __init__(self):
        print("Ancestor.__init__")

    def fun(self):
        print("Ancestor.fun")

    def __del__(self):
        print("Ancestor.__del__")


class Child(Ancestor):
    def __init__(self):
        print("Child.__init__")

    def fun(self):
        print("Child.fun")

    def __del__(self):
        print("Child.__del__")