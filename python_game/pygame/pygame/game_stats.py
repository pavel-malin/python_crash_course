class GameStats():
    """Tracks statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initializes statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # The game starts in an inactive.
        self.game_active = False

        # Records should not be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
