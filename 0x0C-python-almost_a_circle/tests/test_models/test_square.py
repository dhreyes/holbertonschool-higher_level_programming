#!/usr/bin/python3
""" unittest for class Square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestBase(unittest.TestCase):
    """ tests stuff in unittest standard """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py',
                                        'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """ set up class for testing """
        self.r0 = Square(2, 4, 6, 8)
        self.r1 = Square(0, 0, 0, 0)
        self.r2 = Square(3, 4, 5, 6)
        self.r3 = Square(100, 101, 102, 103)
        self.r4 = Square(7, 8, 9, 10)

    def test_id(self):
        """ tests for valid id """
        pass

    def test_get_size(self):
        """ tests getter for size """
        pass

    def test_set_size(self):
        """ tests setter for size """
        pass

    def test_area(self):
        """ tests the area of class Square """
        pass
