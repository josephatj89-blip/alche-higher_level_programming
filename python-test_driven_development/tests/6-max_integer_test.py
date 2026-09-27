#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument_uses_default(self):
        """Calling with no argument uses the default empty list."""
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """A single-element list returns that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_start(self):
        """Max value located at the start of the list."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Max value located at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_max_in_middle(self):
        """Max value located in the middle of the list."""
        self.assertEqual(max_integer([1, 9, 3]), 9)

    def test_ascending_order(self):
        """List already sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_descending_order(self):
        """List sorted in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unsorted_order(self):
        """List in an arbitrary unsorted order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_all_negative(self):
        """All negative numbers."""
        self.assertEqual(max_integer([-5, -1, -10, -3]), -1)

    def test_mixed_positive_negative(self):
        """A mix of positive and negative numbers."""
        self.assertEqual(max_integer([-5, 3, -10, 7, 0]), 7)

    def test_duplicate_max_values(self):
        """The max value appears more than once."""
        self.assertEqual(max_integer([2, 9, 5, 9, 1]), 9)

    def test_all_same_value(self):
        """Every element is identical."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_two_elements(self):
        """A two-element list."""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)

    def test_zero_included(self):
        """A list that includes zero as the max."""
        self.assertEqual(max_integer([-5, -3, 0, -1]), 0)

    def test_floats(self):
        """A list of floats also works correctly."""
        self.assertEqual(max_integer([1.5, 3.2, 2.1]), 3.2)


if __name__ == '__main__':
    unittest.main()
