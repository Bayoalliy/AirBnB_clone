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


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter:"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
