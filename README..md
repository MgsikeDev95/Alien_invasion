# Alien Invasion



Alien Invasion é um jogo clássico de invasão alienígena desenvolvido em Python usando a biblioteca Pygame. O objetivo do jogo é destruir ondas de aliens enquanto protege sua nave de ataques inimigos.

---

 Como Executar

Siga estas instruções para rodar o jogo no seu computador.

 Pré-requisitos

Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/).

Além disso, instale a biblioteca Pygame:

```bash
pip install pygame

Passos para Executar o Jogo
Clone este repositório:

bash
Copy
git clone https://github.com/seu-usuario/alien-invasion.git
Navegue até a pasta do projeto:

bash
Copy
cd alien-invasion
Execute o jogo:

bash
Copy
python alien_invasion.py
Como Jogar
Movimentação: Use as setas do teclado (← → ↑ ↓) para mover a nave.

Atirar: Pressione a barra de espaço para disparar projéteis.

Objetivo: Destrua todos os aliens antes que eles cheguem à parte inferior da tela.


O projeto está organizado da seguinte forma:

Copy
alien-invasion/
├── alien_invasion.py       # Arquivo principal do jogo
├── settings.py             # Configurações do jogo
├── ship.py                 # Classe da nave do jogador
├── bullet.py               # Classe dos projéteis
├── alien.py                # Classe dos aliens
├── game_stats.py           # Controle de estatísticas do jogo
├── scoreboard.py           # Exibição da pontuação e vidas
├── button.py               # Botões para o menu do jogo
├── images/                 # Pasta com imagens do jogo
│   ├── ship.bmp            # Imagem da nave
│   ├── alien.bmp           # Imagem do alien
│   └── background.bmp      # Imagem de fundo (opcional)
└── README.md               # Este arquivo
Personalização
Você pode personalizar o jogo alterando os seguintes arquivos:

settings.py: Ajuste a velocidade do jogo, número de vidas, cores, etc.

images/: Substitua as imagens da nave, aliens e fundo para criar seu próprio estilo.

Vidas: Você tem um número limitado de vidas. Cuidado com os ataques dos aliens!
