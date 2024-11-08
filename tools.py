from colorama import Fore, Back, Style

class ColorPrint:
	error = Fore.WHITE + Back.RED
	info = Fore.BLACK + Back.GREEN
	success = Fore.CYAN + Back.WHITE
	fail = Fore.BLUE + Back.YELLOW

	def __init__(self, style, text) -> None:
		print(style + text + Style.RESET_ALL)
	

