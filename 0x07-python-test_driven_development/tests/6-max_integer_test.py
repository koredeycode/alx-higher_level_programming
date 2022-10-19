#!/usr/bin/python3
"""Unitest for max-integer([...])
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Contains all the test method for max_int function
    """
    def test_unordered_list(self):
        """Test an unordered list
        """
        self.assertEqual(max_int([2, 1, 6, 0, 8, 9]), 9)

    def test_ordered_list(self):
        """Test an ordered list
        """
        self.assertEqual(max_int([2, 4, 6, 7, 8, 9]), 9)

    def test_max_at_beginning(self):
        """Test a list which max is at the beginning
        """
        self.assertEqual(max_int([20, 1, 6, 0, 8, 9]), 9)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_int([]), None)

    def test_equal_list(self):
        """Test a list with it values all equal"""
        self.assertAlmostEqual(max_int([4, 4, 4, 4]), 4)

    def test_one_element_list(self):
        """Test a list only one element"""
        self.assertAlmostEqual(max_int([4]), 4)

    def test_float_list(self):
        """Test a list with it values are floats"""
        self.assertAlmostEqual(max_int([9.45, 7.65, 67.5]), 67.5)

    def test_int_float_list(self):
        """Test a list with it valuses floats and ints"""
        self.assertAlmostEqual(max_int([9.45, 7, 68.89, 67]), 68.89)

    def test_string(self):
        """Test a string"""
        self.assertAlmostEqual(max_int("Engineering"), "r")

    def test_string_list(self):
        """Test a list of string"""
        self.assertAlmostEqual(max_int(["Kore", "is", "my", "name"]),"name")
    def test_empty_string(self):
        """Test an empty string."""
        self.assertAlmostEqual(max_int(""), None)

if __name__ == "__main__":
    unittest.main()
