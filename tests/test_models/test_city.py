#!/usr/bin/python3
"""
A module that tests the class State
"""
import datetime
from models.city import City
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
        self.c = City()

    def test_init(self):
        """
        Tets the __init__ method
        """
        self.assertIsInstance(self.c, City)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.created_at, datetime.datetime)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)

        d = {
                "id": "1234",
                "created_at": "2023-12-10T09:44:39.000000",
                "updated_at": "2023-12-10T09:44:39.000000"
        }

        self.t = City(**d)
        self.assertIsInstance(self.t, City)
        self.assertEqual(self.t.id, "1234")
        dt = datetime.datetime(2023, 12, 10, 9, 44, 39)
        self.assertEqual(self.t.created_at, dt)
        self.assertEqual(self.t.updated_at, dt)

    def test_str(self):
        """
        Tests the __str__ method
        """
        s = "[City] ({}) {}".format(self.c.id, self.c.__dict__)
        self.assertEqual(str(self.c), s)

    def test_save(self):
        """
        Tests the save method of State
        """
        old = self.c.updated_at
        self.c.save()
        new = self.c.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict(self):
        """
        Tests the to_dict method of State
        """
        d = self.c.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "City")
        self.assertEqual(d["id"], self.c.id)
        self.assertEqual(d["created_at"], self.c.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.c.updated_at.isoformat())

    def tearDown(self):
        """
        Teardown for State
        """
        del self.c


if __name__ == "__main__":
    unittest.main()
