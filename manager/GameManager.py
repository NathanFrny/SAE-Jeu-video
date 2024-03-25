from entities import Player, Slime, Golem, Skeleton, Bat, Action
from tiles import ExitTile, LeverTile
from gameboard import GameboardAdapter
from components import SpriteRendererComponent, ActionPointComponent, PlayerActionsComponent, TransformComponent
from components.monstersComponents.SkeletonComponent import SkeletonComponent
from utils.constants import *
from manager.InputManager import InputManager
from random import choice
import pygame

class GameManager:

    def __init__(self, players_count):
        self.players = []
        self.monsters = []
        self.monsters_list = ["Slime", "Skeleton", "Golem", "Bat"]
        self.room_level = 12
        self.levers_count = LEVER_COUNT
        self.exit: ExitTile = None
        self.exit_position = [0, 0]
        
        for i in range(players_count):
            self.players.append(Player("Player " + str(i + 1), "images/player" + str(i + 1) + ".png"))
        self.adapter = GameboardAdapter(self.players)
        
        self.input_manager = InputManager()
        self.current_actions = []
        
    def random_monster_spawning(self):
        """ Spawn monsters randomly on the gameboard.
        """
        while self.room_level > 0:
            match choice(self.monsters_list):
                case "Slime":
                    self.monsters.append(Slime("Slime", SLIME_IMAGE, SLIME_HEALTH, SLIME_ACTION_POINT, SLIME_DAMAGES))
                    self.room_level -= SLIME
                case "Skeleton":
                    self.monsters.append(Skeleton("Skeleton", SKELETON_IMAGE, SKELETON_HEALTH, SKELETON_ACTION_POINT, SKELETON_DAMAGES))
                    self.room_level -= SKELETON
                case "Bat":
                    self.monsters.append(Bat("Bat", BAT_IMAGE, BAT_HEALTH, BAT_ACTION_POINT, BAT_DAMAGES))
                    self.room_level -= BAT
                case "Golem":
                    self.monsters.append(Golem("Golem", GOLEM_IMAGE, GOLEM_HEALTH, GOLEM_ACTION_POINT, GOLEM_DAMAGES))
                    self.room_level -= GOLEM
        
        self.adapter.spawn_entities_randomly(self.monsters)
            
    
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 10))
        self.adapter.draw()

        # Getting the exit tiles and store it into the exit attribute
        for row in range(self.adapter.gameboard.nb_row):
            for col in range(self.adapter.gameboard.nb_col):
                tile = self.adapter.gameboard.grid[row][col]
                if isinstance(tile, ExitTile):
                    self.exit = tile
                    self.exit_position = [row, col]
                    break

        self.random_monster_spawning()
        self.adapter.graphic_gameboard.draw(screen)
        for player in self.players:
            player.get_component(PlayerActionsComponent).gameboard = self.adapter.gameboard
        pygame.display.flip()
        running = True
        possible_actions = {}
        current_player_index = 0
        self.skip_turn_count = 0
        self.players[current_player_index].get_component(ActionPointComponent).reset_action_point()
        for player in self.players:
            self.adapter.gameboard.grid[player.get_component(TransformComponent).position[0]][player.get_component(TransformComponent).position[1]].entity = player
        for monster in self.monsters:
            if (isinstance(monster, Skeleton)):
                monster.get_component(SkeletonComponent).gameboard = self.adapter.gameboard

        while running:
            current_player = self.players[current_player_index]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                player_input = self.input_manager.get_input(current_player, self.current_actions, self.adapter.gameboard.grid, self.adapter.graphic_gameboard, event)
                    
                if (player_input == "getAllActions"):
                    player_actions_component = current_player.get_component(PlayerActionsComponent)
                    player_actions_component.update_possible_actions()
                    possible_actions = player_actions_component.all_actions
                    for actions, positions in possible_actions.items():
                        match (actions):
                            case "PossibleMovement":
                                for position in positions:
                                    action = Action("Move", "images/movement.png")
                                    action.get_component(TransformComponent).position = position
                                    self.current_actions.append(action)
                            case "PossibleAttack":
                                for position in positions:
                                    action = Action("Attack", "images/action.png")
                                    action.get_component(TransformComponent).position = position
                                    self.current_actions.append(action)
                            case "PossibleLever":
                                for position in positions:
                                    action = Action("Lever", "images/action.png")
                                    action.get_component(TransformComponent).position = position
                                    self.current_actions.append(action)
                                    

                if (player_input == "skip"):
                    self.current_actions.clear()
                    current_player_index = (current_player_index + 1) % len(self.players)
                    current_player = self.players[current_player_index]
                    current_player.get_component(ActionPointComponent).reset_action_point()
                    screen.fill((0, 0, 0))
                    self.adapter.graphic_gameboard.draw(screen)

                    self.skip_turn_count += 1

                    if self.skip_turn_count >= len(self.players):
                        self.skip_turn_count = 0

                        for enemy in self.monsters:
                            
                            if isinstance(enemy, Skeleton):
                                action = enemy.get_component(SkeletonComponent).all_actions
                                enemy.get_component(SkeletonComponent).update_possible_actions()
                            if isinstance(enemy, Slime):
                                #action = enemy.get_component(SlimeComponent).all_actions
                                #enemy.get_component(SkeletonComponent).update_possible_actions()
                                pass
                            if isinstance(enemy, Golem):
                                #action = enemy.get_component(GolemComponent).all_actions
                                #enemy.get_component(SkeletonComponent).update_possible_actions()
                                pass
                            if isinstance(enemy, Bat):
                                #action = enemy.get_component(BatComponent).all_actions
                                #enemy.get_component(SkeletonComponent).update_possible_actions()
                                pass

                            
                            if (isinstance(enemy, Skeleton)):
                                if (action["PossibleAttack"]):
                                    enemy.attack()
                                else:
                                    closest_player_directions = enemy.get_component(SkeletonComponent).findClosestPlayer(self.players)
                                    print(closest_player_directions)
                                    print(action['PossibleMovement'])
                                    for direction in closest_player_directions:
                                        for movement in action["PossibleMovement"]:
                                            if movement == direction:
                                                enemy.move(movement)


                    
            screen.fill((0, 0, 0))
            background = pygame.image.load("images/background.png")
            background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT - 10))
            screen.blit(background, (0, 0))
            self.adapter.graphic_gameboard.draw(screen)
                        
            
            for player in self.players:
                player.update()
                sprite = player.get_component(SpriteRendererComponent)
                if sprite:
                    screen.blit(sprite.image, sprite.rect)
                    
            if self.current_actions:
                for action in self.current_actions:
                    action.update()
                    sprite = action.get_component(SpriteRendererComponent)
                    if sprite:
                        screen.blit(sprite.image, sprite.rect)

            self.levers_count = 0
            for row in range(self.adapter.gameboard.nb_row):
                for col in range(self.adapter.gameboard.nb_col):
                    if isinstance(self.adapter.gameboard.grid[row][col], LeverTile):
                        lever = self.adapter.gameboard.grid[row][col]
                        if not lever.isOn:
                            self.levers_count += 1

            if self.exit.is_closed and self.levers_count <= 0:
                self.exit.is_closed = False
                self.adapter.graphic_gameboard.set_image(self.exit_position[0], self.exit_position[1], self.exit.dataTile.variants["open"][0])
                    
            for monster in self.monsters:
                monster.update()
                sprite = monster.get_component(SpriteRendererComponent)
                if sprite:
                    screen.blit(sprite.image, sprite.rect)
                    
            pygame.display.flip()


    # Implémentez ici la logique de sauvegarde (players et gameboard dans un premier temps)
    def save_game(self):
        ...