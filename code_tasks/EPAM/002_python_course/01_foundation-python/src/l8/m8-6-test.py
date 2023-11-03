import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


# 2
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

#3
# @unittest.skipIf(condition, reason)
# Skip the decorated test if condition is true.
#
# @unittest.skipUnless(condition, reason)
# Skip the decorated test unless condition is true.
#
# @unittest.expectedFailure
# Mark the test as an expected failure. If the test fails it will be considered
# a success. If the test passes, it will be considered a failure.
#
# exception unittest.SkipTest(reason)
# This exception is raised to skip a test.