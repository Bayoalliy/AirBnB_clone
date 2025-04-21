import unittest
from models.city import City
from datetime import datetime
from time import sleep


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        """Check City inherits from BaseModel"""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_default_attributes(self):
        """Check default attributes of City"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_str_representation(self):
        """Check the __str__ output"""
        city = City()
        expected = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected)

    def test_to_dict_output(self):
        """Test dictionary representation from to_dict()"""
        city = City()
        city.name = "Ikeja"
        city.state_id = "state-123"
        city_dict = city.to_dict()

        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["name"], "Ikeja")
        self.assertEqual(city_dict["state_id"], "state-123")
        self.assertEqual(city_dict["id"], city.id)
        self.assertTrue(isinstance(city_dict["created_at"], str))
        self.assertTrue(isinstance(city_dict["updated_at"], str))

    def test_save_method(self):
        """Ensure updated_at changes after save()"""
        city = City()
        old_time = city.updated_at
        sleep(0.01)
        city.save()
        self.assertNotEqual(city.updated_at, old_time)
        self.assertGreater(city.updated_at, old_time)


if __name__ == "__main__":
    unittest.main()
