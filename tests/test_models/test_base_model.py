#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string_uuid(self):
        self.assertIsInstance(self.model.id, str)
        # Check if the UUID is valid
        try:
            uuid_obj = uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID4 string")

    def test_created_at_and_updated_at_are_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_returns_correct_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

class TestBaseModelKwargs(unittest.TestCase):
    def setUp(self):
        self.base_dict = {
            'id': '1234-5678-9012',
            'created_at': '2023-01-01T12:00:00.000001',
            'updated_at': '2023-01-02T12:00:00.000002',
            'name': 'TestModel',
            '__class__': 'BaseModel'
        }
        self.model = BaseModel(**self.base_dict)

    def test_attributes_from_kwargs(self):
        self.assertEqual(self.model.id, self.base_dict['id'])
        self.assertEqual(self.model.name, self.base_dict['name'])

    def test_created_at_and_updated_at_parsing(self):
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(
            self.model.created_at.isoformat(), self.base_dict['created_at']
        )
        self.assertEqual(
            self.model.updated_at.isoformat(), self.base_dict['updated_at']
        )

    def test_class_key_not_added(self):
        self.assertFalse(hasattr(self.model, '__class__') and isinstance(getattr(self.model, '__class__'), str))

    def test_default_creation_without_kwargs(self):
        new_model = BaseModel()
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
