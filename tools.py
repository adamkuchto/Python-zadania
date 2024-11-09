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
