from scramble import (
	ImageScrambleGame,
	MOVE_UP,
	MOVE_LEFT,
	MOVE_DOWN,
	MOVE_RIGHT
)

class ScrambleGame:
	def __init__(self, gsize, seednum):
		self.__gsize = gsize
		self.__game = ImageScrambleGame(gsize=gsize, seednum=seednum)


	def is_solved(self):
		state = self.__game.get_state()
		tile_index = 0
		for y in range(len(state)):
			line = state[y]
			for x in range(len(line)):
				element = state[y][x]
				if element == -1:
					return tile_index == self.__gsize * self.__gsize - 1
				if element != tile_index:
					return False
				tile_index += 1
		return True


	def step(self, action):
		self.__game.move_blank(action)


	def get_state(self):
		return self.__game.get_state()


	@staticmethod
	def get_actions():
		return (MOVE_UP, MOVE_LEFT, MOVE_DOWN, MOVE_RIGHT)
