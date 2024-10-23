#!/usr/bin/env python

from player import Player
from menu import Menu
from tools import ColorPrint
from game import Game

def main():
	menu = Menu()
	game = Game()
	menu.printMenu()
	player = Player(input("Enter your nickname: "))
	# sprawdz czy już grał
	player.result = 3
	game.getGoldNumber()
	try:
		while player.result:
			game.getPlayerNumber()
			if game.checkNumers():
				ColorPrint(ColorPrint.error, "YOU WON")
				break
			else:
				player.result -= 1
				ColorPrint(ColorPrint.error, "WRONG")
				continue
	except:
		pass
	finally:
		player.saveResult()
		ColorPrint(ColorPrint.info, f"Result saved for player {player.nick} with score {player.result}")

# def main():
# 	menu = Menu()
# 	game = Game()
# 	menu.printMenu()
# 	# player = Player("Player1")
# 	# player.result = "4"
# 	# player.saveResult()
# 	# player.readResult()


if __name__ == "__main__":
	main()