#!/usr/bin/env python
from random import randint
import toml

YOUWON = True
YOULOSE = False
NOTICE = "This is a gessing number game\nYou have 3 hange to guess the number\n\
Max score is 3 points\nGOOD LUCK!!!"
		
class Player:
	# Constructor.
	def __init__(self, nick) -> None:
		# Player's nick.
		self.nick = nick
		self.result = 0  # Initialize result to 0 or any default value
		self.path = ".toml"

	# Save result to file.
	def saveResult(self):
		text = {"player": {self.nick: int(self.result)}}
		with open(self.nick + self.path, 'w') as f:
			toml.dump(text, f)

	def readResult(self):
		with open(self.nick + self.path, 'r') as f:
			text = toml.load(f)
			print(text['player'][self.nick])


class Game:
	def __init__(self) -> None:
		self.goldNumber = None
		self.playerNumber = None
		
	def getGoldNumber(self):
		try:
			range_value = int(input("Set the range: "))
			if range_value > 100 or range_value < 0:
				print("Wrong number, please enter a number between 0 and 100.")
			else:
				self.goldNumber = randint(0, range_value)
		except ValueError:
			print("Please enter a valid number.")

	def getPlayerNumber(self):
		try:
			self.playerNumber = int(input("Guess the nuber!!!\n\r"))
		except ValueError:
			print("Please enter a valid number.")

	def checkNumers(self):
		print(f"TEST GOLD: {self.goldNumber} PLAYER: {self.playerNumber}")
		return YOUWON if self.goldNumber == self.playerNumber else YOULOSE

class Menu:
	def __init__(self) -> None:
		pass

	def checkPlayerScore(self):
		pass

	def printMenu(self):
		print("*"*40)
		print("         WELCOME")
		print(NOTICE)
		print("*"*40)

# def main():
	# menu = Menu()
	# game = Game()
	# menu.printMenu()
	# player = Player(input("Enter your nickname: "))
	# # sprawdz czy już grał
	# player.result = 3
	# game.getGoldNumber()
	# try:
	# 	while player.result:
	# 		player.result -= 1
	# 		game.getPlayerNumber()
	# 		if game.checkNumers():
	# 			print("YOU WON")
	# 			break
	# 		else:
	# 			print("WRONG")
	# 			continue
	# except:
	# 	pass
	# finally:
	# 	player.saveResult()
	# 	print(f"Result saved for player {player.nick} with score {player.result}")

def main():
	menu = Menu()
	game = Game()
	player = Player("aaa")
	player.result = "4"
	player.saveResult()
	player.readResult()


if __name__ == "__main__":
	main()
