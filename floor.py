import pygame
from setting import WIDTH, HEIGHT

class Floor:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("assets/floor.png"), (WIDTH, 168))
        self.x_pos = 0

    def move(self):
        self.x_pos -= 1
        if self.x_pos <= -WIDTH:
            self.x_pos = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, HEIGHT - 100))
        screen.blit(self.image, (self.x_pos + WIDTH, HEIGHT - 100))
