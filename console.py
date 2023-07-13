#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program at EOF (Ctrl+D).
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()