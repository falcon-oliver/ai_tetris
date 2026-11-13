from random import random
from numpy import inf
from numpy import dot
from include.ai.bfs import get_all_moves
from include.ai.evaluator import get_features
from include.ai.features import Features

BUMPINESS = -0.8
AGGREGATE_HEIGHT = -0.4
WELLS = -0.4
HOLES = -0.3
LINES_CLEARED = 0.2

FEATURES = [Features.BUMPINESS, Features.AGGREGATE_HEIGHT, Features.WELLS, Features.HOLES, Features.LINES_CLEARED]
WEIGHTS = [BUMPINESS, AGGREGATE_HEIGHT, WELLS, HOLES, LINES_CLEARED]

class HeuristicAi():
    def __init__(self, game):
        self.game = game
        self.board = game.board

    def evaluate(self, features):
        score = dot(features, WEIGHTS)
        return score

    def get_optimal_move(self):
        next_piece = self.game.next_piece
        moves = get_all_moves(next_piece, self.board)
        optimal_piece = None
        optimal = -inf
        optimal_features = []
        for piece in moves:
            self.board.place_piece(piece.piece)
            features = get_features(FEATURES, self.board)
            score = self.evaluate(features)
            if optimal < score:
                optimal_piece = piece.piece
                optimal = score
                optimal_features = features
            self.board.go_back()
        self.board.go_back()
        print(f'optimal features {optimal_features}')
        return optimal_piece

    def step(self):
        optimal_piece = self.get_optimal_move()
        self.game.drop_piece(optimal_piece)
