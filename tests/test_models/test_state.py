import unittest
from models.state import State
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    def test_inheritance(self):
        """Test if State is a subclass of BaseModel"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_default_attributes(self):
        """Test default attribute values"""
        state = State()
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        """Test __str__ output"""
        state = State()
        expected = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected)

    def test_to_dict_output(self):
        """Test dictionary representation of State"""
        state = State()
        state.name = "Lagos"
        state_dict = state.to_dict()

        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "Lagos")
        self.assertEqual(state_dict["id"], state.id)
        self.assertTrue(isinstance(state_dict["created_at"], str))
        self.assertTrue(isinstance(state_dict["updated_at"], str))

    def test_save_updates_updated_at(self):
        """Test that save() updates 'updated_at'"""
        state = State()
        old_updated_at = state.updated_at
        sleep(0.01)  # Ensure time difference
        state.save()
        self.assertNotEqual(state.updated_at, old_updated_at)
        self.assertGreater(state.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
