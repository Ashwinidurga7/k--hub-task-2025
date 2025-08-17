import pygame

class Game:
    def __init__(self, goal_cell, tile):
        self.goal_cell = goal_cell
        self.tile = tile
        self.font = pygame.font.SysFont("Arial", 24)  # Font for messages
        self.win = False  # Track if the game is won

    def add_goal_point(self, screen):
        goal_color = (255, 215, 0)  # Gold
        goal_size = self.tile
        gx = self.goal_cell.x
        gy = self.goal_cell.y
        pygame.draw.rect(screen, goal_color, (gx, gy, goal_size, goal_size))

    def is_game_over(self, player):
        """Check if player reached the goal."""
        px, py = player.x, player.y
        gx, gy = self.goal_cell.x, self.goal_cell.y
        goal_size = self.tile
        if gx <= px <= gx + goal_size and gy <= py <= gy + goal_size:
            self.win = True
            return True
        return False

    def message(self):
        """Return a text surface with game status."""
        if self.win:
            return self.font.render("You Win!", True, (0, 255, 0))
        else:
            return self.font.render("Reach the goal!", True, (255, 255, 255))
