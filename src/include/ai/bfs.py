from collections import deque
from copy import deepcopy
from controls import DOWN, LEFT, RIGHT, ROTATE
from include.ai.node import Node
from include.game.board import Board
from include.game.piece import Piece

MOVES = [DOWN, LEFT, RIGHT]

def _visited(piece, visited):
    return piece.state in visited

def get_all_moves(piece:Piece, board:Board):
    parent_node = Node(piece=piece, parent_node=None, move=-1, rotations=0)
    queue = deque([parent_node])
    visited = set()
    candidate_moves = []
    while queue:
        node = queue.popleft()
        visited.add(node.piece.state)
        for current_move in MOVES:
            temp_piece = deepcopy(node.piece)
            temp_piece.move(current_move)
            for index in range(len(temp_piece.rotations)):
                temp_piece.move(ROTATE)
                if not _visited(temp_piece, visited):
                    if board.is_valid(temp_piece):
                        copied_temp = deepcopy(temp_piece)
                        potential_piece = Node(piece=copied_temp, parent_node=node, move=current_move, rotations=index)
                        queue.append(potential_piece)
                        visited.add(temp_piece.state)
                        if board.is_placable(temp_piece):
                            candidate_moves.append(potential_piece)
    return candidate_moves