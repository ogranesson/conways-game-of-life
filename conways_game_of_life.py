import pygame
import sys

pygame.init()

GRID_SIZE_X = 50          # no. of columns
GRID_SIZE_Y = 50          # no. of rows
CELL_SIZE = 20

GRID = [[0 for _ in range(GRID_SIZE_Y)] for _ in range(GRID_SIZE_X)]    # multidimensional array full of zeros
                                                                        # underscores instead of i, j because we're not using them here anyway

main_title = "Conway's Game of Life | Generations: "
generations = 0
paused_text = " | Game paused"
board = pygame.display.set_mode([GRID_SIZE_X * CELL_SIZE, GRID_SIZE_Y * CELL_SIZE])
pygame.display.set_caption(main_title + str(generations) + paused_text)
timer = pygame.time.Clock()
fps = 30
game_running = True
game_paused = True

# setting the event to be used in the interval later
STEP_EVENT = pygame.USEREVENT
TIMER_DURATION = 400

def restart():
    global generations
    global GRID
    global game_paused

    generations = 0
    GRID = [[0 for _ in range(GRID_SIZE_Y)] for _ in range(GRID_SIZE_X)]
    game_paused = True
    pygame.time.set_timer(STEP_EVENT, 0)

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

        # wraps around if out of bounds
        if r < 0:
            r = GRID_SIZE_Y - 1
        if r == GRID_SIZE_Y:
            r = 0
        if c < 0:
            c = GRID_SIZE_X - 1
        if c == GRID_SIZE_X:
            c = 0

        if 0 <= r < GRID_SIZE_Y and 0 <= c < GRID_SIZE_X:
            count += GRID[r][c]     # since boolean, adding value of cell also equals to no. of living neighbors

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
                if event.key == pygame.K_RETURN:
                    if game_paused:
                        game_paused = False
                        pygame.time.set_timer(STEP_EVENT, TIMER_DURATION)  # resume timer
                        pygame.display.set_caption(main_title + str(generations))
                    else:
                        game_paused = True
                        pygame.time.set_timer(STEP_EVENT, 0)    # stop timer
                        pygame.display.set_caption(main_title + str(generations) + paused_text)
                elif event.key == pygame.K_r:
                    restart()
                    pygame.display.set_caption(main_title + str(generations) + paused_text)
                elif event.key  == pygame.K_MINUS:
                    TIMER_DURATION += 50
                    pygame.time.set_timer(STEP_EVENT, TIMER_DURATION)
                elif event.key == pygame.K_EQUALS:
                    TIMER_DURATION -= 50
                    pygame.time.set_timer(STEP_EVENT, TIMER_DURATION)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // CELL_SIZE
                col = mouse_x // CELL_SIZE
                update_cell(row, col)
            elif event.type == pygame.USEREVENT:
                    live_or_die()
                    generations += 1
                    pygame.display.set_caption(main_title + str(generations))

        draw()
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()
    sys.exit()
except Exception as e:
    print(e)