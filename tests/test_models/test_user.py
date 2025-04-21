import unittest
import os
import json
from io import StringIO
from unittest.mock import patch
from models import storage
from models.user import User
from console import HBNBCommand


class TestUserCommands(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand(()
        # Ensure file is clean
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage._FileStorage__objects.clear()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage._FileStorage__objects.clear()

    def test_create_user(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertIn(f"User.{user_id}", storage.all())
            self.assertTrue(len(user_id) > 0)

    def test_show_user(self):
        user = User()
        storage.new(user)
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd(f"show User {user.id}")
            output = f.getvalue().strip()
            self.assertIn(user.id, output)
            self.assertIn("User", output)

    def test_destroy_user(self):
        user = User()
        storage.new(user)
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd(f"destroy User {user.id}")
        self.assertNotIn(f"User.{user.id}", storage.all())

    def test_all_users(self):
        user1 = User()
        user2 = User()
        storage.new(user1)
        storage.new(user2)
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn(user1.id, output)
            self.assertIn(user2.id, output)

    def test_update_user(self):
        user = User()
        storage.new(user)
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd(f'update User {user.id} first_name "Alice"')
        updated_user = storage.all()[f"User.{user.id}"]
        self.assertEqual(updated_user.first_name, "Alice")

    def test_create_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create NotAClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("show NotAClass 123")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_no_instance(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("show User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")


if __name__ == '__main__':
    unittest.main()
