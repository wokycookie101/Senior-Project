class Tile:
    def __init__(self, color_id):
        self.color_id = color_id  # 1, 2, 3, etc.
        self.is_empty = color_id == 0

    def clear(self):
        self.color_id = 0
        self.is_empty = True

    def is_matchable_with(self, other):
        return (
            not self.is_empty and
            other is not None and
            not other.is_empty and
            self.color_id == other.color_id
        )