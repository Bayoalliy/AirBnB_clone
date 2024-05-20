#!/usr/bin/python3
""" This module tests the basemodel class """

import unittest
from models.base_model import BaseModel
from models import base_model
from datetime import datetime


class test_BaseModel(unittest.TestCase):
    """ class with methods that test basemodel"""

    model = BaseModel()

    def test_base_model_docs(self):
        """ tests module and class documentation"""

        self.assertIsNotNone(base_model.__doc__, 'No documentation detected')
        if base_model.__doc__ is not None:
            self.assertTrue(len(base_model.__doc__) >= 10)
        self.assertIsNotNone(BaseModel.__doc__, 'class has no documentation')

    def test_BaseModel_attributes(self):
        """ testing attributes of BaseModel class """

        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """ tests if __str__ output is correct """

        _str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(self.model.__str__(), _str)

    def test_save(self):
        """ tests save method """

        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict(self):
        """ testing the to_dict method """

        dic = self.model.to_dict()
        self.assertIn('__class__', dic)
        self.assertIsInstance(dic['created_at'], str)
        self.assertIsInstance(dic['updated_at'], str)


if __name__ = "main":
    unittest.main()
