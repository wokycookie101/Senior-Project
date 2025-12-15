import os

SCORE_FILE = "highscore.txt"

class ScoreManager:
    def __init__(self):
        self.score=0
        self.highscore=self.load_highscore()

    def load_highscore(self):
        if os.path.exists(SCORE_FILE):
            return int(open(SCORE_FILE).read().strip())
        return 0

    def save_highscore(self):
        open(SCORE_FILE,"w").write(str(self.highscore))

    def add_points(self, matched):
        bonus=5 if len(matched)>3 else 0
        self.score+=len(matched)*10+bonus
        if self.score>self.highscore:
            self.highscore=self.score
            self.save_highscore()