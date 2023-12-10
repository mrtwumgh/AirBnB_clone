#!/usr/bin/python3
"""
A module for the class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class that inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __str__(self):
        """
        returns the string representation of Place
        """
        s = "[Place] ({}) {}".format(self.id, self.__dict__)
        return s

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = __class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
