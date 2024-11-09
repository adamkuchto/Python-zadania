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
	def __init__(self) -> None:
		pass

	def printMenu(self):
		ColorPrint(ColorPrint.info, NOTICE)

	def mode(self):
		ColorPrint(ColorPrint.info, OPTIONS)
		return int(input())
		

