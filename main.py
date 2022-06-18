import pygame
import sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((900, 800))

running = True

board = [[0 for c in range(0, 7)] for r in range(0, 6)]


def draw_board(screen):
    screen.fill((0, 0, 0))
    pygame.display.set_caption(str(clock.get_fps()))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(100, 100, 700, 600))


print(board)

if __name__ == "__main__":
    while running:
        draw_board(window)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
