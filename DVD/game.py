import sys
import pygame
from move_text import MoveText
from move_text_horizontal import MoveTextHorizontal
from move_text_vertical import MoveTextVertical
from bounces import Bounces
from config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    FPS,
    PRETO,
    VERMELHO,
    BRANCO,
    VERDE,
    AZUL,
)


class Game:
    """
    Classe principal do jogo, responsável por gerenciar eventos, atualizações e renderização.
    """
    
    def __init__(self):
        """
        Inicializa o jogo, configurando a tela, música, clock e instanciando o texto animado.
        """
        pygame.init()
        
        self.musicas = ["music1.mp3", "musica.mp3"]
        self.musica_atual = 0
        pygame.mixer.music.load(self.musicas[self.musica_atual])
        pygame.mixer.music.play(-1)
        self.musica_pausada = False

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True

        self.text = Bounces("DVD", 50, BRANCO, SCREEN_WIDTH, SCREEN_HEIGHT)

    def events(self):
        """
        Captura e processa os eventos do jogo, como teclas pressionadas e fechamento da janela.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    """
                    Pausa ou despausa a música quando a barra de espaço é pressionada.
                    """
                    if self.musica_pausada:
                        pygame.mixer.music.unpause()  
                    else:
                        pygame.mixer.music.pause()  
                    self.musica_pausada = not self.musica_pausada  
                    
                elif event.key == pygame.K_s:
                    """
                    Alterna para a próxima música na lista quando 's' é pressionado.
                    """
                    self.musica_atual = (self.musica_atual + 1) % len(self.musicas)  
                    pygame.mixer.music.load(self.musicas[self.musica_atual])
                    pygame.mixer.music.play(-1)

    def update(self):
        """
        Atualiza os elementos do jogo, como a posição do texto animado.
        """
        self.text.update()

    def draw(self):
        """
        Renderiza os elementos na tela, incluindo o fundo e o texto animado.
        """
        self.screen.fill(PRETO)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """
        Loop principal do jogo, gerenciando eventos, atualizações e renderização.
        """
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()