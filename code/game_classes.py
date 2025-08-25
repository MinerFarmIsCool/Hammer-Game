import pygame
import sys
import random
import math

import game
import level

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        
        self.image = pygame.image.load("assets/the gurt.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def movement_update(self):
        pass