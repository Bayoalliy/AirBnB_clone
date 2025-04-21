import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep


class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        """Test if Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_default_attributes(self):
        """Test that name is initialized as an empty string"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        """Test __str__ method"""
        amenity = Amenity()
        expected = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected)

    def test_to_dict_output(self):
        """Test conversion to dictionary with to_dict()"""
        amenity = Amenity()
        amenity.name = "Wi-Fi"
        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["name"], "Wi-Fi")
        self.assertEqual(amenity_dict["id"], amenity.id)
        self.assertTrue(isinstance(amenity_dict["created_at"], str))
        self.assertTrue(isinstance(amenity_dict["updated_at"], str))

    def test_save_method(self):
        """Test that save() updates the updated_at timestamp"""
        amenity = Amenity()
        old_time = amenity.updated_at
        sleep(0.01)
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_time)
        self.assertGreater(amenity.updated_at, old_time)


if __name__ == "__main__":
    unittest.main()
