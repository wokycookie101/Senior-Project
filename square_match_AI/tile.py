import pygame

WHITE = (255, 255, 255)

class Tile:
    def __init__(self, color):
        self.color = color
        self.fade_progress = None  # None = not fading

    def start_fade(self):
        """Begin fading this tile to white."""
        self.fade_progress = 0

    def update(self):
        """Advance fade if active."""
        if self.fade_progress is not None:
            steps = 30  # number of frames to fade
            t = self.fade_progress / steps
            # interpolate current color toward white
            r = int(self.color[0] + (255 - self.color[0]) * t)
            g = int(self.color[1] + (255 - self.color[1]) * t)
            b = int(self.color[2] + (255 - self.color[2]) * t)
            self.color = (r, g, b)

            self.fade_progress += 1
            if self.fade_progress >= steps:
                self.color = WHITE
                self.fade_progress = None

    def draw(self, screen, rect):
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)