import pygame
import sys

pygame.init()

GRID_SIZE_X = 50
GRID_SIZE_Y = 50
CELL_SIZE = 20

GRID = [[0 for _ in range(GRID_SIZE_Y)] for _ in range(GRID_SIZE_X)]

board = pygame.display.set_mode([GRID_SIZE_X * CELL_SIZE, GRID_SIZE_Y * CELL_SIZE])
pygame.display.set_caption("Conway's game of life")
timer = pygame.time.Clock()
fps = 30
game_running = True

def draw():
    board.fill((0, 0, 0))
    for row in range(GRID_SIZE_X):
        for col in range(GRID_SIZE_Y):
            if GRID[row][col] == 0:
                pygame.draw.rect(board, (255, 255, 255), (row * CELL_SIZE + 1, col * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))
            else:
                pygame.draw.rect(board, (255, 0, 0), (row * CELL_SIZE + 1, col * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))

def update_cell(row, column):
    if GRID[row][column] == 0:
        GRID[row][column] = 1
    else:
        GRID[row][column] = 0

    pygame.display.flip()

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
                row = mouse_x // CELL_SIZE
                column = mouse_y // CELL_SIZE
                update_cell(row, column)

        draw()
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()
    sys.exit()
except Exception as e:
    print(e)