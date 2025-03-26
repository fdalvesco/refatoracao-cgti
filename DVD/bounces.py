from move_text import MoveText
import random
import pygame
from config import (
    UP, BOTTOM, LEFT, RIGHT
)

class Bounces(MoveText):
    """
    Classe responsável por mover um texto na tela, fazendo-o quicar
    nas bordas da tela e alterar sua cor ao colidir e após 10 segundos, 
    reposiciona de forma aleatória na tela o texto.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """
        Inicializa o objeto Bounces.
        """
        super().__init__(text, font_size, initial_color, screen_width, screen_height)

    def update(self):
        """
        Atualiza a posição do texto na tela, fazendo-o quicar
        ao atingir as bordas e alterando sua cor ao colidir e 
        soltando o som de grito ao colidir com as bordas.
        """
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        toctoc = pygame.mixer.Sound("grito.mp3")

        if self.rect.left <= 0:
            self.speed_x = random.choice(UP)
            self.speed_y = random.choice(LEFT)
            self._change_color()
            toctoc.play()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.choice(BOTTOM)
            self.speed_y = random.choice(RIGHT)
            self._change_color()
            toctoc.play()

        if self.rect.top <= 0:
            self.speed_x = random.choice(LEFT)
            self.speed_y = random.choice(UP)
            self._change_color()
            toctoc.play()

        if self.rect.bottom >= self.screen_height:
            self.speed_x = random.choice(LEFT)
            self.speed_y = random.choice(BOTTOM)
            self._change_color()
            toctoc.play()
        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_quick_time >= 10000:
            """
            A cada 10 segundos, reposiciona aleatoriamente o texto na tela.
            """
            self.rect.x = random.randint(0, self.screen_width - self.rect.width)
            self.rect.y = random.randint(0, self.screen_height - self.rect.height)
            self.last_quick_time = current_time


