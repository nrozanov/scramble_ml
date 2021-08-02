import random

class RandomSolver:
    def __init__(self, actions, *args):
        self.actions = actions

    def solve(self, game):
        self.game = game
        self.moves_num = 0

        while True:
            self.moves_num += 1
            action = random.choice(self.actions)
            self.game.step(action)
            if self.game.is_solved():
                return self.moves_num
