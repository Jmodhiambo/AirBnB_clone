#!/usr/bin/python3
"""
Command-line interpreter for the HBNB project.
Supports interactive and non-interactive modes.
"""

import cmd
import sys
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
        print() # Ensure a newline before exiting
        return True

    def emptyline(self):
        """
        Overrides the default behavior for empty lines.
        Does nothing when an empty line is entered.
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of a valid class, saves it to the JSON file, 
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
        Prints all string representations of instances based or not on the class name.
        """
        args = args.strip()
        if args.endswith(".all()"):
            class_name = args[:-6].strip()
            if not class_name:
                print("** class name missing **")
                return
            if class_name not in classes:
                print("** class doesn't exist **")
                return
        else:
            class_name = args if args else None

        result = all_instances(class_name)
        print(result)

    def default(self, line):
        """
        Overrides the default behavior of cmd.Cmd to handle custom commands
        like <class name>.all().
        """
        args = line.strip()
        if ".all()" in args:
            self.do_all(args)
        else:
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
    # Check if commands are passed as arguments
    if len(sys.argv) > 1:
        # Concatenate all arguments into a single command string
        command = " ".join(sys.argv[1:])
        interpreter = HBNBCommand()
        # Process the command and exit
        interpreter.onecmd(command)
    else:
        # Start the interactive loop
        HBNBCommand().cmdloop()
