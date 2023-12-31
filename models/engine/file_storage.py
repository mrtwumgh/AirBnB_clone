#!/usr/bin/python3
"""
A module that serializes instances to JSON
and deserializes JSON to instances
"""
import json


class FileStorage:
    """
    A class that serializes instances to JSON
    and deserializes JSON to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        from models.base_model import BaseModel
        dict_objects = {}
        for key, value in self.__objects.items():
            dict_objects[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(dict_objects, f)

    def reload(self):
        """
        deserializes JSON File to __objects
        """
        from datetime import datetime
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        t_f = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            with open(self.__file_path, "r") as f:
                dict_objects = json.load(f)
                for key, value in dict_objects.items():
                    if key.split(".")[0] == "User":
                        self.__objects[key] = User(**value)
                    elif key.split(".")[0] == "State":
                        self.__objects[key] = State(**value)
                    elif key.split(".")[0] == "City":
                        self.__objects[key] = City(**value)
                    elif key.split(".")[0] == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif key.split(".")[0] == "Place":
                        self.__objects[key] = Place(**value)
                    elif key.split(".")[0] == "Review":
                        self.__objects[key] = Review(**value)
                    else:
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
