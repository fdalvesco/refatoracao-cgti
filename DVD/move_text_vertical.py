from move_text import MoveText
import random
import pygame
from config import (
    UP, BOTTOM, LEFT, RIGHT
)

class MoveTextVertical(MoveText):
    """
    Classe que move o texto apenas na direção vertical.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """
        Inicializa o texto animado com movimento vertical.

        """
        super().__init__(text, font_size, initial_color, screen_width, screen_height)

    def update(self):
        """
        Atualiza a posição vertical do texto, invertendo a direção ao atingir as bordas da tela.
        """
        self.rect.x += self.speed_x
        self.rect.y = 0
        toctoc = pygame.mixer.Sound("grito.mp3")
              
        if self.rect.left <= 0:
            """
            Inverte a direção do movimento ao atingir a borda esquerda da tela.
            """
            self.speed_x = random.randint(0, 1)
            self._change_color()
            toctoc.play()

        if self.rect.right >= self.screen_width:
            """
            Inverte a direção do movimento ao atingir a borda direita da tela.
            """
            self.speed_x = random.randint(-1, 0)
            self._change_color()
            toctoc.play()