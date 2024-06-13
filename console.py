#!/usr/bin/python3
"""
This module contains the entry point
of the command interpreter
"""

from models import storage
from models.base_model import BaseModel
import cmd
import shlex


class HBNBCommand(cmd.Cmd):
    """ Entry point """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        pass

    def do_create(self, cls_name):
        if cls_name is None:
            print("** class name missing **")

        elif cls_name != "BaseModel":
            print("** class doesn't exist **")

        else:
            new_class = BaseModel()
            new_class.save()
            print(new_class.id)

    def do_show(self, args):
        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] != "BaseModel":
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            classes = storage.all()
            key = args[0] + '.' + args[1]

            for k, v in classes.items():
                if k == key:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] != "BaseModel":
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            classes = storage.all()
            key = args[0] + '.' + args[1]

            for k in classes.keys():
                if k == key:
                    del classes[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, cls_name):
        all_objs = storage.all()
        objs_lst = []
        if not cls_name:
            for obj_id in all_objs.keys():
                objs_lst.append(str(all_objs[obj_id]))
            print(objs_lst)

        else:
            if cls_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                for obj_id in all_objs.keys():
                    if all_objs[obj_id].__class__.__name__ == cls_name:
                        objs_lst.append(str(all_objs[obj_id]))
                    print(objs_lst)

    def do_update(self, args):
        args = shlex.split(args)
        if args is None:
            print("** class name missing **")

        elif args[0] != "BaseModel":
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            classes = storage.all()
            key = args[0] + '.' + args[1]

            for k, v in classes.items():
                if k == key:
                    try:
                        args[3] = int(args[3])
                    except ValueError:
                        try:
                            args[3] = float(args[3])
                        except ValueError:
                            pass
                    setattr(v, args[2], args[3])
                    v.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
