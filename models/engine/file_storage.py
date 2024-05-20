#!/usr/bin/python3
import json
import os

"""
This module defines FileStorage that
serializes instances to a JSON file
and deserializes JSON file to instances.
"""


class FileStorage:
    """
    main class that defines instances
    attributes
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass
        """ constructor function """

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        name = obj.__class__.__name__ + '.' + obj.id
        self.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        dic = self.__objects
        for key, value in dic.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dic, f)

    def reload(self):
        """ deserializes the JSON file to __objects """

        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            dic = {}
            with open(self.__file_path, 'r') as f:
                dic = json.load(f)
            for key, value in dic.items():
                self.__objects[key] = BaseModel(**value)
