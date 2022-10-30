#!/usr/bin/python3
"""
Console.py - 
"""

import cmd
import shlex

class Shell(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        "End of file: Exit"
        exit()
    
    def do_quit(self, arg):
        'Quit program'
        exit()

if __name__ == "__main__":
    Shell().cmdloop()