#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Ids increase automatically when none is given."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_id_given(self):
        """A given id is used as is."""
        self.assertEqual(Base(89).id, 89)

    def test_to_json_string_none(self):
        """None and an empty list both give '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_none(self):
        """None and an empty string both give an empty list."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])


if __name__ == "__main__":
    unittest.main()
