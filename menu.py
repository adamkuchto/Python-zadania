"""
Main menu
"""
from tools import ColorPrint

NOTICE = """
+--------------------------------------+
|               WELCOME                |
|   This is a number guessing game.    |
|    You have 3 chances to succeed.    |
|        Max score is 3 points.        |
|             GOOD LUCK!!!"            |
+--------------------------------------+
"""
OPTIONS = """
+--------------------------------------+
|1 - Player quess number               |
|2 - Computer quess number             |
|3 - Mixed game                        |
|4 - Quit                              |
+--------------------------------------+
"""

class Menu:
    """
    A class to represent a menu in the application.
    """
    def __init__(self) -> None:
        """
        Initializes an instance of the Menu class.
        """

    def printMenu(self):
        """
        Displays the menu to the user.
        """
        ColorPrint(ColorPrint.info, NOTICE)

    def mode(self):
        """
        Displays mode options and gets the user's selection.
        
        Returns:
            int: The mode selected by the user.
        """
        ColorPrint(ColorPrint.info, OPTIONS)
        return int(input())
