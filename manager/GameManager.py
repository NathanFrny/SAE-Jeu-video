from entities import Player
from gameboard import GameboardAdapter
from components import SpriteRendererComponent, ActionPointComponent
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
        current_player_index = 0
        self.players[current_player_index].get_component(ActionPointComponent).reset_action_point()


        while running:
            current_player = self.players[current_player_index]
            action_points = current_player.get_component(ActionPointComponent).current_action_points
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                player_input = self.input_manager.get_input(current_player, event)
                    
                if (player_input == "getAllActions"):
                    possible_actions = getAllActions(current_player, self.adapter.gameboard)
                    print(getAllActions(current_player, self.adapter.gameboard))

                if (player_input == "skip" or action_points <= 0):
                    current_player_index = (current_player_index + 1) % len(self.players)
                    current_player = self.players[current_player_index]
                    current_player.get_component(ActionPointComponent).reset_action_point()
                    screen.fill((0, 0, 0))
                    self.adapter.graphic_gameboard.draw(screen)

                # Ajoutez ici la détection de l'input et l'appel de la méthode
                    
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


    # Implémentez ici la logique de sauvegarde (players et gameboard dans un premier temps)
    def save_game(self):
        ...