import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("SetUp")

    def tearDown(self):
        print("tearDown")

    def test_case_1(self):
        print("tear_case_1")

    def test_case_2(self):
        print("tear_case_2")

    def function(self):
        print("function")

if __name__ == '__main__':
    unittest.main()