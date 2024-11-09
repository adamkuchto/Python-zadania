from random import randint
from tools import ColorPrint
import random

YOUWON = True
YOULOSE = False

class Game:
	def __init__(self) -> None:
		self.goldNumber = None
		self.playerNumber = None
		self.range = None

	def getRange(self):
		try:
			range_value = int(input("Set the range (0-100): "))
			if 0 <= range_value <= 100:
				self.range = range_value
			else:
				ColorPrint(ColorPrint.error, "Wrong number, please enter a number between 0 and 100.")
		except ValueError:
			ColorPrint(ColorPrint.error, "Please enter a valid number.")

	def getGoldNumber(self):
		if self.range is not None:
			self.goldNumber = randint(0, self.range)
		else:
			ColorPrint(ColorPrint.error, "Range is not set. Please set the range first.")

	def getPlayerNumber(self, text="Guess"):
		try:
			ColorPrint(ColorPrint.info, f"{text} the number!!!\n\r")
			self.playerNumber = int(input())
		except ValueError:
			ColorPrint(ColorPrint.error, "Please enter a valid number.")

	def checkNumbers(self):
		return YOUWON if self.goldNumber == self.playerNumber else YOULOSE

	def playGame(self, attempts, mode=1):
		self.getRange()
		if mode == 1:
			self.getGoldNumber()
		elif mode == 2:
			self.getPlayerNumber(text="Set")
		elif mode == 3:
			self.getGoldNumber()

		playerTurn = random.choice([True, False])

		while attempts:
			if mode == 1 or (mode == 3 and playerTurn):
				ColorPrint(ColorPrint.info, "Player turn")
				self.getPlayerNumber()
			else:
				ColorPrint(ColorPrint.info, "Computer turn")
				self.getGoldNumber()


			if self.checkNumbers():
				if mode == 1 or (mode == 3 and playerTurn):
					ColorPrint(ColorPrint.success, "YOU WON")
				else:
					ColorPrint(ColorPrint.success, "COMPUTER WON")
				break
			else:
				attempts -= 1
				ColorPrint(ColorPrint.error, "WRONG")
				if mode == 3:
					playerTurn = not playerTurn
		else:
			ColorPrint(ColorPrint.error, "GAME OVER")

