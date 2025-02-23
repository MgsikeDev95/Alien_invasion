import pygame.font

class Button:
    """Classe para criar botões para o game."""

    def __init__(self, ai_game, msg, position=None):
        """Inicializa os atributos do botão."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()  # Corrigido: self.screen_rect

        # Define dimensões e propriedades do botão
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Cria o objeto rect (retângulo) do botão
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Define a posição do botão
        if position is None:
            # Se nenhuma posição for fornecida, centraliza o botão
            self.rect.center = self.screen_rect.center
        else:
            # Usa a posição personalizada fornecida
            self.rect.center = position

        # A mensagem do botão precisa ser preparada apenas uma vez
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transforma msg em uma imagem renderizada e centraliza o texto no botão."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Desenha o botão em branco e depois desenha a mensagem."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)