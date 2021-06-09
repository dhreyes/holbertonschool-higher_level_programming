#!/usr/bin/python3
""" unittest for class Base """
import unittest
from models.base import Base
import pep8


class TestBase(unittest.TestCase):
    """ tests stuff in unittest standard """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setUpClass(self):
        """ Sets up the class for testing """
        Base.__nb_objects = 0
        self.b0 = Base(0)
        self.b1 = Base(100)
        self.b2 = Base(10)
        self.b3 = Base(-13.2)
        self.b4 = Base("string")
        self.b5 = Base([1, 2, 3])
        self.b6 = Base({2: "hello", 4: "world"})
        self.b7 = Base()
        self.b8 = Base()
        self.b9 = Base()

    def test_empty_constructors(self):
        """ tests if counter in base works correctly """
        self.assertEqual(self.b7.id, 1)
        self.assertEqual(self.b8.id, 2)
        self.assertEqual(self.b9.id, 3)

    def test_ids_as_input(self):
        """ tests the input for id """
        self.assertEqual(self.b0.id, 0)
        self.assertEqual(self.b1.id, 100)
        self.assertEqual(self.b2.id, 10)
        self.assertEqual(self.b3.id, -13.2)
        self.assertEqual(self.b4.id, "string")
        self.assertEqual(self.b5.id, [1, 2, 3])
        self.assertEqual(self.b6.id, {2: "hello", 4: "world"})

    def test_to_json_string(self):
        """ testing to_json_string method """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'json': 69}, {'file': 96}]),
                         '[{"json": 69}, {"file": 96}]')
        self.assertIsInstance((Base.to_json_string([{'json': 69},
                                                   {'file': 96}])), str)

    def test_from_json_string(self):
        """ testing from_json_string method """
        self.assertEqual(Base.from_json_string(None), '[]')
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"json": 69}, {"file": 96}]'),
                         [{"json": 69}, {"file": 96}])
        self.assertIsInstance((Base.from_json_string('[{"json": 69},\
                                                   {"file": 96}]')), list)

    def tearDown(self):
        """ Always runs after each test module """
        pass
