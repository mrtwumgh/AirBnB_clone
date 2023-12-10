#!/usr/bin/python3
"""
A module that tests the class State
"""
import datetime
from models.place import Place
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
        self.p = Place()

    def test_init(self):
        """
        Tets the __init__ method
        """
        self.assertIsInstance(self.p, Place)
        self.assertIsInstance(self.p.id, str)
        self.assertIsInstance(self.p.created_at, datetime.datetime)
        self.assertIsInstance(self.p.updated_at, datetime.datetime)

        d = {
                "id": "1234",
                "created_at": "2023-12-10T09:44:39.000000",
                "updated_at": "2023-12-10T09:44:39.000000"
        }

        self.t = Place(**d)
        self.assertIsInstance(self.t, Place)
        self.assertEqual(self.t.id, "1234")
        dt = datetime.datetime(2023, 12, 10, 9, 44, 39)
        self.assertEqual(self.t.created_at, dt)
        self.assertEqual(self.t.updated_at, dt)

    def test_str(self):
        """
        Tests the __str__ method
        """
        s = "[Place] ({}) {}".format(self.p.id, self.p.__dict__)
        self.assertEqual(str(self.p), s)

    def test_save(self):
        """
        Tests the save method of State
        """
        old = self.p.updated_at
        self.p.save()
        new = self.p.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict(self):
        """
        Tests the to_dict method of State
        """
        d = self.p.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "Place")
        self.assertEqual(d["id"], self.p.id)
        self.assertEqual(d["created_at"], self.p.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.p.updated_at.isoformat())

    def tearDown(self):
        """
        Teardown for State
        """
        del self.p


if __name__ == "__main__":
    unittest.main()
