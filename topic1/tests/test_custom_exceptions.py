"""
Program: test_custom_exceptions.py
Author:  Luke Xiong
Date: 7/12/2020

This program will test the exceptions in Customer class of custom_exceptions.py
"""

import unittest

def div(a,b):
   return a/b
class raiseTest(unittest.TestCase):
   def testraise(self):
      self.assertRaises(ZeroDivisionError, div, 1,0)

if __name__ == '__main__':
   unittest.main()
