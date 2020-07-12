"""
Program: test_custom_exceptions.py
Author:  Luke Xiong
Date: 7/12/2020

This program will test the exceptions in Customer class of custom_exceptions.py
"""

import unittest
from topic1 import custom_exceptions as c

class CustomExceptTest(unittest.TestCase):

   def setUp(self):
      self.Customer = c.Customer('123', 'Johnson', 'Shawn', '123-333-7777')

   def tearDown(self):
      del self.Customer

   def test_custom_cid_attributes(self):
      self.assertEqual(self.Customer.customer_id, '123')

   def test_custom_last_name_attributes(self):
      self.assertEqual(self.Customer.last_name, 'Johnson')

   def test_custom_first_name_attributes(self):
      self.assertEqual(self.Customer.first_name, 'Shawn')

   def test_custom_phone_number_attributes(self):
      self.assertEqual(self.Customer.phone_number, '123-333-7777')

   def test_custom_invalid_attribute(self):
        s = c.Customer('123', 'Johnson', 'Shawn', '123-333-7777')
        with self.assertRaises(c.ValueError):
            s.display('ABC')


if __name__ == '__main__':
   unittest.main()
