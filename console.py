#!/usr/bin/python3
"""
Write a program called console.py that contains the
entry point of the command interpreter:

You must use the module cmd

Your class definition must be: class HBNBCommand(cmd.Cmd):


Your command interpreter should implement

quit and EOF to exit the program

help (this action is provided by default by cmd but
you should keep it updated and documented as you work through tasks)

a custom prompt: (hbnb)

an empty line + ENTER shouldn’t execute anything

Your code should not be executed when imported
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter:"""
    prompt = '(hbnb) '

    classes = {
                'BaseModel': BaseModel, 'User': User,
                'Place': Place, 'Amenity': Amenity,
                'City': City, 'State': State, 'Review': Review
                }

    def precmd(self, line):
        """parsing command line arguments"""
        if line.endswith(')'):
            real_line = []
            args = line.split('(')
            cmd_cls_name = args[0].split('.')
            real_line.append(cmd_cls_name[1])
            real_line.append(cmd_cls_name[0])
            arg_1 = args[1].strip(')')
            if arg_1.endswith('}'):
                real_line.append(arg_1.split(',')[0])
                for i in arg_1.split('{')[1].strip('}').split(','):
                    name = ' ' + i.split(':')[0].strip('"').strip("'")
                    value = i.split(':')[1].strip('"').strip("'")
                    print(' '.join(real_line) + name + value)
                    self.onecmd(' '.join(real_line) + name +  value)
                return ' '
            else:
                real_line.append(' '.join(arg_1.split(', ')))
                return ' '.join(real_line)
        return line

    def do_count(self, arg):
        """prints the number of instances of a class"""
        print(len([i for i in storage.all().keys() if i.startswith(arg)]))

    def do_create(self, arg):
        """command to create an object"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            new_obj = self.classes[arg]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id"""

        line = line.split()
        if len(line) > 1:
            key = line[0] + '.' + line[1]
        if not line:
            print("** class name missing **")

        elif line[0] not in self.classes.keys():
            print("** class doesn't exist **")

        elif len(line) < 2:
            print("** instance id missing **")

        elif key not in storage.all().keys():
            print("** no instance found **")

        else:
            for k, v in storage.all().items():
                if k == key:
                    print(v)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            key = args[0] + '.' + args[1]
            dic = storage.all()
            for k in dic.keys():
                if k == key:
                    del dic[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_update(self, line):
        """
        Updates an instance based on the class-name
        and id by adding or updating attribute
        (save the change into the JSON file)."""
        args = line.split()
        if len(args) > 1:
            key = args[0] + '.' + args[1].strip('"')

        if not args:
            print("** class name missing **")

        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif key not in storage.all().keys():
            print("** no instance found **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            key = args[0] + '.' + args[1].strip('"')
            obj = storage.all()[key]
            args[3] = args[3].strip('"')
            try:
                args[3] = int(args[3])
            except ValueError:
                try:
                    args[3] = float(args[3])
                except ValueError:
                    pass

            setattr(obj, args[2].strip('"'), args[3])

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name."""
        if arg:
            if arg in self.classes.keys():
                for val in storage.all().values():
                    if val.to_dict()['__class__'] == arg:
                        print(val)
            else:
                print("** class doesn't exist **")

        else:
            for val in storage.all().values():
                print(val.to_dict())

    def do_quit(self, arg):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the command interpreter """
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
