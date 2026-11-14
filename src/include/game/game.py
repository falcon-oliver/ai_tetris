from .piece import Piece
from .board import Board
from random import shuffle

START_X = 4
START_Y = 0

class Game:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = Board(width, height)
        self.game_over = False
        self.pieces = [Piece(START_X, START_Y, i) for i in range (7)]
        self.bag = self._generate_bag()
        self.next_piece = self.pieces[self.bag.pop()]

    def _get_next_piece(self):
        self.next_piece.reset()
        if len(self.bag) == 0:
            self.bag = self._generate_bag()
        return self.pieces[self.bag.pop()]

    def _generate_bag(self):
        bag = list(range(7))
        shuffle(bag)
        return bag

    def drop_piece(self, piece):
        lines_cleared = self.board.place_piece(piece)
        self.next_piece = self._get_next_piece()
        return lines_cleared
    
    def reset(self):
        self.game_over = False
        for piece in self.pieces:
            piece.reset()
        self.board.reset()
