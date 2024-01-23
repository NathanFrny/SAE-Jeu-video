from __future__ import annotations
from entities import Entity
from cases import Case, Wall, Lever
from constant import SKELETON_HEALTH, SKELETON_DAMAGES, SKELETON_ACTION_POINT, SKELETON_COST
import pygame
import heapq


class Skeleton(Entity):
    """
    The class that represent the Skeleton entity that the players have to fight against
    """
    def __init__(self: Skeleton, image: str,  location: list[int, int]= [0,0], max_health: int = SKELETON_HEALTH, damage: int = SKELETON_DAMAGES, action_point: int = SKELETON_ACTION_POINT):
        """
        Initialization of the Skeleton entity
        Args:
            image (str): The image path of the skeleton
            location (list[int, int]): his location on the gameboard
            max_health (int): The maximum amount of health
            damage (int): The maximum amount of damage the entity deal
            action_point (int): The action point of the skeleton
        """
        super().__init__(image, location, max_health, damage, action_point)
        self._costs = SKELETON_COST # The number of coins the player have if he kill a skeleton
        
        
    @property
    def costs(self: Skeleton) -> int:
        return self._costs
    @costs.setter
    def costs(self: Skeleton, cost: int):
        self._costs = cost
        
    def getAllMovements(self: Skeleton, players: list[Entity], grid: list[Case], nb_row: int, nb_col: int) -> list:
        """ Get all the possible movements for the player

        Args:
            self (Skeleton): The player
            grid (list[Case]): The gameboard
            nb_row (int): The number of row of the gameboard
            nb_col (int): The number of column of the gameboard

        Returns:
            list: a list of all possible movement
        """
        possible_positions = []
        attack_positions = []
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
                # Check if the position is good (not wall or lever)
                if 0 <= new_x < nb_row and 0 <= new_y < nb_col and not isinstance(grid[new_x][new_y], Wall) and not isinstance(grid[new_x][new_y], Lever):
                    if [new_x, new_y] != [x, y] and (grid[new_x][new_y].entity in players and not grid[new_x][new_y].entity.is_dead) and not [new_x, new_y] in possible_positions:
                        attack_positions.append([new_x, new_y])
                        explore_moves(new_x, new_y, depth_left - 1)
                    if [new_x, new_y] != [x, y] and not isinstance(grid[new_x][new_y].entity, Entity) and not [new_x, new_y] in possible_positions and not [new_x, new_y] in attack_positions:
                        possible_positions.append([new_x, new_y])
                        explore_moves(new_x, new_y, depth_left - 1)
                    

        # explore function recursively to obtain all the possible positions
        explore_moves(current_x, current_y, max_depth)
        
        

        return possible_positions, attack_positions

    def findClosestPlayer(self: Skeleton, grid: list[object], players: list[Entity], nb_row: int, nb_col: int) -> list[list[int, int]]:
        """
        Find the closest player on the gameboard
        Args:
            grid (list[object]): The console representation of the gameboard
            players (list[Entity]): The list of all the players still alive on the gameboard
            nb_row (int): The number of row on the grid
            nb_col (int): The number of col on the grid

        Returns: The list of movement the entity have to do to reach the closest player
        """
        def is_valid_move(row, col):
            if 0 <= row < nb_row and 0 <= col < nb_col:
                cell = grid[row][col]
                return (not isinstance(cell, (Wall, Lever)))
            return False

        def dijkstra():
            distances = [[float('inf')] * nb_col for _ in range(nb_row)]
            heap = [(0, self.location)]
            distances[self.location[0]][self.location[1]] = 0
            parents = [[None] * nb_col for _ in range(nb_row)]

            while heap:
                current_distance, current_node = heapq.heappop(heap)

                if current_node == closest_player:
                    break

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = current_node[0] + dr, current_node[1] + dc

                    if is_valid_move(new_row, new_col):
                        new_distance = current_distance + 1

                        if new_distance < distances[new_row][new_col]:
                            distances[new_row][new_col] = new_distance
                            parents[new_row][new_col] = current_node
                            heapq.heappush(heap, (new_distance, (new_row, new_col)))

            path = []
            node = closest_player
            while node:
                path.insert(0, node)
                node = parents[node[0]][node[1]]

            return path

        alive_players = []
        for player in players:
            if not player.is_dead:
                alive_players.append(player)
        if alive_players:
            find_closest_player = min([(Entity.calculateDistance(self.location, player.location), player.location) for player in alive_players])
            closest_player = find_closest_player[1]

            shortest_path = dijkstra()

            return shortest_path
        return
                    
    def move(self: Skeleton, target: list[int, int], group: pygame.sprite.Group) -> pygame.sprite.Group:
        """
        Move the entity on the gameboard
        Args:
            target (list[int, int]): The position where the entity move
            group (pygame.sprite.Group): The group sprite of the entity 
        """
        super().move(target, group)
        return group
    
    def attack(self: Skeleton, target: Entity, grid: list[Case], turn_list: list[Entity], group: pygame.sprite.Group):
        """
        The attack function of the entity, which allow them to attack a player
        Args:
            target (Entity): The entity that the bat attack
            grid (list[object]): The console representation of the gameboard
            turn_list (list[Entity]): The list of all the entities still alive on the gameboard
            group (pygame.sprite.Group): The group sprite of the entity 
        """
        group, turn_list = super().attack(target, grid, turn_list, group)
        # If target is dead, delete it in turn_list and in the sprite entities group
        if target.current_health <= 0:
            target.is_dead = True
        return group, turn_list