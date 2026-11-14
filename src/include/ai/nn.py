import numpy as np
from torch import nn
import torch
from torch.nn.utils import parameters_to_vector, vector_to_parameters
from include.ai.bfs import get_all_moves
from include.ai.evaluator import get_features
from include.ai.features import Features

LINES_CLEARED = 0.16
SURVIVAL_SCORE = 0.2

INPUT_LAYER = 5
HIDDEN_LAYER = 7
OUTPUT_LAYER = 5

FEATURES = [Features.HOLES, Features.AGGREGATE_HEIGHT, Features.WELLS, Features.LINES_CLEARED, Features.BUMPINESS]

torch.set_grad_enabled(False)
class NeuralNetwork(nn.Module):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.board = game.board
        self.total_lines_cleared = 0
        self.survival_time = 0
        self.network = nn.Sequential(
            nn.Linear(INPUT_LAYER, HIDDEN_LAYER),
            nn.ReLU(),
            nn.Linear(HIDDEN_LAYER, OUTPUT_LAYER)
        )

    @property
    def fitness(self):
        return (self.total_lines_cleared * LINES_CLEARED + self.survival_time * SURVIVAL_SCORE)

    def get_features(self, piece):
        self.board.place_piece(piece.piece)
        features = torch.tensor(get_features(FEATURES, self.board), dtype=torch.float32)
        return features

    def _get_param(self, param_name):
        values = []
        for name, param in self.named_parameters():
            if param_name in name:
                values.append(param)
        return values
    
    def get_weights(self):
        return parameters_to_vector(self._get_param("weight"))

    def get_biases(self):
        return parameters_to_vector(self._get_param("bias"))
    
    def set_weights(self, weights):
        weight_params = self._get_param("weight")
        vector_to_parameters(weights, weight_params)

    def set_biases(self, biases):
        bias_params = self._get_param("bias")
        vector_to_parameters(biases, bias_params)

    def forward(self, x):
        return self.network(x)

    def play_game(self):
        while len((available_moves := get_all_moves(self.game.next_piece, self.board))) > 0:
            max_score = -np.inf
            chosen_piece = None
            for piece in available_moves:
                features = self.get_features(piece)
                scores = self.forward(features)
                if (score := sum(scores)) > max_score:
                    chosen_piece = piece.piece
                    max_score = score
            self.total_lines_cleared += self.game.drop_piece(chosen_piece)
            self.survival_time += 1

    def save_model(self, path):
        torch.save(self.state_dict(), path)
