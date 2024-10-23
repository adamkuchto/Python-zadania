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

class Menu:
	def __init__(self) -> None:
		pass

	def printMenu(self):
		ColorPrint(ColorPrint.info, NOTICE)