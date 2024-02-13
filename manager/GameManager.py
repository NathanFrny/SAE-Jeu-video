from entities import Player
from gameboard import GameboardAdapter
from components import SpriteRendererComponent, ActionPointComponent, HealthComponent, StrengthComponent, TransformComponent, CoinsComponent
from utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, CASE_SIZE, BOARD_X
from utils.PyFunc import getAllActions
from manager.InputManager import InputManager
import pygame
import json


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
                
                if (player_input == "save"):
                    self.save_game("save.json")
                    
                    
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
    # Implémentez ici la logique de sauvegarde (players et gameboard dans un premier temps)
    def save_game(self, file_path):
        game_data = {
            "players": [],
            "gameboard": []
        }

        # Parcourir chaque rangée de la grille
        for row in self.adapter.gameboard.grid:
            row_data = []

            # Parcourir chaque élément dans la rangée
            for element in row:
                # Convertir chaque élément en une liste d'attributs
                row_data.append(toJSONGrid(element))

            # Ajouter le type de l'élément dans le JSON avant ses attributs
            game_data["gameboard"].append(row_data)
            
        for row in self.adapter._room_builder._players:
            row_data = []
        
            row_data.append(toJSONPlayer(row))
                
            game_data["players"].append(row_data)

        with open(file_path, 'w') as file:
            json.dump(game_data, file)

        
def toJSONGrid(instance):
    attributes = {"__type__": type(instance).__name__}  # Ajouter le type de l'instance comme clé spéciale
    for attr in dir(instance):
        if not callable(getattr(instance, attr)) and not attr.startswith("__"):
            value = getattr(instance, attr)
            # Convertir la valeur en une représentation JSON compatible
            if isinstance(value, (list, dict, str, int, float, bool, type(None))):
                attributes[attr] = value
            else:
                attributes[attr] = str(value)  # Convertir les autres types en chaînes de caractères
    return attributes


def toJSONPlayer(player: Player):
    return {
        "name": player.name,
        "max_health": player.get_component(HealthComponent).max_health,
        "current_health":player.get_component(HealthComponent).current_health,
        "max_action_point":player.get_component(ActionPointComponent).max_action_points,
        "current_action_point":player.get_component(ActionPointComponent).current_action_points,
        "initial_strength":player.get_component(StrengthComponent).initial_strength,
        "strength":player.get_component(StrengthComponent).strength,
        "position":player.get_component(TransformComponent).position,
        # "image":player.get_component(SpriteRendererComponent).image,
        # "rect":player.get_component(SpriteRendererComponent).rect,
        # "sprite":player.get_component(SpriteRendererComponent).sprite,
        "coins":player.get_component(CoinsComponent).coins
        
        # Add other attributes as needed
    }

