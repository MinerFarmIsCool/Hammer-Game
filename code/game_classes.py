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
        
        self._speed = 10
        self.image = pygame.image.load("assets/the gurt.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self._stats = {
            "health": 10,
            "attack": 5,
            "defense": 2
        }
        
    def movement_update(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self._speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self._speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self._speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self._speed

        return self.rect.x, self.rect.y
    
    def get_pos(self):
        return self.rect.x, self.rect.y
    
    def get_stats(self):
        return self._stats
    
    def die(self):
        pygame.quit()
        sys.exit()

    def get_hit(self, enemy):
        enemy_stats = enemy.get_stats()
        damage = enemy_stats["attack"] - self._stats["defense"]
        self._stats["health"] -= damage
        return self._stats["health"]
    
    def attack(self, enemy):
        enemy_stats = enemy.get_stats()
        damage = self._stats["attack"] - enemy_stats["defense"]
        enemy_stats["health"] -= damage
        return enemy_stats["health"]
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, type = "basic"):
        super().__init__()

        self.speed = 5
        self.image = pygame.image.load("assets/Hammer Game Enemy Basic.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self._stats = {
            "health": 5,
            "attack": 5,
            "defense": 1
        }

    def movement(self, player):

        player_x, player_y = player.get_pos()

        if self.rect.x != player_x:
            if self.rect.x > player_x:
                self.rect.x -= self.speed
            if self.rect.x < player_x:
                self.rect.x += self.speed

        if self.rect.y != player_y:
            if self.rect.y > player_y:
                self.rect.y -= self.speed
            if self.rect.y < player_y:
                self.rect.y += self.speed

        return self.rect.x, self.rect.y
    
    def get_stats(self):
        return self._stats
        
class Weapons():
    def __init__(self):
        pass