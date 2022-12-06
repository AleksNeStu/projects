"""Diamond inheritance."""


class Ancestor:
    def __init__(self):
        print("Ancestor.__init__")

    def fun(self):
        print("Ancestor.fun")

    def __del__(self):
        print("Ancestor.__del__")


class Child1(Ancestor):

    def __init__(self):
        print("Child1.__init__")
        super().__init__()

    def fun(self):
        print("Child1.fun")
        super().fun()

    def __del__(self):
        print("Child1.__del__")
        super().__del__()

class Child2(Ancestor):

    def __init__(self):
        print("Child2.__init__")
        super().__init__()

    def fun(self):
        print("Child2.fun")
        super().fun()

    def __del__(self):
        print("Child2.__del__")
        super().__del__()

class Child3(Child1, Child2):

    def __init__(self):
        print("Child3.__init__")
        super().__init__()

    def fun(self):
        print("Child3.fun")
        super().fun()

    def __del__(self):
        print("Child3.__del__")
        super().__del__()