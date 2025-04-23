import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up a fresh storage and test file."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        # Override the private attribute for testing purposes
        self.storage._FileStorage__file_path = self.file_path
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the JSON file after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_has_private_attributes(self):
        """Test that FileStorage has private attributes __file_path and __objects"""
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))

    def test_file_path_is_string(self):
        """Test that __file_path is a string"""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects_is_dict(self):
        """Test that __objects is a dictionary"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_new_adds_object(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_creates_file_and_serializes(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key]['id'], obj.id)

    def test_reload_loads_objects(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Create new storage instance to test reload
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, new_storage.all())
        self.assertIsInstance(new_storage.all()[key], BaseModel)
        self.assertEqual(new_storage.all()[key].id, obj.id)

    def test_reload_no_file(self):
        # No file exists
        self.assertFalse(os.path.exists(self.file_path))
        try:
            self.storage.reload()
        except Exception as e:
            self.fail(f"reload() raised an exception unexpectedly: {e}")

if __name__ == "__main__":
    unittest.main()
