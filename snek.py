import pygame

pygame.init()

GRID_SIZE_X = 50          # no. of columns
GRID_SIZE_Y = 50          # no. of rows
CELL_SIZE = 10

board = pygame.display.set_mode([GRID_SIZE_X * CELL_SIZE, GRID_SIZE_Y * CELL_SIZE])
pygame.display.set_caption("Conway's Game of Life")
timer = pygame.time.Clock()
fps = 30
game_running = True