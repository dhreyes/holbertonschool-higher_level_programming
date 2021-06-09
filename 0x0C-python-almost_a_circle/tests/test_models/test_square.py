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

    @classmethod
    def setUpClass(self):
        """ set up class for testing """
        Base.__nb_objects = 0
        self.s1 = Square(2, 2, 0, 0)
        self.s2 = Square(6, 8, 4, 6)
        self.s3 = Square(300, 1, 1, 200)
        self.s4 = Square(10, 5, 3, 15)

    def test_id(self):
        """ tests for valid id """
        self.assertEqual(self.s1.id, 0)
        self.assertEqual(self.s2.id, 6)
        self.assertEqual(self.s3.id, 200)
        self.assertEqual(self.s4.id, 15)

    def test_get_size(self):
        """ tests getter for size """
        self.assertEqual(self.s1.width, 2)
        self.assertEqual(self.s2.width, 6)
        self.assertEqual(self.s3.width, 300)

    def test_set_size(self):
        """ tests setter for size """
        self.assertEqual(self.s1.width, 2)
        self.assertEqual(self.s2.width, 6)
        self.assertEqual(self.s3.width, 300)
        s5 = Square(1, 1)
        with self.assertRaises(TypeError):
            s5.size = "hey"
        with self.assertRaises(TypeError):
            s5.width = 6.5
        with self.assertRaises(ValueError):
            s5.size = 0

    def test_area(self):
        """ tests the area of class Square """
        self.assertEqual(self.s1.area(), 4)
        self.assertEqual(self.s2.area(), 36)
        self.assertEqual(self.s3.area(), 90000)
