import pygame
import random
from config import (
    UP, BOTTOM, LEFT, RIGHT
)

class MoveText:
    """
    Classe responsável por animar o movimento de um texto na tela, mudando de cor ao atingir as bordas.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """
        Inicializa o objeto de texto.
        """
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center=(screen_width / 2, screen_height / 2))
        
        self.speed_x = random.choice([-1, 1])
        self.speed_y = random.choice([-1, 1])
        
        self.last_quick_time = pygame.time.get_ticks()
        
        self.screen_width = screen_width
        self.screen_height = screen_height

    def _change_color(self):
        """
        Altera a cor do texto de forma aleatória.
        """
        self.color = (
            random.choice([10, 255]),
            random.choice([10, 255]),
            random.choice([10, 255]),
        )
        self.text_surf = self.font.render(self.text, True, self.color)

    def update(self):
        """
        Atualiza a posição do texto e inverte a direção ao atingir as bordas e solta um grito ao bater nas bordas.
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

    def draw(self, screen):
        """
        Desenha o texto na tela.
        """
        screen.blit(self.text_surf, self.rect)

