# Alien Invasion



Alien Invasion é um jogo clássico de invasão alienígena desenvolvido em Python usando a biblioteca Pygame. O objetivo do jogo é destruir ondas de aliens enquanto protege sua nave de ataques inimigos.

---
asso 1: Acesse o Repositório no GitHub
Abra o seu navegador e vá para o endereço do repositório: https://github.com/MgsikeDev95/Alien_invasion/.

Passo 2: Baixe o Código-Fonte
No repositório, clique no botão verde "Code" (Código) no canto superior direito da página.

No menu que aparece, selecione "Download ZIP". Isso fará o download de um arquivo ZIP contendo todo o código-fonte do jogo.

Passo 3: Extraia o Arquivo ZIP
Após o download, localize o arquivo ZIP no seu computador (geralmente na pasta "Downloads").

Clique com o botão direito no arquivo ZIP e selecione "Extrair Tudo" (ou algo similar, dependendo do seu sistema operacional).

Escolha um local para extrair os arquivos e clique em "Extrair".

Passo 4: Instale o Python

 Você pode baixá-lo em [python.org](https://www.python.org/).

Além disso, instale a biblioteca Pygame:

```bash
pip install pygame

Passo 5: Instale as Dependências
Abra o terminal ou prompt de comando no seu computador.

Navegue até a pasta onde você extraiu os arquivos do jogo. Por exemplo, se você extraiu os arquivos para a pasta Downloads/Alien_invasion, você pode usar o comando:

bash
Copy
cd Downloads/Alien_invasion

Passo 6: Execute o Jogo
Após instalar as dependências, você pode executar o jogo. Procure pelo arquivo principal do jogo, que geralmente tem um nome alien_invasion.py.

Execute o arquivo usando o Python:


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
