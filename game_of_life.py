import pygame
import sys

pygame.init()

GRID_SIZE_X = 50          # no. of columns
GRID_SIZE_Y = 50          # no. of rows
CELL_SIZE = 20

GRID = [[0 for _ in range(GRID_SIZE_Y)] for _ in range(GRID_SIZE_X)]    # multidimensional array full of zeros
                                                                        # underscores instead of i, j because we're not using them here anyway

board = pygame.display.set_mode([GRID_SIZE_X * CELL_SIZE, GRID_SIZE_Y * CELL_SIZE])
pygame.display.set_caption("Conway's Game of Life")
timer = pygame.time.Clock()
fps = 30
game_running = True

def draw():
    board.fill((0, 0, 0))
    for row in range(GRID_SIZE_Y):
        for col in range(GRID_SIZE_X):
            if GRID[row][col] == 0:
                pygame.draw.rect(board, (255, 255, 255), (col * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))
            else:
                pygame.draw.rect(board, (255, 0, 0), (col * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))

def update_cell(row, col):
    if GRID[row][col] == 0:
        GRID[row][col] = 1
    else:
        GRID[row][col] = 0

def count_neighbors(row, col):
    count = 0
    directions = [      # always remember direction tuples and grids in any array-based game
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for direction_r, direction_c in directions:
        r = row + direction_r
        c = col + direction_c
        if 0 <= r < GRID_SIZE_Y and 0 <= c < GRID_SIZE_X:   # keep in bounds
            count += GRID[r][c]

    return count

def live_or_die():
    #   we cannot upgrade the main grid as the game is going on since changing one value can mess up the calculation for the others
    #   thus, a temporary grid is created for calculation
    global GRID
    temp_grid = [[0 for _ in range(GRID_SIZE_Y)] for _ in range(GRID_SIZE_X)]

    for row in range(GRID_SIZE_Y):
        for col in range(GRID_SIZE_X):
            living_neighbors = count_neighbors(row, col)

            if GRID[row][col] == 1:
                if living_neighbors == 2 or living_neighbors == 3:
                    temp_grid[row][col] = 1
                else:
                    temp_grid[row][col] = 0
            else:
                if living_neighbors == 3:
                    temp_grid[row][col] = 1

    GRID = temp_grid

try:
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    live_or_die()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // CELL_SIZE
                col = mouse_x // CELL_SIZE
                update_cell(row, col)

        draw()
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()
    sys.exit()
except Exception as e:
    print(e)