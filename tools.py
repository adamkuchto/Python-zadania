"""
Additional tools. 
"""
from colorama import Fore, Back, Style


class ColorPrint:
    """
    A class to print colored text using the colorama library.
    """
    error = Fore.WHITE + Back.RED
    info = Fore.BLACK + Back.GREEN
    success = Fore.CYAN + Back.WHITE
    fail = Fore.BLUE + Back.YELLOW

    def __init__(self, style, text) -> None:
        """
        Initializes the ColorPrint instance and prints the text with the specified style.

        Parameters
        ----------
        style : str
            The style to apply to the text.
        text : str
            The text to be printed.
        """
        print(style + text + Style.RESET_ALL)

def switcher(value):
    """
    Returns a string based on the provided value. 
 
    Warning :
        It is a bad idea to compare strings because it has a high possibility of issues.
    Args : value (int): 
        The integer value representing a game mode.
    Returns : str:
        The description of the game mode or "NUL" if the value is not found.
    """
    switch = {
        1: "Player quess number",
        2: "Computer quess number",
        3: "Mixed game",
        4: "Multiplayer",
        5: "Exit"
    }
    return switch.get(value, "NUL")
