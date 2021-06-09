#!/usr/bin/python3
""" unittest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8


class TestBase(unittest.TestCase):
    """ tests stuff in unittest standard """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py',
                                        'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setUpClass(self):
        """ set up class for testing """
        Base._Base__nb_objects = 0
        self.r0 = Rectangle(1, 2)
        self.r1 = Rectangle(5, 5, 5, 5)
        self.r2 = Rectangle(3, 4, 5, 6)
        self.r3 = Rectangle(100, 101, 102, 103, 104)
        self.r4 = Rectangle(7, 8, 9)

    def test_id(self):
        """ test id values """
        self.assertEqual(self.r0.id, 1)
        self.assertEqual(self.r1.id, 2)
        self.assertEqual(self.r2.id, 3)
        self.assertEqual(self.r3.id, 104)
        self.assertEqual(self.r4.id, 4)

    def test_get_width(self):
        """ test getter for width """
        self.assertEqual(self.r0.width, 1)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r3.width, 100)
        self.assertEqual(self.r4.width, 7)

    def test_get_height(self):
        """ test getter for height """
        self.assertEqual(self.r0.height, 2)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r2.height, 4)
        self.assertEqual(self.r3.height, 101)
        self.assertEqual(self.r4.height, 8)

    def test_get_x(self):
        """ test getter for x """
        self.assertEqual(self.r1.x, 5)
        self.assertEqual(self.r2.x, 5)
        self.assertEqual(self.r3.x, 102)
        self.assertEqual(self.r4.x, 9)

    def test_get_y(self):
        """ test getter for y """
        self.assertEqual(self.r1.y, 5)
        self.assertEqual(self.r2.y, 6)
        self.assertEqual(self.r3.y, 103)

    def test_set_width(self):
        """ test setter for width """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            newrect = Rectangle("string", 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            newrect = Rectangle(10.5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            newrect = Rectangle(-5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            newrect = Rectangle(-1, 5)

    def test_set_height(self):
        """ test setter for height """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            newrect = Rectangle(5, "string")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            newrect = Rectangle(5, 10.5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            newrect = Rectangle(5, -5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            newrect = Rectangle(1, -1)

    def test_set_x_and_y(self):
        """ test setter for x """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            newrect = Rectangle(5, 5, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            newrect = Rectangle(5, 5, 10, -5)

    def test_area(self):
        """ test area method for rectangle """
        self.assertEqual(self.r0.area(), 2)
        self.assertEqual(self.r1.area(), 25)
        self.assertEqual(self.r2.area(), 12)
