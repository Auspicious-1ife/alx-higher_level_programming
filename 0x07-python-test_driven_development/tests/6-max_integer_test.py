#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, 4]), 4)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.8, 4.2]), 4.2)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)

if __name__ == '__main__':
    unittest.main()
