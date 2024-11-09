"""
Player Management.
"""
import toml
from tools import ColorPrint

class Player:
    """
     A class to represent a player in the game.
    """

    def __init__(self, nick) -> None:
        """
        Initializes an instance of the Player class.

        Parameters
        ----------
        nick : str
            The nickname of the player.
        """
        self.nick = nick
        self.result = 0
        self.path = ".toml"
        self.score = 0

    def saveResult(self):
        """
        Saves the player's result to a TOML file.

        The file is named after the player's nickname with a .toml extension.
        """
        text = {"player": {self.nick: int(self.result)}}
        try:
            with open(self.nick + self.path, 'w', encoding='utf-8') as f:
                toml.dump(text, f)
        except FileNotFoundError as err:
            ColorPrint(ColorPrint.error, f'error: {err}')


    def readResult(self):
        """
        Reads the player's result from a TOML file.

        Returns
        -------
        int or None
            The player's score if the file exists and is readable, otherwise None.
        """
        try:
            with open(self.nick + self.path, 'r', encoding='utf-8') as f:
                text = toml.load(f)
                return text['player'][self.nick]
        except FileNotFoundError:
            ColorPrint(ColorPrint.info, 'It is your first game. Welcome!')
        except PermissionError:
            ColorPrint(ColorPrint.error, 'You do not have permission to open this file!')
        except ValueError:
            ColorPrint(ColorPrint.error, 'Invalid data format!')
        return None

    def showResult(self):
        """
        Displays the player's score and updates the result.

        If the score is read successfully, it is displayed and added to a base value of 3.
        If the score is not available, the result is set to 3.
        """
        self.score = self.readResult()
        if self.score:
            ColorPrint(ColorPrint.info, f"Your score: {self.score}")
            self.result = 3 + self.score
        else:
            self.result = 3
