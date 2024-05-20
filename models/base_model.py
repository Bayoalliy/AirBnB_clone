#!/usr/bin/python3
"""
This Module defines the basemodel
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """ Defines all common attributes """

    def __init__(self, *args, **kwargs):
        """ constructor function """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ customizing the __str__ method """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updating attributes """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ editing the __dict__ method"""
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        for key in dic:
            if key == 'updated_at' or key == 'created_at':
                dic[key] = dic[key].isoformat()
        return dic
