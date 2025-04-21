from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from base_model import BaseModel


class TestCommandInterpreter(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def test_prompt(self):
        self.assertEqual(self.cmd.prompt, "(hbnb) ")

    def test_quit_command_exits(self):
        with patch('sys.stdout', new=StringIO()) as f:
            result = self.cmd.onecmd("quit")
            self.assertTrue(result)  # quit returns True to exit

    def test_EOF_command_exits(self):
        with patch('sys.stdout', new=StringIO()) as f:
            result = self.cmd.onecmd("EOF")
            self.assertTrue(result)  # EOF returns True to exit

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands", output)

    def test_empty_line_does_nothing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            result = self.cmd.onecmd("")
            output = f.getvalue()
            self.assertEqual(output, "")
            self.assertFalse(result)




class TestCommandExtended(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()
        self.prompt = "(hbnb) "

    def tearDown(self):
        storage._FileStorage__objects = {}

    def run_cmd(self, command_str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.cmd.onecmd(command_str)
            return output.getvalue().strip()

    def test_create_success(self):
        output = self.run_cmd("create BaseModel")
        self.assertRegex(output, r"^[a-f0-9\-]{36}$")  # UUID

    def test_create_no_class(self):
        output = self.run_cmd("create")
        self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        output = self.run_cmd("create MyModel")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_success(self):
        obj = BaseModel()
        obj.save()
        output = self.run_cmd(f"show BaseModel {obj.id}")
        self.assertIn(obj.__class__.__name__, output)
        self.assertIn(obj.id, output)

    def test_show_missing_class(self):
        output = self.run_cmd("show")
        self.assertEqual(output, "** class name missing **")

    def test_show_invalid_class(self):
        output = self.run_cmd("show MyModel")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_id(self):
        output = self.run_cmd("show BaseModel")
        self.assertEqual(output, "** instance id missing **")

    def test_show_no_instance(self):
        output = self.run_cmd("show BaseModel 1234")
        self.assertEqual(output, "** no instance found **")

    def test_destroy_success(self):
        obj = BaseModel()
        obj.save()
        obj_key = f"BaseModel.{obj.id}"
        self.assertIn(obj_key, storage.all())
        self.run_cmd(f"destroy BaseModel {obj.id}")
        self.assertNotIn(obj_key, storage.all())

    def test_destroy_errors(self):
        self.assertEqual(self.run_cmd("destroy"), "** class name missing **")
        self.assertEqual(self.run_cmd("destroy MyModel"), "** class doesn't exist **")
        self.assertEqual(self.run_cmd("destroy BaseModel"), "** instance id missing **")
        self.assertEqual(self.run_cmd("destroy BaseModel 1234"), "** no instance found **")

    def test_all_with_class(self):
        obj = BaseModel()
        obj.save()
        output = self.run_cmd("all BaseModel")
        self.assertIn("BaseModel", output)
        self.assertIn(obj.id, output)

    def test_all_no_class(self):
        obj = BaseModel()
        obj.save()
        output = self.run_cmd("all")
        self.assertIn("BaseModel", output)

    def test_all_invalid_class(self):
        output = self.run_cmd("all MyModel")
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_success(self):
        obj = BaseModel()
        obj.save()
        self.run_cmd(f'update BaseModel {obj.id} name "TestUser"')
        updated_obj = storage.all()[f"BaseModel.{obj.id}"]
        self.assertEqual(updated_obj.name, "TestUser")

    def test_update_integer_and_float(self):
        obj = BaseModel()
        obj.save()
        self.run_cmd(f'update BaseModel {obj.id} age 25')
        self.assertEqual(getattr(obj, "age"), 25)
        self.run_cmd(f'update BaseModel {obj.id} rating 4.5')
        self.assertEqual(getattr(obj, "rating"), 4.5)

    def test_update_errors(self):
        obj = BaseModel()
        obj.save()
        existing_id = obj.id
        self.assertEqual(self.run_cmd("update"), "** class name missing **")
        self.assertEqual(self.run_cmd("update MyModel"), "** class doesn't exist **")
        self.assertEqual(self.run_cmd("update BaseModel"), "** instance id missing **")
        self.assertEqual(self.run_cmd("update BaseModel 1234"), "** no instance found **")
        self.assertEqual(self.run_cmd(f"update BaseModel {existing_id}"), "** attribute name missing **")
        self.assertEqual(self.run_cmd(f"update BaseModel {existing_id} name"), "** value missing **")
        # Should ignore extra arguments
        output = self.run_cmd(f'update BaseModel {existing_id} email "a@b.com" name "Betty"')
        self.assertNotIn("Betty", output)  # only first attr/value should be considered

if __name__ == "__main__":
    unittest.main()
