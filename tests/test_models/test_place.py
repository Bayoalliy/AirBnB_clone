import unittest
from models.place import Place
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        """Test that Place inherits from BaseModel"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_default_attributes(self):
        """Test default values of attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str_representation(self):
        """Test __str__ output format"""
        place = Place()
        expected = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), expected)

    def test_to_dict_output(self):
        """Test the dictionary returned by to_dict()"""
        place = Place()
        place.name = "Lake House"
        place.city_id = "city-001"
        place.user_id = "user-001"
        place.number_rooms = 4
        place.latitude = 6.5244
        place.longitude = 3.3792
        place.amenity_ids = ["amenity-1", "amenity-2"]

        place_dict = place.to_dict()

        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["name"], "Lake House")
        self.assertEqual(place_dict["city_id"], "city-001")
        self.assertEqual(place_dict["user_id"], "user-001")
        self.assertEqual(place_dict["number_rooms"], 4)
        self.assertEqual(place_dict["latitude"], 6.5244)
        self.assertEqual(place_dict["longitude"], 3.3792)
        self.assertEqual(place_dict["amenity_ids"], ["amenity-1", "amenity-2"])
        self.assertTrue(isinstance(place_dict["created_at"], str))
        self.assertTrue(isinstance(place_dict["updated_at"], str))

    def test_save_method(self):
        """Test that updated_at is changed after save()"""
        place = Place()
        old_time = place.updated_at
        sleep(0.01)
        place.save()
        self.assertNotEqual(place.updated_at, old_time)
        self.assertGreater(place.updated_at, old_time)


if __name__ == "__main__":
    unittest.main()
