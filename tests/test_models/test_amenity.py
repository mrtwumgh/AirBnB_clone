#!/usr/bin/python3
"""
A module that tests the class State
"""
import datetime
from models.amenity import Amenity
import unittest
import uuid


class TestState(unittest.TestCase):
    """
    A class that tests the class state
    """

    def setUp(self):
        """
        SetUp for testing
        """
        self.a = Amenity()

    def test_init(self):
        """
        Tets the __init__ method
        """
        self.assertIsInstance(self.a, Amenity)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

        d = {
                "id": "1234",
                "created_at": "2023-12-10T09:44:39.000000",
                "updated_at": "2023-12-10T09:44:39.000000"
        }

        self.t = Amenity(**d)
        self.assertIsInstance(self.t, Amenity)
        self.assertEqual(self.t.id, "1234")
        dt = datetime.datetime(2023, 12, 10, 9, 44, 39)
        self.assertEqual(self.t.created_at, dt)
        self.assertEqual(self.t.updated_at, dt)

    def test_str(self):
        """
        Tests the __str__ method
        """
        s = "[Amenity] ({}) {}".format(self.a.id, self.a.__dict__)
        self.assertEqual(str(self.a), s)

    def test_save(self):
        """
        Tests the save method of State
        """
        old = self.a.updated_at
        self.a.save()
        new = self.a.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict(self):
        """
        Tests the to_dict method of State
        """
        d = self.a.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "Amenity")
        self.assertEqual(d["id"], self.a.id)
        self.assertEqual(d["created_at"], self.a.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.a.updated_at.isoformat())

    def tearDown(self):
        """
        Teardown for State
        """
        del self.a


if __name__ == "__main__":
    unittest.main()
