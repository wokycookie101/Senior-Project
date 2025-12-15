import pygame
import time
from game import Board
from game import GameLogic
from game.ui import draw_board, draw_game_over, draw_score, draw_paused

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Strategic Match")

# Initialize game modules
board = Board(size=GRID_SIZE)
logic = GameLogic(board)

# Main loop
running = True
restart_button = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                logic.toggle_pause()

        if logic.game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button and restart_button.collidepoint(event.pos):
                    logic.restart()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // CELL_SIZE
                row = event.pos[1] // CELL_SIZE
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    logic.handle_click(row, col)

    # Draw game
    draw_board(screen, board, CELL_SIZE)
    draw_score(screen, logic.score, logic.load_high_score())

    if logic.paused:
        draw_paused(screen, WIDTH, HEIGHT)

    if not logic.game_over and not logic.paused:
        logic.update()
    else:
        restart_button = draw_game_over(screen, logic.result, WIDTH, HEIGHT)

    pygame.display.flip()

pygame.quit()