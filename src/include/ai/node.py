from controls import DOWN

class Node:
    def __init__(self, piece=None, parent_node=None, move=DOWN, rotations=0):
        self.parent_node = parent_node
        self.piece = piece
