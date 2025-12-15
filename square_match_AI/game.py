import pygame
from board import Board
from score_manager import ScoreManager
from pause_menu import PauseMenu

GRID_SIZE = 8
TILE_SIZE = 64
SCREEN_SIZE = GRID_SIZE * TILE_SIZE

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 100))
        pygame.display.set_caption("Match-3 Game")
        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.score_manager = ScoreManager()
        self.pause_menu = PauseMenu(SCREEN_SIZE)

        self.running = True
        self.paused = False
        self.game_over = False

    def run(self):
        while self.running:
            self.screen.fill((255, 255, 255))
            self.board.update()
            self.board.draw(self.screen, TILE_SIZE)

            # Score area
            pygame.draw.rect(self.screen, (200, 200, 200), (0, SCREEN_SIZE, SCREEN_SIZE, 100))
            score_text = self.font.render(f"Score: {self.score_manager.score}", True, (0, 0, 0))
            high_text = self.font.render(f"High Score: {self.score_manager.highscore}", True, (0, 0, 0))
            self.screen.blit(score_text, (20, SCREEN_SIZE + 20))
            self.screen.blit(high_text, (20, SCREEN_SIZE + 50))

            if self.game_over:
                msg = "You Win!" if self.board.check_win() else "Game Over!"
                restart_text = self.font.render(f"{msg} Press R to Restart", True, (255, 0, 0))
                self.screen.blit(restart_text, (SCREEN_SIZE // 4, SCREEN_SIZE + 20))

            if self.paused and not self.game_over:
                self.pause_menu.draw(self.screen, self.font, SCREEN_SIZE)

            # --- Event Handling ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.paused and not self.game_over:
                        if self.pause_menu.resume_button.collidepoint(x, y):
                            self.paused = False
                        elif self.pause_menu.quit_button.collidepoint(x, y):
                            self.running = False
                    elif not self.game_over and not self.paused and y < SCREEN_SIZE:
                        r, c = y // TILE_SIZE, x // TILE_SIZE
                        if self.board.selected:
                            # Swap and check for matches
                            self.board.swap(self.board.selected, (r, c))
                            matched = self.board.find_matches()
                            if matched:
                                self.board.remove_matches(matched)
                                self.score_manager.add_points(matched)
                            self.board.selected = None
                        else:
                            self.board.selected = (r, c)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and not self.game_over:
                        self.paused = not self.paused
                    elif event.key == pygame.K_r and self.game_over:
                        self.__init__()

            # --- Win/Lose Check ---
            if not self.game_over and not self.paused:
                if self.board.check_win() or self.board.check_game_over():
                    self.game_over = True

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()