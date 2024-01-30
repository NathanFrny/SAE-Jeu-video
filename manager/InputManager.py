from entities import Player
from components import SpriteRendererComponent
import pygame

class InputManager:
    def __init__(self):
        pass

    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #

    def get_input(self, player: Player, event: pygame.event):
        """ Get the input of the player.

        Args:
            player (Player): The player who is playing
        """
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left mouse button
            print("Mouse click")
            mouse_pos = pygame.mouse.get_pos()

            sprite_renderer = player.get_component(SpriteRendererComponent)
            if sprite_renderer:
                player_rect = sprite_renderer.sprite.rect

                if player_rect.collidepoint(mouse_pos):
                    return "getAllActions"
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                return "skip"
            
        # Ajoutez ici l'input pour enclencher la sauvegarde
                
