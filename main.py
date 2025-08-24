import pygame
import sys
import random
import math

import game_classes
import level
from game import Game


pygame.init()

def main():
    game = Game()

    gaming_running = True
    player_sprite = game.init_sprite_groups()

    while gaming_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        

        game.screen.fill("white")

        player_sprite.draw(game.screen)

        pygame.display.flip()
        game.clock.tick(game.FPS)

if __name__ == "__main__":
    main()