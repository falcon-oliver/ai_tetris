import pygame
from include.game.board import Board

FPS = 60
BACKGROUND = (0, 0, 0)
BLOCK = (0, 255, 0)
GRID = (15, 15, 15)

class Gui:
    def __init__(self, width, height, board:Board):
        pygame.init()
        self.board = board
        self.width = width
        display_info = pygame.display.Info()
        screen_height = display_info.current_h
        self.cell_size = (screen_height/2) / height
        self.side_bar_width = int(width * self.cell_size * 0.75)
        self.height = height
        self.screen = pygame.display.set_mode((width * self.cell_size, height * self.cell_size))
        pygame.display.set_caption("ai model")
        self.clock = pygame.time.Clock()
    
    def _draw_board(self):
        for y in range(self.height):
            for x in range(self.width):
                color = BLOCK if self.board.board[y, x] else BACKGROUND
                pygame.draw.rect(self.screen, color, (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, GRID, (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size), 1)
    
    def render(self):
        self._draw_board()
        self._check_quit()
        pygame.display.flip()
        self.clock.tick(FPS)

    def _check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
