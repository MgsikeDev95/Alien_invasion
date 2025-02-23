import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe para gerenciar os projéteis disparados pela nave."""

    def __init__(self, ai_game):
        """Cria um projétil na posição da nave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria um projétil na posição da nave
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move o projétil para cima."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
