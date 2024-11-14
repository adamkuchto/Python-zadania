"""
This file contains all function about the game logic.
"""
import sys
from random import randint, choice
from tools import ColorPrint

YOUWON = True
YOULOSE = False

class Game:
    """
    A class to represent the game logic.
    """
    def __init__(self) -> None:
        """
        Initializes an instance of the Game class.
        """
        self.goldNumber = None
        self.playerNumber = None
        self.range = None
        self.level = None
        self.howManyPlayers = None

    def getLevel(self):
        """
        Prompts the user to set the game level.
        """
        self.level = int(input("Set the level (1 - 3): "))

    def getRange(self):
        """
        Prompts the user to set the range for the goldNumber.
        Ensures the range is between 0 and 100.
        """
        rangeTab = ['0 - 100', '0 - 1000', '0 - 10000']
        levelTab = [100, 1000, 10000]
        try:
            range_value = int(input(f"Set the range ({rangeTab[self.level - 1]}): "))
            if 0 <= range_value <= levelTab[self.level - 1]:
                self.range = range_value
            else:
                ColorPrint(ColorPrint.error, (
                    f"Wrong number, please enter a number between 0 and "
                    f"{levelTab[self.level - 1]}."
                ))
        except ValueError:
            ColorPrint(ColorPrint.error, "Please enter a valid number.")

    def getGoldNumber(self):
        """
        Sets the goldNumber within the specified range.
        If the range is not set, prompts the user to set the range first.
        """
        if self.range is not None:
            self.goldNumber = randint(0, self.range)
        else:
            ColorPrint(ColorPrint.error, "Range is not set. Please set the range first.")

    def getPlayerNumber(self, text="Guess"):
        """
        Prompts the player to guess a number.
        
        Parameters
        ----------
        text : str
            The prompt text to display to the player.
        """
        try:
            ColorPrint(ColorPrint.info, f"{text} the number!!!\n\r")
            self.playerNumber = int(input())
        except ValueError:
            ColorPrint(ColorPrint.error, "Please enter a valid number.")

    def checkNumbers(self):
        """
        Checks if the player's guess matches the goldNumber.
        
        Returns
        -------
        bool
            True if the player's guess matches the goldNumber, False otherwise.
        """
        return YOUWON if self.goldNumber == self.playerNumber else YOULOSE

    def multiplayer(self):
        """
        Runs multiplayer game.
        """
        again = "Y"
        players = {}
        try:
            self.howManyPlayers = int(input("Enter numbers of players: "))
        except ValueError:
            ColorPrint(ColorPrint.error, f"{ValueError}")

        for i in range(1, self.howManyPlayers + 1):
            try:
                nick = input(f"Enter nickname of {i} player: ")
                players[nick] = 0
            except:
                ColorPrint(ColorPrint.error, "Wrong value")

        self.getLevel()
        self.getRange()

        while again == "Y":
            self.getGoldNumber()
            print(f"DEBUG {self.goldNumber}")
            for p in players:
                try:
                    num = int(input(f"{p} guess the number: "))
                except ValueError:
                    ColorPrint(ColorPrint.error, "Bad value")
                    continue
                if num == self.goldNumber:
                    players[p] += 1 
            ColorPrint(ColorPrint.info, f" Score {players}")
            again = input("Once again? (Y/N)").upper()
            


    def playGame(self, attempts, mode=1):
        """
        Runs the main game loop with the specified number of attempts and mode.
        
        Parameters
        ----------
        attempts : int
            The number of attempts the player has to guess the number.
        mode : int, optional
            The mode of the game (default is 1).
            Mode 1: Player guesses the number.
            Mode 2: Player sets the number, computer guesses.
            Mode 3: Alternating turns between player and computer.
            Mode 4: Multiplayer game mode.
            Mode 5: Quit the game.
        """
        if mode == 4:
            self.multiplayer()
            return
        if mode == 5:
            sys.exit()
        self.getLevel()
        self.getRange()
        if mode == 1:
            self.getGoldNumber()
        elif mode == 2:
            self.getPlayerNumber(text="Set")
        elif mode == 3:
            self.getGoldNumber()

        playerTurn = choice([True, False])

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

        ColorPrint(ColorPrint.error, "GAME OVER")
