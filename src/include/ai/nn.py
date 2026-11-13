from torch import nn
import torch
from torch.nn.utils import parameters_to_vector, vector_to_parameters

INPUT_LAYER = 4
HIDDEN_LAYER = 7
OUTPUT_LAYER = 4

torch.set_grad_enabled(False)
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Sequential(
            nn.Linear(INPUT_LAYER, HIDDEN_LAYER),
            nn.ReLU(),
            nn.Linear(HIDDEN_LAYER, HIDDEN_LAYER),
            nn.ReLU(),
            nn.Linear(HIDDEN_LAYER, OUTPUT_LAYER)
        )

    def get_params(self):
        params = self.linear.parameters()
        return parameters_to_vector(params)

    def set_params(self, params):
        vector_to_parameters(params, self.linear.parameters())

    def forward(self, x):
        x = self.flatten(x)
        return self.linear(x)

    def choose(self, x):
        pass

    def save_model(self, path):
        torch.save(self.state_dict(), path)
