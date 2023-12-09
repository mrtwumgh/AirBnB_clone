#!/usr/bin/python3
"""
console for the AirBnB project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class for the console
    """
    prompt = "(hbnb) "

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

    def do_EOF(self, arg):
        """
        EOF to quit
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
