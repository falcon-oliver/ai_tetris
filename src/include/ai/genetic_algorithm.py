from include.ai.nn import NeuralNetwork
from include.game.game import Game

class GeneticAlgorithm:
    def __init__(self):
        self.best_network = None
        self.population = self._generate_population()

    def _generate_population(self, population_size=10):
        population = []
        for i in range(population_size):
            game = Game()
            network = NeuralNetwork(game)
            population.append(network)
        return population

    def _evaluate_population(self):
        fitness_scores = []
        for neural_network in self.population:
            fitness_scores.append(self._evaluate(neural_network))
        return fitness_scores

    def _evaluate(self, neural_network):
        fitness_score = 0
        neural_network.play_game()
        fitness_score = neural_network.fitness
        return fitness_score


    def train(self, iterations=10):
        for i in range(iterations):
            fitness_scores = self._evaluate_population()
            print(fitness_scores)
            pass
        pass

    def get_best_network(self):
        return self.best_network

    pass