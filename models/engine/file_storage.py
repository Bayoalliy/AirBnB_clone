#!/usr/bin/python3
"""
serialization of dictionary representation of our objects
"""
import os
import json


class FileStorage():
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        new_obj = {}
        for key, val in self.__objects.items():
            new_obj[key] = val.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new_obj, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity

        classes = {
                'BaseModel': BaseModel, 'User': User,
                'Place': Place, 'Amenity': Amenity,
                'City': City, 'State': State
                }
        tmp_obj = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                tmp_obj = json.load(f)
            for key, val in tmp_obj.items():
                cls_name = val['__class__']
                self.__objects[key] = classes[cls_name](**val)
