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
	player.showResult()
	game.playGame(player.result, menu.mode())
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