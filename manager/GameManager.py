from entities import Player, Slime, Golem, Skeleton, Bat
from gameboard import GameboardAdapter
from components import SpriteRendererComponent, ActionPointComponent, PlayerActionsComponent
from utils.constants import *
from utils.PyFunc import getAllActions
from manager.InputManager import InputManager
from random import choice
import pygame

class GameManager:

    def __init__(self, players_count):
        self.players = []
        self.monsters = []
        self.monsters_list = ["Slime", "Skeleton", "Golem", "Bat"]
        self.room_level = 12
        
        for i in range(players_count):
            self.players.append(Player("Player " + str(i + 1), "images/player" + str(i + 1) + ".png"))
        self.adapter = GameboardAdapter(self.players)
        
        self.input_manager = InputManager()
        
    def random_monster_spawning(self):
        """ Spawn monsters randomly on the gameboard.
        """
        while self.room_level > 0:
            match choice(self.monsters_list):
                case "Slime":
                    self.monsters.append(Slime(SLIME_IMAGE, SLIME_HEALTH, SLIME_ACTION_POINT, SLIME_DAMAGES))
                    self.room_level -= SLIME
                case "Skeleton":
                    self.monsters.append(Skeleton(SKELETON_IMAGE, SKELETON_HEALTH, SKELETON_ACTION_POINT, SKELETON_DAMAGES))
                    self.room_level -= SKELETON
                case "Bat":
                    self.monsters.append(Bat(BAT_IMAGE, BAT_HEALTH, BAT_ACTION_POINT, BAT_DAMAGES))
                    self.room_level -= BAT
                case "Golem":
                    self.monsters.append(Golem(GOLEM_IMAGE, GOLEM_HEALTH, GOLEM_ACTION_POINT, GOLEM_DAMAGES))
                    self.room_level -= GOLEM
        
        self.adapter.spawn_entities_randomly(self.monsters)
            
    
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 10))
        self.adapter.draw()
        self.random_monster_spawning()
        self.adapter.graphic_gameboard.draw(screen)
        for player in self.players:
            player.get_component(PlayerActionsComponent).gameboard = self.adapter.gameboard
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
                    player_actions_component = current_player.get_component(PlayerActionsComponent)
                    player_actions_component.update_possible_actions()
                    possible_actions = player_actions_component.all_actions
                    print(possible_actions)

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
                for attack in possible_actions["PossibleAttack"]:
                    pygame.draw.circle(screen, (0, 0, 255), (attack[1] * CASE_SIZE + BOARD_X, attack[0] * CASE_SIZE), 5)
            
            
            for player in self.players:
                player.update()
                sprite = player.get_component(SpriteRendererComponent)
                if sprite:
                    screen.blit(sprite.image, sprite.rect)
                    
            for monster in self.monsters:
                monster.update()
                sprite = monster.get_component(SpriteRendererComponent)
                if sprite:
                    screen.blit(sprite.image, sprite.rect)
                    
            pygame.display.flip()


    # Implémentez ici la logique de sauvegarde (players et gameboard dans un premier temps)
    def save_game(self):
        ...