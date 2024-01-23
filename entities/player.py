from __future__ import annotations
from constant import PLAYER_HEALTH, PLAYER_ACTION_POINT, PLAYER_DAMAGES, LEVER_ACTIVATED
from items import Item
from entities import Entity
from cases import Case, Wall, Lever, Exit
import pygame

class Player(Entity):
    """
    The class that represent the Bat entity that the players have to fight against
    """
    
    def __init__(self: Player, image: str, name: str = "Player",  location: list[int, int]= [0,0], max_health: int= PLAYER_HEALTH, damage: int= PLAYER_DAMAGES, action: int= PLAYER_ACTION_POINT, is_dead: bool = False, coins: int = 0, inventory: list[Item] = []):
        """
        Initialization of the Player entity
        Args:
            image (str): The image path of the player
            name (str): The name of the player
            location (list[int, int]): his location on the gameboard
            max_health (int): The maximum amount of health
            damage (int): The maximum amount of damage the entity deal
            action (int): The action point of the player
            is_dead (bool): Is the player dead ?
            coins (int): The coins that the player have
            inventory (list[Item]): The inventory of the player
        """
        super().__init__(image, location, max_health, damage, action)
        self._name = name
        self._coins = coins
        self._inventory = inventory
        self._is_dead = is_dead
          
    @property
    def name(self: Player) -> str:
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name
        
    @property
    def coins(self: Player) -> int:
        return self._coins
    @coins.setter
    def coins(self: Player, coins: int):
        self._coins = coins
    def addCoins(self: Player, coins: int):
        """
        Give coins to the player
        Args:
            coins (int): The number of coins the player get
        """
        self._coins += coins
        if (self._coins > 99):
            self._coins = 99

    @property
    def inventory(self: Player) -> list[Item]:
        return self._inventory
    @inventory.setter
    def inventory(self: Player, inventory: list[Item]) :
        self._inventory = inventory
        
    @property
    def is_dead(self: Player) -> bool:
        return self._is_dead
    @is_dead.setter
    def is_dead(self: Player, is_dead: bool):
        self._is_dead = is_dead
        


    ###### Methods ##################################################################


    def getAllActions(self: Player, grid: list[Case], items_location: list[list[int, int]], nb_row: int, nb_col: int) -> list[list[int, int]]:
        """ Get all the possible movements and attack possibilities for the player

        Args:
            self (Player): The player
            grid (list[Case]): The gameboard
            nb_row (int): The number of row of the gameboard
            nb_col (int): The number of column of the gameboard

        Returns:
            list: a list of all possible movement
            list: a list of all possible attacks
        """
        possible_positions = []
        attack_positions = []
        levers_positions = []
        items_positions = []
        max_depth = self._current_action_point

        current_x, current_y = self.location

        # index directions list
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        # check possible direction recursively
        def explore_moves(x, y, depth_left):
            # Check if we have enough action point
            if depth_left == 0:
                return

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # Check if the position is good (Inside the Gameboard)
                if 0 <= new_x < nb_row and 0 <= new_y < nb_col:
                    if isinstance(grid[new_x][new_y], Wall):
                        if grid[new_x][new_y].canCross:
                            if ([new_x, new_y] != [x, y] and [new_x, new_y] not in items_location and (not isinstance(grid[new_x][new_y].entity, Entity) or isinstance(grid[new_x][new_y], Exit)) and not isinstance(grid[new_x][new_y], Lever)):
                                possible_positions.append([new_x, new_y])
                                explore_moves(new_x, new_y, depth_left - 1)
                    else:
                        if ([new_x, new_y] != [x, y] and [new_x, new_y] not in items_location and (not isinstance(grid[new_x][new_y].entity, Entity) or isinstance(grid[new_x][new_y], Exit)) and not isinstance(grid[new_x][new_y], Lever)):
                            possible_positions.append([new_x, new_y])
                            explore_moves(new_x, new_y, depth_left - 1)
                    # Check if a possible attack action is possible
                    if ([new_x, new_y] != [x, y] and isinstance(grid[new_x][new_y].entity, Entity) and not isinstance(grid[new_x][new_y].entity, Player) and [new_x, new_y] not in attack_positions):
                        attack_positions.append([new_x, new_y])
                        explore_moves(new_x, new_y, depth_left - 1)
                    # Check if a lever is in the range
                    if ([new_x, new_y] != [x, y] and isinstance(grid[new_x][new_y], Lever) and grid[new_x][new_y].state == "inactive" and [new_x, new_y] not in levers_positions):
                        levers_positions.append([new_x, new_y])
                        explore_moves(new_x, new_y, depth_left - 1)
                    # Check if an item is in the range
                    if ([new_x, new_y] != [x, y] and [new_x,new_y] in items_location and [new_x,new_y] not in items_positions and [new_x,new_y] not in attack_positions):
                        items_positions.append([new_x, new_y])
                        explore_moves(new_x, new_y, depth_left - 1)
        # explore function recursively to obtain all the possible positions
        explore_moves(current_x, current_y, max_depth)

        return possible_positions, attack_positions, levers_positions, items_positions

    def activateLever(self: Player, lever: Lever, group: pygame.sprite.Group):
        """
        The function that is called when a player activate a lever
        Args:
            lever (Lever): The lever that is activated
            group (pygame.sprite.Group): The group sprite of the interface
        """
        lever.state = "active"
        lever.tile = LEVER_ACTIVATED
        for sprite in group:
            if sprite == lever:
                sprite.kill()
                group.remove(lever)
        self.current_action_point -= 1
        return group

    def move(self: Player, target: list[int, int], group: pygame.sprite.Group) -> pygame.sprite.Group:
        """
        Move the player on the gameboard
        Args:
            target (list[int, int]): The position where the player move
            group (pygame.sprite.Group): The group sprite of the player 
        """
        super().move(target, group)
        return group
    
    def attack(self: Player, target: Entity, grid: list[Case], turn_list: list[Entity], group: pygame.sprite.Group) -> pygame.sprite.Group:
        """
        The attack function of the player, which allow them to attack an entity
        Args:
            target (Entity): The player that the bat attack
            grid (list[object]): The console representation of the gameboard
            turn_list (list[Entity]): The list of all the entities still alive on the gameboard
            group (pygame.sprite.Group): The group sprite of the player 
        """
        group, turn_list = super().attack(target, grid, turn_list, group)
        gain = 0
        # If target is dead, delete it in turn_list and in the sprite entities group
        if target.current_health <= 0:
            gain = target.costs
            grid[target.location[0]][target.location[1]].entity = None
            turn_list.remove(target)
            target.kill()
            group.remove(target)
        self.addCoins(gain)
        return group, turn_list
    
    
    
    