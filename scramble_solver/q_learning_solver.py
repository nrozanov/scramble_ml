import numpy as np
import random

EPSILON = 0.1
LEARNING_RATE = 0.1
GAMMA = 0.6

class QLearningSolver:
    def __init__(self, actions, gsize):
        self.__gsize = gsize
        self.__actions = actions
        self._init_q_matrix()


    def _init_q_matrix(self):
        permutations = list()
        self._generate_permutations(permutations, None, list(range(-1, self.__gsize**2 - 1)))
        self.__q_values = {permutation: [0 for action in self.__actions] for permutation in permutations}


    def _generate_permutations(self, permutations, curr_permutation, left_values):
        if not left_values:
            permutations.append(curr_permutation)
            return

        for value in left_values:
            new_permutation = (curr_permutation and curr_permutation + f';{value}') or str(value)
            new_left_values = [left_value for left_value in list(left_values) if left_value != value]
            self._generate_permutations(permutations, new_permutation, new_left_values)


    def solve(self, game):
        self.__game = game
        self.__moves_num = 0

        current_state = self._get_state_key()
        reward, done = 0, False
        
        while not done:
            self.__moves_num += 1
            if np.random.uniform(0,1) < EPSILON:
                action = self.__actions.index(random.choice(self.__actions))
            else:
                action = self.__q_values[current_state].index(max(self.__q_values[current_state]))

            next_state, reward, done = self._step(current_state, action)
            
            self.__q_values[current_state][action] = (1-LEARNING_RATE) * self.__q_values[current_state][action] + LEARNING_RATE*(reward + GAMMA*max(self.__q_values[next_state]))

            current_state = next_state

        return self.__moves_num


    def _get_state_key(self):
        return ';'.join([str(element) for row in self.__game.get_state() for element in row])


    def _step(self, current_state, action):
        self.__game.step(self.__actions[action])

        new_state = self._get_state_key()
        is_solved = self.__game.is_solved()
        reward = (is_solved and 100) or -1

        return new_state, reward, is_solved
