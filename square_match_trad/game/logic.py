from .board import Board
import os

class GameLogic:
    def __init__(self, board):
        self.board = board
        self.selected = None
        self.game_over = False
        self.result = ""
        self.score = 0
        self.paused = False

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0
    
    def save_high_score(self):
        high_score = self.load_high_score()
        if self.score > high_score:
            with open("highscore.txt", "w") as f:
                f.write(str(self.score))

    def handle_click(self, row, col):
        if self.selected is None:
            self.selected = (row, col)
        else:
            self.board.swap(self.selected, (row, col))
            self.selected = None

    def update(self):
        if self.game_over or self.paused:
            return

        matches = self.board.detect_matches()
        if matches:
            # Count how many tiles are matched
            match_count = len(matches)
            # Base score: 10 pts per tile
            base = match_count * 10
            # Bonus: +5 pts per tile beyond 3
            bonus = max(0, match_count - 3) * 5

            self.score += base + bonus
            self.board.clear_matches(matches)

        self.check_game_end()
        
    def check_game_end(self):
        if self.board.is_empty():
            self.result = "You Win!"
            self.game_over = True
            self.save_high_score()
        elif not self.board.has_possible_match():
            self.result = "No More Matches. You Lose!"
            self.game_over = True
            self.save_high_score()

    def restart(self):
        self.selected = None
        self.game_over = False
        self.result = ""
        self.score = 0  # ✅ Reset score here
        self.board.generate_valid_grid()

    def toggle_pause(self):
        self.paused = not self.paused

    