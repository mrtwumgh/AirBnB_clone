#!/usr/bin/python3
"""
A module that tests the class State
"""
import datetime
from models.state import State
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
        self.s = State()

    def test_init(self):
        """
        Tets the __init__ method
        """
        self.assertIsInstance(self.s, State)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)

        d = {
                "id": "1234",
                "created_at": "2023-12-10T09:44:39.000000",
                "updated_at": "2023-12-10T09:44:39.000000"
        }

        self.t = State(**d)
        self.assertIsInstance(self.t, State)
        self.assertEqual(self.t.id, "1234")
        dt = datetime.datetime(2023, 12, 10, 9, 44, 39)
        self.assertEqual(self.t.created_at, dt)
        self.assertEqual(self.t.updated_at, dt)

    def test_str(self):
        """
        Tests the __str__ method
        """
        s = "[State] ({}) {}".format(self.s.id, self.s.__dict__)
        self.assertEqual(str(self.s), s)

    def test_save(self):
        """
        Tests the save method of State
        """
        old = self.s.updated_at
        self.s.save()
        new = self.s.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict(self):
        """
        Tests the to_dict method of State
        """
        d = self.s.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "State")
        self.assertEqual(d["id"], self.s.id)
        self.assertEqual(d["created_at"], self.s.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.s.updated_at.isoformat())

    def tearDown(self):
        """
        Teardown for State
        """
        del self.s


if __name__ == "__main__":
    unittest.main()
