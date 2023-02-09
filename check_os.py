import unittest
from cal.py import *

def is_int(val):
    if type(val) == int:
        return True
    else:
       return False
 
class TestStringMethods(unittest.TestCase):
    # test function
    def test_negative(self):
        testValue = False
        # error message in case if test case got failed
        message = "Test value is not true."
        # assertTrue() to check true of test value
        self.assertTrue( testValue, message)
 
if __name__ == '__main__':
    unittest.main()
