from constants import DOWN, LEFT, NO_MOVE, RIGHT, ROTATE

NODE_COST = {
    DOWN: 0,
    LEFT: 2,
    RIGHT: 2
}

class Node:
    def __init__(self, piece=None, parent_node=None, move=DOWN, rotations=0):
        self.parent_node = parent_node
        self.piece = piece
        # self.weight = ( parent_node.weight if parent_node is not None else 0 ) + NODE_COST[move]
