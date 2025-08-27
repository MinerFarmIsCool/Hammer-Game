import pygame
import sys
import random
import math

import game_classes
import level
from game import Game


pygame.init()

def game_loop():
    game = Game()

    gaming_running = True
    player_sprite, enemy_sprite = game.init_sprite_groups()

    main_font = pygame.font.SysFont("comisans", 40)


    while gaming_running:

        game.frame_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        #Game Logic
        game_classes.Player.movement_update(game.player)
        game.game_level.little_fuck_stupid.movement(game.player)
        
        if pygame.Rect.colliderect(game.player.rect, game.game_level.little_fuck_stupid.rect) and game.frame_count % 20 == 0:
            game.player.get_hit(game.game_level.little_fuck_stupid)

        if game.player.get_stats()["health"] < 0:
            game.player.die()

        #Drawing stuff
        game.screen.fill("purple")

        player_sprite.draw(game.screen)
        enemy_sprite.draw(game.screen)

        #Display text
        player_health = game.player.get_stats()["health"]
        player_health_text = main_font.render(f"Health: {player_health}", True, (0, 0, 0))
        game.screen.blit(player_health_text, (900, 400))

        pygame.display.flip()
        game.clock.tick(game.FPS)

if __name__ == "__main__":
    game_loop()