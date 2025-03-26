import pygame
import random
from config import (
    UP, BOTTOM, LEFT, RIGHT
)

class MoveText:
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(
            center=(screen_width / 2, screen_height / 2)
        )

        self.speed_x = self._non_zero()
        self.speed_y = self._non_zero()

        self.screen_width = screen_width
        self.screen_height = screen_height

    def _non_zero(self):
        speed = 0
        while speed == 0:
            speed = random.randint(-1, 1)

        return speed

    def _change_color(self):

        self.color_random = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        self.color = self.color_random
        self.text_surf = self.font.render(self.text, True, self.color)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.speed_x = random.randint(UP)
            self.speed_y = random.randint(LEFT)
            self._change_color()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(BOTTOM)
            self.speed_y = random.randint(RIGHT)
            self._change_color()

        if self.rect.top <= 0:
            self.speed_x = random.randint(LEFT)
            self.speed_y = random.randint(UP)
            self._change_color()

        if self.rect.bottom >= self.screen_height:
            self.speed_x = random.randint(LEFT)
            self.speed_y = random.randint(BOTTOM)
            self._change_color()

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)