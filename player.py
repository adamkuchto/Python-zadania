from tools import ColorPrint
import toml

class Player:
	# Constructor.
	def __init__(self, nick) -> None:
		# Player's nick.
		self.nick = nick
		self.result = 0  # Initialize result to 0 or any default value
		self.path = ".toml"
		self.score = 0

	# Save result to file.
	def saveResult(self):
		text = {"player": {self.nick: int(self.result)}}
		try:
			with open(self.nick + self.path, 'w') as f:
				toml.dump(text, f)
		except FileNotFoundError as err:
			ColorPrint(ColorPrint.error, f'error: {err}')


	def readResult(self):
		try:
			with open(self.nick + self.path, 'r') as f:
				text = toml.load(f)
				return text['player'][self.nick]
		except FileNotFoundError:
			ColorPrint(ColorPrint.info, 'It is your first game. Welcome!')
		except PermissionError:
			ColorPrint(ColorPrint.error, 'You do not have permission to open this file!')
		except ValueError:
			ColorPrint(ColorPrint.error, 'Invalid data format!')

	def showResult(self):
		self.score = self.readResult()
		if self.score:
			ColorPrint(ColorPrint.info, f"Your score: {self.score}")
			self.result = 3 + self.score
		else:
			self.result = 3