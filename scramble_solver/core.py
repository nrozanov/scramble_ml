from collections import namedtuple
import re
import argparse

from random_solver import RandomSolver
from q_learning_solver import QLearningSolver
from scramble_game import ScrambleGame

RunStats = namedtuple("SolverStats", "RandResult MLResult MLBetter")
UnsolvableExceptionRe = re.compile('Unsolvable')

def run():
	parser = argparse.ArgumentParser(description='Compare random and q learning algorithms efficiency while solving sliding puzzle game')
	parser.add_argument('gsize', type=int, help='game dimension')
	parser.add_argument('run_num', type=int, help='number of games to play')
	args = parser.parse_args()

	gsize, run_num = args.gsize, args.run_num

	actions = ScrambleGame.get_actions()
	random_solver = RandomSolver(actions, gsize)
	q_learing_solver = QLearningSolver(actions, gsize)
	stats = list()
	for i in range(run_num):
		try:
			rand_game, q_learning_game = ScrambleGame(gsize, i), ScrambleGame(gsize, i)
		except Exception as e:
			if not UnsolvableExceptionRe.match(str(e)):
				raise e
		else:
			rand_result, q_learning_result = random_solver.solve(rand_game), q_learing_solver.solve(q_learning_game)
			stat = RunStats(rand_result, q_learning_result, (rand_result - q_learning_result) / q_learning_result * 100)
			stats.append(stat)
	print(f'Average value better {sum([stat.MLBetter for stat in stats]) / len(stats)}%')


if __name__ == "__main__":
	run()
