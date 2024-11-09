"""
This file contains all function about the game logic.
"""
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

    def getRange(self):
        """
        Prompts the user to set the range for the goldNumber.
        Ensures the range is between 0 and 100.
        """
        try:
            range_value = int(input("Set the range (0-100): "))
            if 0 <= range_value <= 100:
                self.range = range_value
            else:
                ColorPrint(ColorPrint.error, "Wrong number,\
                    please enter a number between 0 and 100.")
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
        """
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
