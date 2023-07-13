#!/usr/bin/python3
"""
Defines the command interpreter of the HBnB console.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def do_help(self, arg):
        """
        Display help message.
        """
        super().do_help(arg)

    def do_create(self, arg):
        """
        Create a new instance of a class.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show string representation of an instance.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_key = class_name + "." + args[1]
        if instance_key in instances:
            print(instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_key = class_name + "." + args[1]
        if instance_key in instances:
            del instances[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all instances of a class or all instances.
        Usage: all or all <class_name>
        """
        class_name = arg.split()[0] if arg else None
        if class_name and class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        instances = storage.all()
        if class_name:
            filtered_instances = {k: v for k, v in instances.items() if k.split(".")[0] == class_name}
        else:
            filtered_instances = instances
        print([str(instance) for instance in filtered_instances.values()])

    def do_update(self, arg):
        """
        Update an instance based on the class name, id, attribute name, and attribute value.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ("BaseModel",):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_key = class_name + "." + args[1]
        if instance_key in instances:
            instance = instances[instance_key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_value = args[3]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    storage.reload()
    HBNBCommand().cmdloop()

