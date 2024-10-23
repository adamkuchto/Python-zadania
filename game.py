from random import randint
from tools import ColorPrint

YOUWON = True
YOULOSE = False

class Game:
	def __init__(self) -> None:
		self.goldNumber = None
		self.playerNumber = None
		
	def getGoldNumber(self):
		try:
			range_value = int(input("Set the range: "))
			if range_value > 100 or range_value < 0:
				ColorPrint(ColorPrint.error, "Wrong number, please enter a number between 0 and 100.")
			else:
				self.goldNumber = randint(0, range_value)
		except ValueError:
			ColorPrint(ColorPrint.error, "Please enter a valid number.")

	def getPlayerNumber(self):
		try:
			self.playerNumber = int(input("Guess the nuber!!!\n\r"))
		except ValueError:
			ColorPrint(ColorPrint.error, "Please enter a valid number.")

	def checkNumers(self):
		return YOUWON if self.goldNumber == self.playerNumber else YOULOSE



