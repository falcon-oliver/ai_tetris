from .piece import Piece
import numpy as np

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=bool)
        self.previous_board = self.board
        self.lines_cleared = 0

    def place_piece(self, piece):
        piece_matrix = piece.matrix
        rows, cols = piece_matrix.shape
        self.previous_board = self.board.copy()
        self.board[piece.y:piece.y+rows, piece.x:piece.x+cols] |= piece_matrix
        self.lines_cleared = self.clear_lines()

    def go_back(self):
        self.board = self.previous_board

    def is_placable(self, piece):
        piece_matrix = piece.matrix
        rows, cols = piece_matrix.shape
        if piece.y + rows >= self.height:
            return True
        return (self.board[piece.y+1:piece.y+rows+1, piece.x:piece.x+cols] & piece_matrix).any()

    def _out_of_bounds(self, piece):
        piece_matrix = piece.matrix
        rows, cols = piece_matrix.shape
        return (piece.x < 0 or piece.x + cols > self.width or piece.y < 0 or piece.y + rows > self.height)

    def _intersects(self, piece):
        piece_matrix = piece.matrix
        rows, cols = piece_matrix.shape
        board_target_area = self.board[piece.y:piece.y+rows, piece.x:piece.x+cols]
        return (board_target_area & piece_matrix).any()

    def is_valid(self, piece):
        return not self._out_of_bounds(piece) and not self._intersects(piece)
    
    def reset(self):
        self.board = np.zeros((self.height, self.width), dtype=bool)

    def clear_lines(self):
        lines_cleared = 0
        row = self.height
        while row > 0:
            row -=1
            while np.all(self.board[row] == 1):
                self.board[1:row+1] = self.board[0:row]
                self.board[0] = 0
                lines_cleared += 1
        return lines_cleared