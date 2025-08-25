import pygame
import sys
import random
import math

import game_classes
import level

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.player = game_classes.Player(150, 150, 50, 50)

    def init_sprite_groups(self):
        player_sprite = pygame.sprite.Group(self.player)
        return player_sprite