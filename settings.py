class Settings:
    """Uma classe para armazenar todas as configurações do jogo Alien Invasion."""

    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)  # Fundo preto

        # Configurações da nave
        self.ship_speed = 1.5  # Velocidade inicial da nave
        self.ship_limit = 3  # Número de vidas do jogador

        # Configurações dos projéteis
        self.bullet_speed = 1.5  # Velocidade inicial dos projéteis
        self.bullet_width = 3  # Largura do projétil
        self.bullet_height = 15  # Altura do projétil
        self.bullet_color = (255, 0, 0)  # Cor das balas (vermelho)
        self.bullet_allowed = 9  # Número máximo de projéteis na tela

        # Configurações dos alienígenas
        self.alien_speed = 1.0  # Velocidade inicial dos alienígenas
        self.fleet_drop_speed = 10  # Velocidade de descida da frota
        self.fleet_direction = 1  # 1 representa direita; -1 representa esquerda.

        # Configuração de pontuação
        self.alien_points = 50  # Pontos por alienígena destruído

        # Fatores de escala
        self.speedup_scale = 1.1  # Fator de aumento de velocidade
        self.score_scale = 1.5  # Fator de aumento da pontuação

    def initialize_dynamic_settings(self, difficulty='medium'):
        """Inicializa as configurações que mudam durante o jogo."""
        if difficulty == 'easy':
            # Fácil: Mais rápido (como o Médio atual)
            self.ship_speed = 3.0  # Aumenta a velocidade da nave
            self.bullet_speed = 2.0  # Aumenta a velocidade dos projéteis
            self.alien_speed = 1.0  # Aumenta a velocidade dos alienígenas
        elif difficulty == 'medium':
            # Médio: Mais difícil (como o Difícil atual)
            self.ship_speed = 4.5  # Aumenta a velocidade da nave
            self.bullet_speed = 2.5  # Aumenta a velocidade dos projéteis
            self.alien_speed = 1.5  # Aumenta a velocidade dos alienígenas
        elif difficulty == 'hard':
            # Difícil: Ainda mais difícil
            self.ship_speed = 5.5  # Aumenta a velocidade da nave
            self.bullet_speed = 3.0  # Aumenta a velocidade dos projéteis
            self.alien_speed = 2.0  # Aumenta a velocidade dos alienígenas

    def increase_speed(self):
        """Aumenta as configurações de velocidade."""
        self.ship_speed *= self.speedup_scale  # Aumenta a velocidade da nave
        self.bullet_speed *= self.speedup_scale  # Aumenta a velocidade dos projéteis
        self.alien_speed *= self.speedup_scale  # Aumenta a velocidade dos alienígenas

    def increase_score(self):
        """Aumenta os pontos por alienígena destruído."""
        self.alien_points = int(self.alien_points * self.score_scale)  # Aumenta a pontuação por alienígena