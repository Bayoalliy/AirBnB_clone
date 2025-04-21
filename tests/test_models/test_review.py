import unittest
from models.review import Review
from datetime import datetime
from time import sleep


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        """Test that Review is a subclass of BaseModel"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_default_attributes(self):
        """Test that default attributes are set correctly"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_representation(self):
        """Test the __str__ method"""
        review = Review()
        expected = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), expected)

    def test_to_dict_output(self):
        """Test the dictionary returned by to_dict()"""
        review = Review()
        review.place_id = "place-001"
        review.user_id = "user-001"
        review.text = "Great location and very clean!"

        review_dict = review.to_dict()

        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "place-001")
        self.assertEqual(review_dict["user_id"], "user-001")
        self.assertEqual(review_dict["text"], "Great location and very clean!")
        self.assertTrue(isinstance(review_dict["created_at"], str))
        self.assertTrue(isinstance(review_dict["updated_at"], str))

    def test_save_method(self):
        """Test that save() updates updated_at timestamp"""
        review = Review()
        old_updated_at = review.updated_at
        sleep(0.01)
        review.save()
        self.assertNotEqual(review.updated_at, old_updated_at)
        self.assertGreater(review.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
