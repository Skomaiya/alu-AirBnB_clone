#!/usr/bin/python
"""
Airbnb Console: A simple console-based Airbnb clone.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class: A class for the command-line interface.
    """

    prompt = "(hbnb)"

    def emptyline(self):
        """
        Override the emptyline method to do nothing on an empty line.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self, arg):
        """
        Display help information for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print()
        return True


if __name__ == '__main__':
    # Instantiate HBNBCommand and start the command loop
    HBNBCommand().cmdloop()

