import numpy as np
from include.ai.features import Features
from functools import cache

MAX_LINES_CLEARED = 4

@cache
def get_max_wells(board):
    max_wells = (board.width * board.height) / 2
    return max_wells

@cache
def get_max_bumpiness(board):
    max_bumpiness = board.height * (board.width -1)
    return max_bumpiness

@cache
def get_max_holes(board):
    max_holes = board.width * (board.height -1)
    return max_holes

@cache
def get_max_aggregate_height(board):
    max_aggregate_height = (board.width * board.height) - 1
    return max_aggregate_height

@cache
def get_max_lines_cleared(board):
    return MAX_LINES_CLEARED

NORMALISATION_MAP = {
    Features.WELLS: get_max_wells,
    Features.BUMPINESS: get_max_bumpiness,
    Features.HOLES: get_max_holes,
    Features.AGGREGATE_HEIGHT: get_max_aggregate_height,
    Features.LINES_CLEARED: get_max_lines_cleared
}

def get_column_heights(board):
    max_height = board.height
    board_matrix = board.board
    filled_squares = np.equal(board_matrix, 1)
    column_heights = filled_squares.argmax(axis=0)
    return np.where(filled_squares.any(axis=0), max_height - column_heights, 0)

def get_wells(board):
    column_heights = get_column_heights(board)
    r_column_height = np.roll(column_heights, 1)
    l_column_heights = np.roll(column_heights, -1)
    l_column_heights[0] = board.height
    r_column_height[-1] = board.height
    wells = np.minimum(np.maximum(column_heights - l_column_heights, 0), np.maximum(column_heights - r_column_height, 0))
    wells = wells.sum()
    return wells

def get_bumpiness(board):
    column_heights = get_column_heights(board)
    diffs = np.abs(np.diff(column_heights))
    bumpiness = sum(diffs)
    return bumpiness

def get_holes(board):
    board_matrix = board.board
    column_heights = get_column_heights(board)
    filled = np.equal(board_matrix, 1)
    holes = int(column_heights.sum() - filled.sum())
    return holes

def get_aggregate_height(board):
    column_heights = get_column_heights(board)
    aggregate_height = sum(column_heights)
    return aggregate_height

def get_lines_cleared(board):
    return board.lines_cleared

FEATURES_MAP = {
    Features.WELLS: get_wells,
    Features.BUMPINESS: get_bumpiness,
    Features.HOLES: get_holes,
    Features.AGGREGATE_HEIGHT: get_aggregate_height,
    Features.LINES_CLEARED: get_lines_cleared
}

def get_features(params, board):
    return [(FEATURES_MAP[param](board) / NORMALISATION_MAP[param](board)) for param in params]
