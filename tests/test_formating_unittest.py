import unittest

from projecteuler.mathlibrary import utilities

class format_milliseconds_test(unittest.TestCase):

    def __init__(self):
        object.__init__(self)

    def milliseconds_less_than_10(self):

        total_milliseconds = 0.006

        expected = '00:00:00.006'
        actual = utilities.format_milliseconds(total_milliseconds)

        self.assertTrue(expected == actual)
    
if __name__ == '__main__':
    unittest.main()