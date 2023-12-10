#!/usr/bin/python3
"""
console for the AirBnB project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class for the console
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User"]

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exit **")
        else:
            if arg == "User":
                new_obj = User()
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
        elif args[0] not in self.classes:
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
        elif args[0] not in self.classes:
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
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
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
        elif args[0] not in self.classes:
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

    def do_EOF(self, arg):
        """
        EOF to quit
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()