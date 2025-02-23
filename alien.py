import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that represents an alien in the fleet."""

    def __init__(self, ai_game):
        """Initializes the alien and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and defines rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Starts each new alien near the top-left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Stores the alien's horizontal position.
        self.x =float(self.rect.x)

    def check_edges(self):
        """Return true if the alien is on the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """moves the alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        