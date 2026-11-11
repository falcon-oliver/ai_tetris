import numpy as np
from constants import LEFT, RIGHT, DOWN, ROTATE

PIECE_SHAPES = [
    np.ones((4, 1), dtype=bool),
    np.ones((2, 2), dtype=bool),
    np.array([[0, 1, 1], [1, 1, 0]], dtype=bool),
    np.array([[1, 1, 0], [0, 1, 1]], dtype=bool),
    np.array([[1, 0], [1, 0], [1, 1]], dtype=bool),
    np.array([[0, 1], [0, 1], [1, 1]], dtype=bool),
    np.array([[1, 1, 1], [0, 1, 0]], dtype=bool)
]

class Piece:
    def __init__(self, x, y, piece):
        piece = PIECE_SHAPES[piece]
        self.x = self.previous_x = self.start_x = x
        self.y = self.previous_y = self.start_y = y
        self.rotation_index = self.previous_index = 0
        self.rotations = [np.rot90(piece, i) for i in range(4)]
        self.heights = [self._calculate_height(piece) for piece in self.rotations]

    @property
    def state(self):
        return (self.x, self.y, self.rotation_index)
    @property
    def matrix(self):
        return self.rotations[self.rotation_index]

    @property
    def height(self):
        return self.heights[self.rotation_index]

    def _calculate_height(self, piece):
        rows = piece.shape[0]
        top_index = np.argmax(piece, axis=0)
        heights = rows - top_index
        return heights

    def move(self, move_index):
        self.previous_x = self.x
        self.previous_y = self.y
        self.previous_index = self.rotation_index
        if move_index == LEFT:
            self.x -= 1
        elif move_index == RIGHT:
            self.x += 1
        elif move_index == DOWN:
            self.y += 1
        elif move_index == ROTATE:
            self.rotation_index = (self.rotation_index + 1) % 4

    def reset(self):
        self.x = self.previous_x = self.start_x
        self.y = self.previous_y = self.start_y
        self.rotation_index = 0
