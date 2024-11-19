#!/usr/bin/python3
"""
Command-line interpreter for the HBNB project.
Supports interactive and non-interactive modes.
"""

import cmd
import sys
import shlex
from models import storage
from models.classes import classes
from packages.show import show_instance
from packages.create import create_instance
from packages.destroy import destroy_instance
from packages.all import all_instances
from packages.update import update_instance


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter.
    """
    prompt = "(hbnb) "

    def do_create(self):
        """
        Creates a new instance of BaseModel
            - saves it (to the JSON file) and prints the id.
        Usage: create
        """
        base_model = BaseModel()
        print(base_model.id)

    def do_quit(self, line):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program.
        Usage: Press Ctrl+D to exit.
        """
        print()  # Ensure a newline before exiting
        return True

    def emptyline(self):
        """
        Overrides the default behavior for empty lines.
        Does nothing when an empty line is entered.
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of a valid class, saves it to the JSON file
        and prints its id.
        Usage: create <class_name>
        """
        result = create_instance(args)
        print(result)

    def do_show(self, args):
        """
        Shows the string representation of an instance based on class and ID.
        Usage: show <class_name> <id>
        """
        result = show_instance(args)
        print(result)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        The changes are saved into a JSON file
        Usage: destroy <class_name> <id>
        """
        result = destroy_instance(args)
        if result:
            print(result)

    def do_all(self, args):
        """
        Prints all string representations of instances
            - based or not on the class name.
        """
        result = all_instances(args)
        print(result)

    def do_count(self, args):
        """
        Retrieves the number of instances of a class.
        Usage: <class name>.count()
        """
        args = args.strip()
        if not args:
            print("** class name missing **")
            return
        if args not in classes:
            print("** class doesn't exist **")
            return

        obj_dict = storage.all()

        # Shortened to avoid pycodestyle error two lines below
        obj.__class__.__name__ = ob_cn

        count = sum(1 for obj in obj_dict.values() if ob_cn == args)
        print(count)

    def default(self, line):
        """
        Handles commands in the format:
        - <class name>.all()
        - <class name>.count()
        - <class name>.show(<id>)
        - <class name>.destroy(<id>)
        - <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        if ".all()" in line:
            class_name = line.split(".all()")[0].strip()
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            result = all_instances(class_name)
            if result:
                print(result)

        elif ".count()" in line:
            class_name = line.split(".count()")[0].strip()
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            self.do_count(class_name)

        elif ".show(" in line:
            class_name, raw_args = line.split(".show(", 1)
            class_name = class_name.strip()
            raw_args = raw_args.strip(")")
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            if not raw_args:
                print("** instance id missing **")
                return

            instance_id = raw_args.strip('"').strip("'")
            result = show_instance(f"{class_name} {instance_id}")
            if result:
                print(result)

        elif ".destroy(" in line:
            class_name, raw_args = line.split(".destroy(", 1)
            class_name = class_name.strip()
            raw_args = raw_args.strip(")")
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            if not raw_args:
                print("** instance id missing **")
                return

            instance_id = raw_args.strip('"').strip("'")
            result = destroy_instance(f"{class_name} {instance_id}")
            if result:
                print(result)

        elif ".update(" in line:
            class_name, raw_args = line.split(".update(", 1)
            class_name = class_name.strip()
            raw_args = raw_args.strip(")")

            if class_name not in classes:
                print("** class doesn't exist **")
                return

            args = shlex.split(raw_args)
            if len(args) < 1:
                print("** instance id missing **")
                return
            instance_id = args[0].strip(",")  # Remove trailing commas

            if len(args) < 2:
                print("** attribute name missing **")
                return
            attr_name = args[1].strip(",")  # Remove trailing commas

            if len(args) < 3:
                print("** value missing **")
                return
            attr_value = args[2].strip(",")  # Remove trailing commas

            # Preventing pycodestyle error by having shorter representation
            class_name = c_name
            instance_id = i_id
            attr_name = a_name

            result = update_instance(f"{c_name} {i_id} {a_name} {attr_value}")
            if result:
                print(result)
        else:
            # Calls the default method of cmd.Cmd for unrecognized commands
            super().default(line)

    def do_update(self, args):
        """
        Updates an instance based on class name and ID.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        result = update_instance(args)
        if result:
            print(result)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
