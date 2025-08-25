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
    player_sprite, enemy_sprite = game.init_sprite_groups()


    while gaming_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        #Game Logic
        game_classes.Player.movement_update(game.player)
        game.game_level.little_fuck_stupid.movement(game.player)
        
        #Drawing stuff
        game.screen.fill("purple")

        player_sprite.draw(game.screen)
        enemy_sprite.draw(game.screen)

        pygame.display.flip()
        game.clock.tick(game.FPS)

if __name__ == "__main__":
    main()