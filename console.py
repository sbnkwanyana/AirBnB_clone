#!/usr/bin/python3
"""
Console.py - contains the interactive/non-interactive shell class
that is the entry point of the console application
"""

import cmd
import shlex
from models.base_model import BaseModel
import models

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    Shell class prompts and accepts input from the a terminal and interprets
    the commands and runs the corresponding command
    """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        "End of file: Quit"
        exit()

    def do_quit(self, arg):
        "Quit command to exit the program"
        exit()

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        command = shlex.split(args)
        if len(command) == 0:
            print("** class name missing **")
            return
        else:
            if command[0] in classes:
                instance = classes[command[0]]()
            else:
                print("** class doesn't exist **")
                return
        print(instance.id)
        instance.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        command = shlex.split(args)
        if len(command) == 0:
            print("** class name missing **")
        else:
            if command[0] in classes:
                if len(command) > 1:
                    key = command[0] + "." + command[1]
                    if key in models.storage.all():
                        print(models.storage.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file
        """
        command = shlex.split(args)
        if len(command) == 0:
            print("** class name missing **")
        else:
            if command[0] in classes:
                if len(command) > 1:
                    key = command[0] + "." + command[1]
                    if key in models.storage.all():
                        models.storage.all().pop(key)
                        models.storage.save()
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        command = shlex.split(args)
        holder = []
        if len(command) == 0:
            dic = models.storage.all()
        else:
            if command[0] in classes:
                dic = models.storage.all()
            else:
                print("** class doesn't exist **")
                return

        for key in dic:
            holder.append(str(dic[key]))
        print("[", end="")
        print(", ".join(holder), end="")
        print("]")

    def update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file
        """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
