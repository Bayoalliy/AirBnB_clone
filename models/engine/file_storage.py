#!/usr/bin/python3
import json
""" 
This module defines FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.
"""


class FileStorage:
    """ main class that defines instances attributes """
    
    __file_path = "../file.json"
    __objects = {}

    def __init__(self):
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
        self.__file_path = json.dumps(self.__objects)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if self.__file_path:
            __objects = json.loads(self.__file_path)
