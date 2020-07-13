"""
Program: test_custom_exceptions.py
Author:  Luke Xiong
Date: 7/12/2020

This program will test the exceptions in Customer class of custom_exceptions.py
"""

import unittest
from topic1 import Rider as r
from topic1.Rider import InvalidSideError


class AbstractMethodTest(unittest.TestCase):

    def setUp(self):
        self.Rider = r.Bicycle()

    def tearDown(self):
        del self.Rider

    def test_abstract_attributes(self):
      self.assertEqual(self.Rider.bike, 'Human powered, not enclosed' + '\n' + '1 or 2 if tandem or a daredevil')
    #def test_constructor(self):
        #with self.assertRaises(InvalidSideError):
            #s = r.Motorcycle(5)
        #with self.assertRaises(InvalidSideError):
            #s = r.Car(-5)

if __name__ == '__main__':
    unittest.main()
