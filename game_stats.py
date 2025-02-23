import json
import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset
        self.high_score_file = 'high_score.json'
        self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score from a file if it exists."""
        if os.path.exists(self.high_score_file):
            with open(self.high_score_file, 'r') as file:
                try:
                    data = json.load(file)
                    self.high_score = data.get('high_score', 0)
                except json.JSONDecodeError:
                    self.high_score = 0
        else:
            self.high_score = 0

    def save_high_score(self):
        """Save the high score to a file."""
        data = {'high_score': self.high_score}
        with open(self.high_score_file, 'w') as file:
            json.dump(data, file)