from __future__ import annotations
from gameboard import Gameboard
from graphics import Inventory, PlayerStats
from entities import Entity, Player, Golem
from cases import Exit, Case
from items import Item
from constant import BOARD_X, CASE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, EXIT_LEVERS, EXIT_OPEN
from random import choice
import pygame


class Gameloop:
    """
    The gameloop of the game, it repeat all the action that the player or the entity do frequently
    """
    
    def __init__(self: Gameloop, tour: int, turn: Entity | None, room: int, entity_group: pygame.sprite.Group):
        """ Initialization of the gameloop
        Args:
            self (Gameloop): The gameloop
            tour (int): The number of round
            turn (Entity): The entity that is the turn
            room (int): The number of room the players beat
            entity_group (pygame.sprite.Group): The group of entities that we have to draw on the interface
        """
        self._tour = tour
        self._turn = turn
        self._room = room
        self._entity_group = entity_group
        self._turn_list = []
        self._exit_list = []
        self._exit_levers = EXIT_LEVERS
        
        # Initialisation du PLateau
        self._gameboard = Gameboard()

        self._items_sprite_location = []
        self._items_sprite = []
        self._items = []
        
        
        self._players = self._gameboard.createPlayers(4)
        self._turn = self._players[0]
        
        self._buttons = []
        
        self._player_stats = PlayerStats(self._players)
        self._inventory = Inventory()
    
    @property
    def tour(self: Gameloop) -> int:
        return self._tour
    @tour.setter
    def tour(self: Gameloop, tour: int):
        self._tour = tour
        
    @property
    def players(self: Gameloop) -> list[Entity]:
        return self._players
    @players.setter
    def players(self: Gameloop, players: list[Player]):
        self._players = players
        
    @property
    def turn(self: Gameloop) -> Entity:
        return self._turn
    @turn.setter
    def turn(self: Gameloop, turn: Entity):
        self._turn = turn
        
    @property
    def turn_list(self: Gameloop) -> list[Entity]:
        return self._turn_list
    @turn_list.setter
    def turn_list(self: Gameloop, turn_list: list[Entity]):
        self._turn_list = turn_list
        
    @property
    def room(self: Gameloop) -> int:
        return self._room
    @room.setter
    def room(self: Gameloop, room: int):
        self._room = room
        
    @property
    def entity_group(self: Gameloop) -> pygame.sprite.Group:
        return self._entity_group
    @entity_group.setter
    def entity_group(self: Gameloop, entity_group: pygame.sprite.Group):
        self._entity_group = entity_group
        
    @property
    def gameboard(self: Gameloop) -> Gameboard:
        return self._gameboard
    @gameboard.setter
    def gameboard(self: Gameloop, gameboard: Gameboard):
        self._gameboard = gameboard

    @property
    def items_sprite_location(self: Gameloop) -> list[int, int]:
        return self._items_sprite_location
    @items_sprite_location.setter
    def items_sprite_location(self: Gameloop, items_sprite_location: list):
        self._items_sprite_location = items_sprite_location

    @property
    def items_sprite(self: Gameloop):
        return self._items_sprite
    @items_sprite.setter
    def items_sprite(self: Gameloop, items: list[int, int]):
        self._items_sprite = items

    @property
    def items(self: Gameloop) -> list[Item]:
        return self._items
    @items.setter
    def items(self: Gameloop, items: list[Item]):
        self._items = items

    @property
    def exit_levers(self: Gameloop) -> int:
        return self._exit_levers
    @exit_levers.setter
    def exit_levers(self: Gameloop, exit_levers: int):
        self._exit_levers = exit_levers

    @property
    def exit_list(self: Gameloop) -> list[Entity]:
        return self._exit_list
    @exit_list.setter
    def exit_list(self: Gameloop, exit_list: [Entity]):
        self._exit_list = exit_list
        
    @property
    def buttons(self: Gameloop) -> list:
        return self._buttons
    @buttons.setter
    def buttons(self: Gameloop, buttons: list):
        self._buttons = buttons   
        
    
    ########### Methods #####################################################
    
    
    def createLevel(self: Gameloop, screen: pygame.Surface):
        """ create and draw a complete room on the graphic interface

        Args:
            self (Gameloop): The gameloop
            screen (pygame.Surface): The graphic interface
        """
        self.room += 1
        enemies = self._gameboard.createEnemies(12)
        self._items_sprite, self.items = self._gameboard.chooseItem(3)
        
        for player in self.players:
            self._entity_group.add(player)
            self._turn_list.append(player)
        for enemy in enemies:
            self._entity_group.add(enemy)
            self._turn_list.append(enemy)

        self.turn = self._turn_list[0]

        self._gameboard.createRoom(100, 10, 10, self._players, enemies, self.items_sprite, self.items)

        for item in self._items_sprite:
            self._items_sprite_location.append(item.location)
            self._entity_group.add(item)
        

        # Draw the firt room
        self._gameboard.drawRoom(screen)
        # Dessiner la grille en fonction de la position de départ
        for row in range(self._gameboard.nb_row):
            for col in range(self._gameboard.nb_col):
                x = BOARD_X + col * CASE_SIZE
                y = row * CASE_SIZE
                screen.blit(self._gameboard._graphicGrid[row][col], (x, y))
        
        for player in self.players:
            self._player_stats.drawPlayerStats(screen)
            self._inventory.drawInventory(player, screen)
            self._buttons = self._inventory.buttons
            
    
    
    def updateRoom(self: Gameloop, screen: pygame.Surface, indice: int | None):
        """ Update the room, the player stats and the inventories of the game

        Args:
            self (Gameloop): The gameloop
            screen (pygame.Surface): The graphic interface
            indice (int): A reference about the entity whose turn it is to play
        """
        
        if indice != None:
            self._turn = self._turn_list[indice]
        
        
        screen.fill((0,0,0))
        
        #load background
        background = pygame.image.load("images/background.png")
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background, (0,0))
        # draw room, playerstats and current player inventory 
        self.gameboard.drawRoom(screen)
        
        self.buttons = []
       
        if (isinstance(self.turn, Player)):
            self._player_stats.drawPlayerStats(screen)
            self._inventory.drawInventory(self.turn, screen)
            self.buttons = self._inventory.buttons
            
            
        if self.exit_levers <= 0:
            for row in self.gameboard.grid:
                for case in row:
                    if isinstance(case, Exit):
                         case.is_open = True
                         case.tile = EXIT_OPEN
        
    
    def resetGameLoop(self: Gameloop):
        """
        Reset the GameLoop when players finish a room
        """
        self.turn_list = []
        self.exit_list = []
        self.items = []
        self.items_sprite = []
        self.items_sprite_location = []
        for player in self.players:
            player.current_action_point = player.action_point
        self.exit_levers = EXIT_LEVERS
        self._gameboard = Gameboard()

        
    def entityTurn(self: Gameloop, group: pygame.sprite.Group):
        """
        Do what the entities should do when it's their turn
        """
        move = False
        attack = False
        closest = self.turn.findClosestPlayer(self.gameboard.grid, self.players, self.gameboard.nb_row, self.gameboard.nb_col)
        if closest:
            pos_possible, attack_possible = self.turn.getAllMovements(self.players, self.gameboard.grid, self.gameboard.nb_row, self.gameboard.nb_col)
            for position in attack_possible:
                self.turn.attack(self.gameboard.grid[position[0]][position[1]].entity, self.gameboard.grid, self.turn_list, group)
                attack = True
                self.turn.current_action_point -= 1
            if not attack:
                for pos in closest:    
                    if list(pos) in pos_possible:
                        self.gameboard.grid[self.turn.location[0]][self.turn.location[1]].entity = None
                        if isinstance(self.turn, Golem):
                            self.turn.move(list(pos), self.gameboard.grid, group)
                        else:
                            self.turn.move(list(pos), group)
                        move = True
                        self.gameboard.grid[self.turn.location[0]][self.turn.location[1]].entity = self.turn
            if not move and pos_possible:
                pos = choice(pos_possible)
                self.gameboard.grid[self.turn.location[0]][self.turn.location[1]].entity = None
                if isinstance(self.turn, Golem):
                    self.turn.move(list(pos), self.gameboard.grid, group)
                else:
                    self.turn.move(list(pos), group)
                self.gameboard.grid[self.turn.location[0]][self.turn.location[1]].entity = self.turn

    
    def setCellEntity(self: Gameloop, entity: Entity, setter: Entity | None):
        """
        Attribute an entity to a cell
        """
        self.gameboard.grid[entity.location[0]][entity.location[1]].entity = setter
        
    def isCell(self: Gameloop, entity: Entity, cell: Case) -> bool:
        """
        Return if the cell checked is the same type as the cell type in parameter
        """
        return isinstance(self.gameboard.grid[entity.location[0]][entity.location[1]], cell)
    
    def getEntityCell(self: Gameloop, entity: Entity) -> Entity:
        """
        Get which entity is on the cell
        """
        return self.gameboard.grid[entity.location[0]][entity.location[1]].entity
    
    def getCell(self: Gameloop, entity: Entity) -> Case:
        """
        Get the cell where the entity is
        """
        return self.gameboard.grid[entity.location[0]][entity.location[1]]