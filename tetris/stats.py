class Stats:
    def __init__(self, game) -> None:
        # game = class Tetris
        self.settings = game.settings
        self.game_active = False
        # Will need to get the high_score from the db
        self.high_score = 0
        self.score = 0
        self.level = 1

    def reset_stats(self) -> None:
        self.score = 0
        self.level = 1
