from entities import Player
from gameboard import GameboardAdapter
from components import SpriteRendererComponent
from utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from manager.InputManager import InputManager
import pygame

class GameManager:

    def __init__(self, players_count):
        self.players = []
        for i in range(players_count):
            self.players.append(Player("Player " + str(i + 1), "images/player" + str(i + 1) + ".png"))
        self.adapter = GameboardAdapter(self.players)
        self.input_manager = InputManager()
    
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 10))
        self.adapter.draw()
        self.adapter.graphic_gameboard.draw(screen)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.input_manager.get_input(self.players[0], event)
            screen.fill((0, 0, 0))
            self.adapter.graphic_gameboard.draw(screen)
            for player in self.players:
                player.update()
                sprite = player.get_component(SpriteRendererComponent)
                if sprite:
                    screen.blit(sprite.image, sprite.rect)
            pygame.display.flip()