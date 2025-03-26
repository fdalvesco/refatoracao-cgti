from move_text import MoveText
import random
import pygame
from config import (
    UP, BOTTOM, LEFT, RIGHT
)

class MoveTextHorizontal(MoveText):
    """
    Classe que move o texto apenas na direção horizontal.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """
        Inicializa o texto animado com movimento horizontal.  
        """
        super().__init__(text, font_size, initial_color, screen_width, screen_height)

    def update(self):
        """
        Atualiza a posição horizontal do texto, invertendo a direção ao atingir as bordas da tela.
        """
        self.rect.x = 0
        self.rect.y += self.speed_y
        toctoc = pygame.mixer.Sound("grito.mp3")
        
        if self.rect.top <= 0:
            """
            Inverte a direção do movimento ao atingir a parte superior da tela.
            """
            self.speed_y = random.randint(0, 1)
            self._change_color()
            toctoc.play()

        if self.rect.bottom >= self.screen_height:
            """
            Inverte a direção do movimento ao atingir a parte inferior da tela.
            """
            self.speed_y = random.randint(-1, 0)
            self._change_color()
            toctoc.play()