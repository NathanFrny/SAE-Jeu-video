from components import MonstersComponent, TransformComponent, ActionPointComponent, HealthComponent
from utils.PyFunc import distance_calcul
from entities import Entity
from typing import Dict, List
import heapq

class SkeletonComponent(MonstersComponent):
    def __init__(self, parent_entity):
        super().__init__(parent_entity)
        self._location = self._parent_entity.get_component(TransformComponent).position

    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    def update_possible_actions(self):
        """Update the lists of possible actions based on the current state of the game."""
        
        if (not self.gameboard):
            KeyError("The gameboard is not set.")
        
        self._possible_movements.clear()
        self._possible_attacks.clear()

        self.current_position = self._parent_entity.get_component(TransformComponent).position
        self.current_action_point = self._parent_entity.get_component(ActionPointComponent).current_action_points
        grid = self.gameboard.grid
        nb_row = self.gameboard.nb_row
        nb_col = self.gameboard.nb_col
        max_depth = self.current_action_point
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def explore_moves(x, y, depth_left):
            from tiles import GroundTile, LeverTile, WaterTile, PortalTile, TrapTile, ExitTile
            from entities import Player
            if depth_left == 0:
                return

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < nb_row and 0 <= new_y < nb_col:
                    tile = grid[new_x][new_y]

                    if (not tile.is_player_on):
                        #TODO : Check if the tile is a player (add tile.entity for players)
                        if isinstance(tile.entity, Player) and ([new_x, new_y] not in self._possible_attacks):
                            self._possible_attacks.append([new_x, new_y])
                        if isinstance(tile, (GroundTile, WaterTile, PortalTile, TrapTile, ExitTile)) and ([new_x, new_y] not in self._possible_movements ) and (tile.entity == None) and ([new_x, new_y] not in self._possible_attacks):
                            self._possible_movements.append([new_x, new_y])
                            explore_moves(new_x, new_y, depth_left - 1) 

        explore_moves(*self.current_position, max_depth)

    def findClosestPlayer(self, players: list[Entity]) -> list[list[int, int]]:
        """ Find the closest player to the monster.
        """
        from tiles import WallTile, LeverTile
        grid = self.gameboard.grid
        nb_row, nb_col = self.gameboard.nb_row, self.gameboard.nb_col
        self._location = self._parent_entity.get_component(TransformComponent).position

        def is_valid_move(row, col):
            if 0 <= row < nb_row and 0 <= col < nb_col:
                cell = grid[row][col]
                return (not isinstance(cell, (WallTile, LeverTile)))
            return False

        def dijkstra():
            distances = [[float('inf')] * nb_col for _ in range(nb_row)]
            heap = [(0, self._location)]
            distances[self._location[0]][self._location[1]] = 0
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
            if (player.get_component(HealthComponent).is_dead):
                alive_players.append(player)
        if alive_players:
            find_closest_player = min([(distance_calcul(self._location, player.get_component(TransformComponent).position), player.get_component(TransformComponent).position) for player in alive_players])
            closest_player = find_closest_player[1]

            shortest_path = [list(node) for node in dijkstra()]
            
            return shortest_path
        return
    
    def update(self):
        pass

    @property
    def all_actions(self) -> Dict[str, List[int]]:
        """Return a dictionary of all possible actions."""
        return {
            "PossibleMovement": self.possible_movements,
            "PossibleAttack": self.possible_attacks,
        }
