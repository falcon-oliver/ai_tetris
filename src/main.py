from random import random
from include.ai.genetic_algorithm import GeneticAlgorithm
from include.ai.heuristic_ai import HeuristicAi
from include.game.game import Game
from include.gui.gui import Gui

FPS = 60
def test_heuristic_ai():
    game = Game(20, 20)
    gui = Gui(20, 20, game.board)
    heuristic_ai = HeuristicAi(game)
    frames = 0
    while True:
        gui.render()
        frames += 1
        if frames >= FPS:
            heuristic_ai.step()
            frames = 0


def test_genetic_algorithm():
    genetic_algorithm = GeneticAlgorithm()
    genetic_algorithm.train()
    nn = genetic_algorithm.get_best_network()

if __name__ == "__main__":
    test_genetic_algorithm()