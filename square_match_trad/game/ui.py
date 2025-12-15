import pygame

WHITE = (255, 255, 255)
GRID_LINE_COLOR = (200, 200, 200)
COLOR_MAP = {
    1: "#56B4E9",
    2: "#D55E00",
    3: "#009E73"
}

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def draw_board(screen, board, cell_size):
    screen.fill(WHITE)
    for row in range(board.size):
        for col in range(board.size):
            tile = board.grid[row][col]
            if not tile.is_empty:
                color = hex_to_rgb(COLOR_MAP.get(tile.color_id, "#000000"))
                pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    for i in range(board.size + 1):
        pygame.draw.line(screen, GRID_LINE_COLOR, (0, i * cell_size), (board.size * cell_size, i * cell_size))
        pygame.draw.line(screen, GRID_LINE_COLOR, (i * cell_size, 0), (i * cell_size, board.size * cell_size))

def draw_game_over(screen, result, width, height):
    font = pygame.font.SysFont(None, 36)
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    text = font.render(result, True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 60))

    button_text = font.render("Restart", True, WHITE)
    button_rect = pygame.Rect(width // 2 - 60, height // 2, 120, 40)
    pygame.draw.rect(screen, (100, 100, 255), button_rect)
    screen.blit(button_text, (button_rect.x + 15, button_rect.y + 5))
    return button_rect

def draw_score(screen, score, high_score):
    font = pygame.font.SysFont(None, 28)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    high_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(high_text, (10, 40))

def draw_paused(screen, width, height):
    font = pygame.font.SysFont(None, 48)
    text = font.render("Paused", True, (0, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 24))