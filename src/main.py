from random import random
from constants import DOWN, NO_MOVE
from include.ai.evaluator import Evaluator
from include.game.game import Game
from include.gui.gui import Gui

def play_game():
    game = Game(20, 20)
    gui = Gui(20, 20, game.board)
    evaluator = Evaluator()
    frames = 0
    while True:
        gui.render()
        frames += 1
        if frames >= 60:
            moves = evaluator.get_all_moves(game.current_piece, game.board)
            if len(moves) > 0:
                game.current_piece = moves[int(random() * len(moves))].piece
                game.drop_piece()
            frames = 0

if __name__ == "__main__":
    play_game()
