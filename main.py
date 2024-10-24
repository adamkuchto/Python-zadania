#!/usr/bin/env python

from player import Player
from menu import Menu
from tools import ColorPrint
from game import Game

def main():
	menu = Menu()
	game = Game()
	menu.printMenu()
	menu.mode()
	player = Player(input("Enter your nickname: "))
	 
	score = player.readResult()
	if score:
		ColorPrint(ColorPrint.info, f"Your score: {score}")
		player.result = 3 + score
	else:
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
# 	menu.printMenu()
# 	menu.mode()
# 	# game = Game()
# 	# player = Player("aaad")
# 	# player.result = "4"
# 	# player.saveResult()
# 	# ile = player.readResult()
# 	# print (ile)


if __name__ == "__main__":
	main()