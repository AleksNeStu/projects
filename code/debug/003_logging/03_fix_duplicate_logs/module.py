import logger


class A:
    def __init__(self):
        self.logger = logger
        self.logger.warning('This is from class A')


class B:
    def __init__(self):
        self.logger = logger
        self.logger.warning('This is from class B')


class C:
    def __init__(self):
        self.logger = logger
        self.logger.warning('This is from class C')


def main():
    a = A()
    b = B()
    c = C()


if __name__ == '__main__':
    main()