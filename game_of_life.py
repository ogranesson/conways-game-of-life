import pygame
import sys

pygame.init()

grid_size_x = 50          # no. of columns
grid_size_y = 50          # no. of rows
CELL_SIZE = 20

GRID = [[0 for _ in range(grid_size_y)] for _ in range(grid_size_x)]

board = pygame.display.set_mode([grid_size_x * CELL_SIZE, grid_size_y * CELL_SIZE])
pygame.display.set_caption("Conway's Game of Life")
timer = pygame.time.Clock()
fps = 30
game_running = True

def draw():
    board.fill((0, 0, 0))
    for row in range(grid_size_y):
        for col in range(grid_size_x):
            if GRID[row][col] == 0:
                pygame.draw.rect(board, (255, 255, 255), (col * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))
            else:
                pygame.draw.rect(board, (255, 0, 0), (col * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))

def update_cell(row, column):
    if GRID[row][column] == 0:
        GRID[row][column] = 1
    else:
        GRID[row][column] = 0

try:
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // CELL_SIZE
                column = mouse_x // CELL_SIZE
                update_cell(row, column)

        draw()
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()
    sys.exit()
except Exception as e:
    print(e)