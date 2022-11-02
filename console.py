#!/usr/bin/python3
"""
Console.py - contains the interactive/non-interactive shell class
that is the entry point of the console application
"""

import cmd
import shlex
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel
from models.amenity import Amenity
import models
from models.user import User

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity
    }


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

    def emptyline(self):
        """
        Empty line executes nothing
        """
        return False

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
                dic = models.storage.all(classes[command[0]])
            else:
                print("** class doesn't exist **")
                return

        for key in dic:
            holder.append(str(dic[key]))
        print("[", end="")
        print(", ".join(holder), end="")
        print("]")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file
        """
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except ValueError:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except ValueError:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """ advanced arguments"""
        cmds = ["all", "count", "destroy", "show", "update"]
        n_list = arg.split('.')
        if len(n_list) > 1:
            try:
                instance = n_list[0]
                command = n_list[1].split('(')[0]
                if command not in cmds:
                    print("*** invalid syntax: {} ***".format(arg))
                if command == cmds[0]:
                    self.do_all(instance)
                    return
                if command == cmds[1]:
                    print(models.storage.count(instance))
                    return
                Id = n_list[1].split('(')[1].split(')')[0]
                if command == cmds[2]:
                    Arg = instance + " " + Id
                    self.do_destroy(Arg)
                    return
                if command == cmds[3]:
                    Arg = instance + " " + Id
                    self.do_show(Arg)
                    return
                if command == cmds[4]:
                    Arg = (n_list[-1].split(","))
                    n_id = Arg[0].split("(")[-1]
                    n_name = Arg[1]
                    n_value = Arg[2].split(')')[0]
                    self.do_update("{} \
{} {} {}".format(instance, n_id, n_name, n_value))

                    return
            except IndexError:
                return

        else:
            print("*** invalid syntax: {} ***")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
