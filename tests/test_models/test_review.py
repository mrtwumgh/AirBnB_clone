#!/usr/bin/python3
"""
A module that tests the class State
"""
import datetime
from models.review import Review
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
        self.r = Review()

    def test_init(self):
        """
        Tets the __init__ method
        """
        self.assertIsInstance(self.r, Review)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.created_at, datetime.datetime)
        self.assertIsInstance(self.r.updated_at, datetime.datetime)

        d = {
                "id": "1234",
                "created_at": "2023-12-10T09:44:39.000000",
                "updated_at": "2023-12-10T09:44:39.000000"
        }

        self.t = Review(**d)
        self.assertIsInstance(self.t, Review)
        self.assertEqual(self.t.id, "1234")
        dt = datetime.datetime(2023, 12, 10, 9, 44, 39)
        self.assertEqual(self.t.created_at, dt)
        self.assertEqual(self.t.updated_at, dt)

    def test_str(self):
        """
        Tests the __str__ method
        """
        s = "[Review] ({}) {}".format(self.r.id, self.r.__dict__)
        self.assertEqual(str(self.r), s)

    def test_save(self):
        """
        Tests the save method of State
        """
        old = self.r.updated_at
        self.r.save()
        new = self.r.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict(self):
        """
        Tests the to_dict method of State
        """
        d = self.r.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "Review")
        self.assertEqual(d["id"], self.r.id)
        self.assertEqual(d["created_at"], self.r.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.r.updated_at.isoformat())

    def tearDown(self):
        """
        Teardown for State
        """
        del self.r


if __name__ == "__main__":
    unittest.main()
