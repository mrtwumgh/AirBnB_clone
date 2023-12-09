#!/usr/bin/python3
"""
A module that tests FileStorage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    A class that tests the class FileStorage
    """

    def setUp(self):
        """
        Setup for testing
        """
        self.f = FileStorage()
        self.m = BaseModel()

    def test_all(self):
        """
        Tests the all method
        """
        self.assertIsInstance(self.f.all(), dict)

    def test_new(self):
        """
        tests the new method
        """
        self.f.new(self.m)
        key = self.m.__class__.__name__ + "." + self.m.id
        self.assertIn(key, self.f.all())

    def test_save(self):
        """
        tests the save method
        """
        self.f.save()
        with open(self.f._FileStorage__file_path, "r") as f:
            self.assertIsNotNone(f.read())

    def test_reload(self):
        """
        rests the reload method
        """
        self.f.reload()
        self.assertIsInstance(self.f.all(), dict)

    def teadDown(self):
        """
        Teardown for class FileStorage
        """
        del self.f
        del self.m


if __name__ == "__main__":
    unittest.main()
