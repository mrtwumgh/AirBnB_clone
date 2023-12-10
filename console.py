#!/usr/bin/python3
"""
console for the AirBnB project
"""
import cmd
import os
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class for the console
    """
    prompt = "(hbnb) "
    mods = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.mods:
            print("** class doesn't exit **")
        else:
            if arg == "User":
                new_obj = User()
            elif arg == "State":
                new_obj = State()
            elif arg == "City":
                new_obj = City()
            elif arg == "Amenity":
                new_obj = Amenity()
            elif arg == "Place":
                new_obj = Place()
            elif arg == "Review":
                new_obj = Review()
            else:
                new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.mods:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage_db = storage.all()
            key = args[0] + "." + args[1]
            if key not in storage_db:
                print("** no instance found **")
            else:
                print(storage_db[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.mods:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage_db = storage.all()
            key = args[0] + "." + args[1]
            if key not in storage_db:
                print("** no instance found **")
            else:
                del storage_db[key]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = arg.split(".")
        if len(args) > 0 and args[0] not in self.mods:
            print("** class doesn't exist **")
        else:
            storage_db = storage.all()
            for key, value in storage_db.items():
                if len(args) > 0 and args[0] != key.split(".")[0]:
                    continue
                print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.mods:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            storage_db = storage.all()
            key = args[0] + "." + args[1]
            if key not in storage_db:
                print("** no instance found **")
            else:
                attribute = args[2]
                value = args[3]
                if attribute not in ['id', 'created_at', 'updated_at']:
                    if '.' in value:
                        try:
                            value = float(value)
                        except ValueError:
                            value = str(value)
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            value = str(value)
                    setattr(storage_db[key], attribute, value)
                    storage.save()

    def do_count(self, arg):
        """
        Prints the number of instances of a class
        """
        if arg not in self.mods:
            print("** class doesn't exist **")
        else:
            storage_db = storage.all()
            count = 0
            for key in storage_db.keys():
                if arg == key.split(".")[0]:
                    count += 1
            print(count)

    def precmd(self, arg):
        """
        precmd method
        """
        if not os.isatty(sys.stdin.fileno()):
            print()
        try:
            args = arg.split(".")
            if len(args) == 2:
                if args[1] == "all()":
                    return "all " + args[0]
        except Exception:
            pass
        try:
            args = arg.split(".")
            if len(args) == 2:
                if args[1] == "count()":
                    return "count " + args[0]
        except Exception:
            pass
        try:
            args = arg.split(".")
            if len(args) == 2 and args[1].startswith("show"):
                id = args[1][6:-2]
                return "show " + args[0] + " " + id
        except Exception:
            pass
        try:
            args = arg.split(".")
            if len(args) == 2 and args[1].startswith("destroy"):
                id = args[1][9:-2]
                return "destroy " + args[0] + " " + id
        except Exception:
            pass
        return arg

    def emptyline(self):
        """
        prints an empty line
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Prints out the help for quit
        """
        print("Quit command to exit the program")
        print()

    def help_create(self):
        """
        Prints out the help for create
        """
        print("Creates a new instance of BaseModel")
        print("Saves it(to the JSON File) and prints the id")
        print("Ex. $ create BaseModel")

    def help_show(self):
        """
        Prints out the help for show
        """
        print("Prints the string representation of an instance")
        print("Based on the class name and id")
        print("Ex. $ show BaseModel 1234-1234-1234")

    def help_destroy(self):
        """
        Prints out the help for delete
        """
        print("Deletes an instance bease on the class name")
        print("and id(save the change into the JSON File)")
        print("Ex. $ destroy BaseModel 1234-1234-1234")

    def help_all(self):
        """
        Prints out the help for delete
        """
        print("Prints all string representation of all instances")
        print("based or not on the class name")
        print("Ex. $ all BaseModel or all")

    def help_update(self):
        """
        Prints out the help for update
        """
        print("Updates an instance based on the class name")
        print("and id by add or updating attribute")
        print("(Save the change into the JSON file)")
        print("Ex. $ update BaseModel 1234-1234-1234 email 'airbnb@mail.com")

    def help_count(self):
        """
        Prints out the help for count
        """
        print("Retrieves the number of instances of a class")
        print("<class name>.count().")

    def do_EOF(self, arg):
        """
        EOF to quit
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
