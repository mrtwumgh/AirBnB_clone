#!/usr/bin/python3
"""
A module that tests the class BaseModel
"""
import datetime
from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """
    A class that test the class BaseModel
    """

    def setUp(self):
        """
        SetUp for testing
        """
        self.b = BaseModel()

    def test_init(self):
        """
        Tests the __init__ method
        """
        self.assertIsInstance(self.b, BaseModel)
        self.assertIsInstance(self.b.id, str)
        self.assertIsInstance(self.b.created_at, datetime.datetime)
        self.assertIsInstance(self.b.updated_at, datetime.datetime)

    def test_str(self):
        """
        Tests the __str__ method
        """
        s = "[BaseModel] ({}) {}".format(self.b.id, self.b.__dict__)
        self.assertEqual(str(self.b), s)


    def test_save(self):
        """
        Tests the save method of BaseModel
        """
        old = self.b.updated_at
        self.b.save()
        new = self.b.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict(self):
        """
        Tests the to_dict method of BaseModel
        """
        d = self.b.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], self.b.id)
        self.assertEqual(d["created_at"], str(self.b.created_at))
        self.assertEqual(d["updated_at"], str(self.b.updated_at))

    def tearDown(self):
        """
        Teardown for BaseModel
        """
        del self.b


if __name__ == "__main__":
    unittest.main()
