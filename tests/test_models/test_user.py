#!/usr/bin/python3
"""
A modue that tests the class User
"""
import datetime
from models.user import User
import unittest
import uuid


class TestUser(unittest.TestCase):
    """
    A class that test the class User
    """

    def setUp(self):
        """
        Setup for testing
        """
        self.u = User()

    def test_init(self):
        """
        tests the __init__ method
        """
        self.assertIsInstance(self.u, User)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.created_at, datetime.datetime)
        self.assertIsInstance(self.u.updated_at, datetime.datetime)

        d = {
                "id": "1234",
                "created_at": "2023-12-10T05:57:39.000000",
                "updated_at": "2023-12-10T05:57:39.000000"
        }
        self.c = User(**d)
        self.assertIsInstance(self.c, User)
        self.assertEqual(self.c.id, "1234")
        dt = datetime.datetime(2023, 12, 10, 5, 57, 39)
        self.assertEqual(self.c.created_at, dt)
        self.assertEqual(self.c.updated_at, dt)

    def test_str(self):
        """
        Tests the __str__ method
        """
        s = "[User] ({}) {}".format(self.u.id, self.u.__dict__)
        self.assertEqual(str(self.u), s)

    def test_save(self):
        """
        Tests the save method of User
        """
        old = self.u.updated_at
        self.u.save()
        new = self.u.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict(self):
        """
        Tests the to_dict method of User
        """
        d = self.u.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "User")
        self.assertEqual(d["id"], self.u.id)
        self.assertEqual(d["created_at"], self.u.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.u.updated_at.isoformat())

    def tearDown(self):
        """
        Teardown for User
        """
        del self.u


if __name__ == "__main__":
    unittest.main()
