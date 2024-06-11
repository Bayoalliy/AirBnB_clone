#!/usr/bin/python3
"""
This module contains the entry point
of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Entry point """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ Quit command to exit the program """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def postloop(self):
        print

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
