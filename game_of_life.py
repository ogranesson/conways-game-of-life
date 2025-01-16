import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 800
SQUARE = 15

X = 400
Y = 400

board = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Conway's game of life")
timer = pygame.time.Clock()
fps = 30
game_running = True

def draw():
    board.fill((0, 0, 0))
    pygame.draw.rect(board, (255, 0, 0), (X, Y, SQUARE, SQUARE))

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