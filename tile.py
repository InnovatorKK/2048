import pygame
from enum import Enum

class POSITION(Enum):
    ...

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, level, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.numbers = [2**i for i in range(1, 11)]
        self.POSITION = [
            [(100, 100), (250, 100), (400, 100), (550, 100)],
            [(100, 250), (250, 250), (400, 250), (550, 250)],
            [(100, 400), (250, 400), (400, 400), (550, 400)],
            [(100, 550), (250, 550), (400, 550), (550, 550)]
        ]
        
        self.image = pygame.image.load(f"img/{self.numbers[level]}.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.POSITION[x][y]
        