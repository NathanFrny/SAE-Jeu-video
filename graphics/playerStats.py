from __future__ import annotations
import pygame
from entities import Player
from graphics import HealthBar
from constant import PLAYER_STATS_X, ICON_SIZE, GAP, COIN

class PlayerStats:
    """
    Class that represent of the player statistics during the game
    """
    
    def __init__(self: PlayerStats, player_list: list[Player]):
        """
        Initialization of the player statistics
        args:
            player_list (list[Player]): All the players of the game
        """
        self._player_list = player_list
        
        self._health_bars = []
        for player in self._player_list:
            health_bar = HealthBar(0, 0, 180, 30, player)
            self._health_bars.append(health_bar)

        
        
    @property
    def player_list(self: PlayerStats) -> list[Player]:
        return self._player_list
    @player_list.setter
    def player_list(self: PlayerStats, player_list: list[Player]):
        self._player_list = player_list
        
    
    #### Methods ##############################################################
    
    
    def drawPlayerStats(self: PlayerStats, screen: pygame.Surface):
        """ Set the all the players stats into the graphic interface

        Args:
            self (PlayerStats): All the players stats
            screen (pygame.Surface): The graphic interface
        """
        posy = 50
        font = pygame.font.Font(None, 36)
        for player, health_bar in zip(self._player_list, self._health_bars):
            # Define the position of the player icon
            image = pygame.image.load(player.image_path)
            image = pygame.transform.scale(image, (ICON_SIZE, ICON_SIZE))
            rect = image.get_rect()
            rect.x = PLAYER_STATS_X
            rect.y = posy
            screen.blit(image, rect)
            
            # Define the position of the player name text
            text = font.render(player.name, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.x = PLAYER_STATS_X + ICON_SIZE + 50
            text_rect.centery = posy - ICON_SIZE // 10
            screen.blit(text, text_rect)
            
            # Define the position of the healthBar
            health_bar.x = rect.x + ICON_SIZE + 15 
            health_bar.y = posy + 15 
            health_bar.draw(screen)
            
            # Define the position of the coin icon
            coin_icon = pygame.image.load(COIN)
            coin_icon = pygame.transform.scale(coin_icon, (ICON_SIZE / 2, ICON_SIZE / 2))
            coin_icon_rect = coin_icon.get_rect()
            coin_icon_rect.x = PLAYER_STATS_X + ICON_SIZE + 15
            coin_icon_rect.centery = posy + ICON_SIZE // 1.4
            screen.blit(coin_icon, coin_icon_rect)
            
            # Define the position of the coin count text
            coin_text = font.render(f"Coins: {player.coins}", True, (255, 255, 255))
            coin_text_rect = coin_text.get_rect()
            coin_text_rect.x = PLAYER_STATS_X + ICON_SIZE + 100
            coin_text_rect.centery = posy + ICON_SIZE // 1.4
            screen.blit(coin_text, coin_text_rect)
            
            posy += GAP * 1.5
            
            
            