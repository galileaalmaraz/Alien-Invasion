class GameStats:
    """Track statistics for Alien Invasion."""

    MIN_HARD_LEVEL = 2

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        # A timer that will be responsible for creating asteroids on a specific time interval
        self.asteroids_timer = None

        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 2
        self.close_asteroids_timer()

    def close_asteroids_timer(self):
        if self.asteroids_timer is not None:
            self.asteroids_timer.stop()
            self.asteroids_timer = None

    def set_asteroids_timer(self, timer):
        self.asteroids_timer = timer