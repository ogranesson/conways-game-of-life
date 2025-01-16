import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 800
SQUARE = 15

board = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Conway's game of life")
timer = pygame.time.Clock()
fps = 30
game_running = True

try:
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        board.fill((0, 0, 0))

        pygame.draw.rect(board, (255, 0, 0), (WIDTH // 2, HEIGHT // 2, SQUARE, SQUARE))

        pygame.display.flip()

        timer.tick(fps)

    pygame.quit()
    sys.exit()
except Exception as e:
    print(e)