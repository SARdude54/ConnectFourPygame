import pygame
import sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((900, 800))
pygame.display.set_caption("Connect Four")

running = True
clicked = False
turn = 1
# TODO Work on who's turn it is

COL = 7
ROW = 6

RADIUS = 38

game_board = [[{
    "cord": [c, r],
    "pos_cord": [r * 100 + 150, c * 100 + 151],
    "value": 0
} for r in range(0, ROW + 1)] for c in range(0, COL + 1)]


def draw_board(screen: pygame.Surface, board: list[list[dict]]):
    """
    Renders the board on the window
    :param screen: pygame.Surface
    :param board: list[list[dict]]
    :return: None
    """
    screen.fill((0, 0, 0))
    pygame.display.set_caption(str(clock.get_fps()))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(100, 100, 700, 600))

    for r in range(0, ROW):
        for c in range(0, COL):
            if board[r][c]["value"] == 0:
                pygame.draw.circle(screen, (0, 0, 0), board[r][c]["pos_cord"], RADIUS)
            if board[r][c]["value"] == 1:
                pygame.draw.circle(screen, (255, 0, 0), board[r][c]["pos_cord"], RADIUS)
            if board[r][c]["value"] == 2:
                pygame.draw.circle(screen, (255, 255, 0), board[r][c]["pos_cord"], RADIUS)


def get_available_positions(board: list[list[dict]]):
    """
    gets available spots on the board
    :param board: pygame.Surface
    :return: list[dict]
    """
    available_positions = []

    def get_pos_from_col(col: int):
        """
        private function that checks each column of the board
        :param col: int
        :return: dict
        """
        position = None
        for r in range(ROW - 1, -1, -1):
            if board[r][col]["value"] == 0:
                position = board[r][col]
                break
        return position

    for c in range(0, COL):
        if get_pos_from_col(c) is not None:
            available_positions.append(get_pos_from_col(c))

    return available_positions


def get_col_clicked(x):
    for c in range(0, COL):
        if game_board[0][c]["pos_cord"][0] - RADIUS <= x <= game_board[0][c]["pos_cord"][0] + RADIUS:
            return c


def get_available_pos_col(col):
    for r in range(ROW - 1, -1, -1):
        if game_board[r][col]["value"] == 0:
            return game_board[r][col]


if __name__ == "__main__":
    while running:
        draw_board(window, game_board)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                clicked = True
                print(get_available_pos_col(get_col_clicked(mx)))

            if event.type == MOUSEBUTTONUP:
                clicked = False

            if event.type == KEYDOWN:
                if event.key == K_e:
                    print(get_available_positions(game_board))

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
