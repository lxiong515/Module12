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
        self.Rider = r.Motorcycle()
        self.Rider = r.Car()

    def tearDown(self):
        del self.Rider

    def test_abstract_attributes(self):
      self.assertEqual(self.Rider.bike, 'Human powered, not enclosed' + '\n' + '1 or 2 if tandem or a daredevil')

    def test_abstract_attributes(self):
      self.assertEqual(self.Rider.motorcycle, 'Engine powered, not enclosed' +'\n'+'1 or 2')

    def test_abstract_attributes(self):
      self.assertEqual(self.Rider.car, 'Engine powered, enclosed'+'\n'+'1 plus comfortably')

if __name__ == '__main__':
    unittest.main()
