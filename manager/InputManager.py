from entities import Player, Action
from components import SpriteRendererComponent
import pygame

class InputManager:
    def __init__(self):
        pass

    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #

    def get_input(self, player: Player, current_actions: list, event: pygame.event):
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
                            action.on_click(player)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                return "skip"
            
        # Ajoutez ici l'input pour enclencher la sauvegarde
                
