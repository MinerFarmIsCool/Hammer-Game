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

        self.player = game_classes.Player(450, 450, 100, 100)
        self.game_level = level.Level()

    def init_sprite_groups(self):
        player_sprite = pygame.sprite.Group(self.player)
        enemy_sprite = pygame.sprite.Group(self.game_level.little_fuck_stupid)
        return player_sprite, enemy_sprite