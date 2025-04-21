#!/usr/bin/python3

from uuid import uuid4
import datetime

class BaseModel():
    """
    defines all common attributes/methods for other classes"""
    def __init__(self):
        """declares attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """prints custom string representation"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dic = {}
        dic['__class__'] = self.__class__.__name__

        for key, val in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                val = val.isoformat()

            dic[key] = val
        return dic
