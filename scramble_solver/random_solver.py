import random

class RandomSolver:
    def __init__(self, actions, *args):
        self.__actions = actions

    def solve(self, game):
        self.__game = game
        self.__moves_num = 0

        while True:
            self.__moves_num += 1
            action = random.choice(self.__actions)
            self.__game.step(action)
            if self.__game.is_solved():
                return self.__moves_num
