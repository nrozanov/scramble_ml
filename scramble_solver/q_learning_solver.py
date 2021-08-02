import numpy as np
import random

EPSILON = 0.1
LEARNING_RATE = 0.1
GAMMA = 0.6

class QLearningSolver:
    def __init__(self, actions, gsize):
        self.gsize = gsize
        self.actions = actions
        self._init_q_matrix()

    def _init_q_matrix(self):
        permutations = list()
        self._generate_permutations(permutations, None, list(range(-1, self.gsize**2 - 1)))
        self.q_values = {permutation: [0 for action in self.actions] for permutation in permutations}

    def _generate_permutations(self, permutations, curr_permutation, left_values):
        if not left_values:
            permutations.append(curr_permutation)
            return

        for value in left_values:
            new_permutation = (curr_permutation and curr_permutation + f';{value}') or str(value)
            new_left_values = [left_value for left_value in list(left_values) if left_value != value]
            self._generate_permutations(permutations, new_permutation, new_left_values)

    def solve(self, game):
        self.game = game
        self.moves_num = 0

        current_state = self._get_state_key()
        reward, done = 0, False
        
        while not done:
            self.moves_num += 1
            if np.random.uniform(0,1) < EPSILON:
                action = self.actions.index(random.choice(self.actions))
            else:
                action = self.q_values[current_state].index(max(self.q_values[current_state]))

            next_state, reward, done = self._step(current_state, action)
            
            self.q_values[current_state][action] = (1-LEARNING_RATE) * self.q_values[current_state][action] + LEARNING_RATE*(reward + GAMMA*max(self.q_values[next_state]))

            current_state = next_state

        return self.moves_num

    def _get_state_key(self):
        return ';'.join([str(element) for row in self.game.get_state() for element in row])

    def _step(self, current_state, action):
        self.game.step(self.actions[action])

        new_state = self._get_state_key()
        is_solved = self.game.is_solved()
        reward = (is_solved and 100) or -1

        return new_state, reward, is_solved
