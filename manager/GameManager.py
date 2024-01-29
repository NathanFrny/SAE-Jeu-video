from entities import Player
from gameboard import GameboardAdapter
from components import SpriteRendererComponent, TransformComponent
from utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, CASE_SIZE, BOARD_X
from utils.PyFunc import getAllActions
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
        possible_actions = {}

        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if (self.input_manager.get_input(self.players[0], event) == "getAllActions"):
                    possible_actions = getAllActions(self.players[0], self.adapter.gameboard)
                    print(getAllActions(self.players[0], self.adapter.gameboard))
                    
            screen.fill((0, 0, 0))
            self.adapter.graphic_gameboard.draw(screen)
            
            if "PossibleMovement" in possible_actions:
                for move in possible_actions["PossibleMovement"]:
                    pygame.draw.circle(screen, (255, 0, 0), (move[1] * CASE_SIZE + BOARD_X, move[0] * CASE_SIZE), 5)
                for position in possible_actions["PossibleLever"]:
                    pygame.draw.circle(screen, (0, 255, 0), (position[1] * CASE_SIZE + BOARD_X, position[0] * CASE_SIZE), 5)
            
            for player in self.players:
                player.update()
                sprite = player.get_component(SpriteRendererComponent)
                if sprite:
                    screen.blit(sprite.image, sprite.rect)
                    
            pygame.display.flip()