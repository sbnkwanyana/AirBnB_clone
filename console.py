#!/usr/bin/python3
"""
Console.py - contains the interactive/non-interactive shell class
that is the entry point of the console application
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Shell class prompts and accepts input from the a terminal and interprets
    the commands and runs the corresponding command
    """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        "End of file and quits"
        exit()

    def do_quit(self, arg):
        "Quits program"
        exit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
