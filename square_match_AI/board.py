import random
import pygame
from tile import Tile, WHITE

GRID_SIZE = 8
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

class Board:
    def __init__(self):
        self.tiles = [[Tile(random.choice(COLORS)) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected = None

    def swap(self, pos1, pos2):
        r1, c1 = pos1
        r2, c2 = pos2
        self.tiles[r1][c1], self.tiles[r2][c2] = self.tiles[r2][c2], self.tiles[r1][c1]

    def find_matches(self):
        matched = []
        # Horizontal matches
        for r in range(GRID_SIZE):
            count = 1
            for c in range(1, GRID_SIZE):
                if self.tiles[r][c].color == self.tiles[r][c-1].color and self.tiles[r][c].color != WHITE:
                    count += 1
                else:
                    if count >= 3:
                        matched.extend([(r, x) for x in range(c-count, c)])
                    count = 1
            if count >= 3:
                matched.extend([(r, x) for x in range(GRID_SIZE-count, GRID_SIZE)])

        # Vertical matches
        for c in range(GRID_SIZE):
            count = 1
            for r in range(1, GRID_SIZE):
                if self.tiles[r][c].color == self.tiles[r-1][c].color and self.tiles[r][c].color != WHITE:
                    count += 1
                else:
                    if count >= 3:
                        matched.extend([(x, c) for x in range(r-count, r)])
                    count = 1
            if count >= 3:
                matched.extend([(x, c) for x in range(GRID_SIZE-count, GRID_SIZE)])

        return matched

    def remove_matches(self, matched):
        """Start fading matched tiles to white."""
        for r, c in matched:
            self.tiles[r][c].start_fade()

    def check_win(self):
        return all(all(tile.color == WHITE for tile in row) for row in self.tiles)

    def check_game_over(self):
        counts = {color: sum(row.count(color) for row in [[t.color for t in r] for r in self.tiles]) for color in COLORS}
        return any(count in [1, 2] for count in counts.values())

    def update(self):
        for row in self.tiles:
            for tile in row:
                tile.update()

    def draw(self, screen, TILE_SIZE):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                rect = pygame.Rect(c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                self.tiles[r][c].draw(screen, rect)