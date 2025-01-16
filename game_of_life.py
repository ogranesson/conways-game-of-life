import pygame
import sys

pygame.init()

GRID_SIZE_X = 50
GRID_SIZE_Y = 50
CELL_SIZE = 20

board = pygame.display.set_mode([GRID_SIZE_X * CELL_SIZE, GRID_SIZE_Y * CELL_SIZE])
pygame.display.set_caption("Conway's game of life")
timer = pygame.time.Clock()
fps = 30
game_running = True

def draw():
    board.fill((0, 0, 0))
    for i in range(0, GRID_SIZE_Y * CELL_SIZE, CELL_SIZE):
        for j in range(0, GRID_SIZE_X * CELL_SIZE, CELL_SIZE):
            pygame.draw.rect(board, (255, 255, 255), (i + 1, j + 1, CELL_SIZE - 1, CELL_SIZE - 1))

def move():
    global X
    global Y

    X += 10
    Y += 10

    board.fill((0, 0, 0))
    pygame.draw.rect(board, (255, 0, 0), (X, Y, SQUARE, SQUARE))

try:
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    move()
                    pygame.display.flip()

        draw()
        pygame.display.flip()
        timer.tick(fps)

    pygame.quit()
    sys.exit()
except Exception as e:
    print(e)