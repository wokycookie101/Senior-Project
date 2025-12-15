import random
from .tile import Tile

class Board:
    def __init__(self, size=8, colors=(1, 2, 3)):
        self.size = size
        self.colors = colors
        self.grid = []
        self.generate_valid_grid()

    def generate_valid_grid(self):
        while True:
            self.grid = [[Tile(random.choice(self.colors)) for _ in range(self.size)] for _ in range(self.size)]
            if self.has_possible_match():
                break

    def swap(self, pos1, pos2):
        r1, c1 = pos1
        r2, c2 = pos2
        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]

    def detect_matches(self):
        matches = set()
    
        # Horizontal runs
        for row in range(self.size):
            run = []
            for col in range(self.size):
                tile = self.grid[row][col]
                if run and tile.is_matchable_with(self.grid[row][run[-1]]):
                    run.append(col)
                else:
                    if len(run) >= 3:
                        matches.update({(row, c) for c in run})
                    run = [col]
            if len(run) >= 3:
                matches.update({(row, c) for c in run})
    
        # Vertical runs
        for col in range(self.size):
            run = []
            for row in range(self.size):
                tile = self.grid[row][col]
                if run and tile.is_matchable_with(self.grid[run[-1]][col]):
                    run.append(row)
                else:
                    if len(run) >= 3:
                        matches.update({(r, col) for r in run})
                    run = [row]
            if len(run) >= 3:
                matches.update({(r, col) for r in run})
    
        return matches

    def clear_matches(self, matches):
        for row, col in matches:
            self.grid[row][col].clear()

    def has_possible_match(self):
        color_counts = {color: 0 for color in self.colors}
        for row in self.grid:
            for tile in row:
                if not tile.is_empty:
                    color_counts[tile.color_id] += 1
        return any(count >= 3 for count in color_counts.values())

    def is_empty(self):
        return all(tile.is_empty for row in self.grid for tile in row)