#!/usr/bin/env python

"""
Main program file.
"""
import sys
from player import Player
from menu import Menu
from tools import ColorPrint, switcher
from game import Game

def main():
    """
    Main function.
    """
    menu = Menu()
    game = Game()
    menu.printMenu()
    options = switcher(menu.mode())
    print(options)
    if options == "Player quess number":
        player = Player(input("Enter your nickname: "))
    elif options == "Computer quess number":
        player = Player("Computer")
    elif options == "Mixed game":
        player = Player(input("Enter your nickname: "))
    elif options == "Multiplayer":
        player = Player(input("Enter your nickname: "))
        game.multiplayer()
    elif options == "Quit":
        sys.exit()
    else:
        return

    player.showResult()
    game.playGame(player.result, options)
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
