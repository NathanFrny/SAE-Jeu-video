from entities import Player
from components import SpriteRendererComponent, TransformComponent
from tiles import Tile
import pygame

class InputManager:
    def __init__(self):
        pass

    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #

    def get_input(self, player: Player, current_actions: list, grid: list, event: pygame.event):
        """ Get the input of the player.

        Args:
            player (Player): The player who is playing
        """
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left mouse button
            mouse_pos = pygame.mouse.get_pos()

            sprite_renderer = player.get_component(SpriteRendererComponent)
            if sprite_renderer:
                player_rect = sprite_renderer.sprite.rect

                if player_rect.collidepoint(mouse_pos):
                    return "getAllActions"
                
            if current_actions:
                for action in current_actions:
                    sprite_renderer = action.get_component(SpriteRendererComponent)
                    if sprite_renderer:
                        action_rect = sprite_renderer.sprite.rect
                        if action_rect.collidepoint(mouse_pos):
                            position = player.get_component(TransformComponent).position
                            action.on_click(player)
                            if (player.get_component(TransformComponent).position != position):
                                grid[position[0]][position[1]].entity = None
                                grid[player.get_component(TransformComponent).position[0]][player.get_component(TransformComponent).position[1]].entity = player
                            print('----------')
                            for row in grid:
                                for tile in row:
                                    if tile.entity != None:
                                        print(grid.index(row), row.index(tile))
                            current_actions.clear()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                return "skip"
            
        # Ajoutez ici l'input pour enclencher la sauvegarde
                
