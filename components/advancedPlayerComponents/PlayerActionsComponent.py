from components import Component
from typing import Dict, List
from components import TransformComponent, ActionPointComponent


class PlayerActionsComponent(Component):
    """ Component that handles the possible actions of the player."""
    
    def __init__(self, parent_entity):
        super().__init__(parent_entity)
        self._possible_movements = []
        self._possible_attacks = []
        self._possible_levers = []
        self._possible_items = []
        
        self.__gameboard = []
        
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def possible_movements(self):
        return self._possible_movements
    @possible_movements.setter
    def possible_movements(self, possible_movements):
        self._possible_movements = possible_movements
        
    @property
    def possible_attacks(self):
        return self._possible_attacks
    @possible_attacks.setter
    def possible_attacks(self, possible_attacks):
        self._possible_attacks = possible_attacks
        
    @property
    def possible_levers(self):
        return self._possible_levers
    @possible_levers.setter
    def possible_levers(self, possible_levers):
        self._possible_levers = possible_levers
        
    @property
    def possible_items(self):
        return self._possible_items
    @possible_items.setter
    def possible_items(self, possible_items):
        self._possible_items = possible_items
        
    @property
    def gameboard(self):
        return self.__gameboard
    @gameboard.setter
    def gameboard(self, gameboard):
        self.__gameboard = gameboard
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    def update(self):
        """ Update the component.
        """
        pass
    
    def update_possible_actions(self):
        """Update the lists of possible actions based on the current state of the game."""
        
        if (not self.__gameboard):
            KeyError("The gameboard is not set.")
        
        self._possible_movements.clear()
        self._possible_attacks.clear()
        self._possible_items.clear()
        self._possible_levers.clear()

        self.current_position = self._parent_entity.get_component(TransformComponent).position
        self.current_action_point = self._parent_entity.get_component(ActionPointComponent).current_action_points
        self.grid = self.__gameboard.grid
        self.nb_row = self.__gameboard.nb_row
        self.nb_col = self.__gameboard.nb_col
        max_depth = self.current_action_point
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def explore_moves(x, y, depth_left):
            from tiles import GroundTile, LeverTile, WaterTile, PortalTile, TrapTile, ExitTile
            from entities import Monster
            if depth_left == 0:
                return

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.nb_row and 0 <= new_y < self.nb_col:
                    tile = self.grid[new_x][new_y]

                    if (not tile.is_player_on):
                        if isinstance(tile.entity, Monster) and ([new_x, new_y] not in self._possible_attacks):
                            self._possible_attacks.append([new_x, new_y])
                        if isinstance(tile, (GroundTile, WaterTile, PortalTile, TrapTile, ExitTile)) and ([new_x, new_y] not in self._possible_movements ) and (tile.entity == None) and ([new_x, new_y] not in self._possible_attacks):
                            self._possible_movements.append([new_x, new_y])
                            explore_moves(new_x, new_y, depth_left - 1) 

                        if isinstance(tile, LeverTile) and ([new_x, new_y] not in self._possible_levers):
                            self._possible_levers.append([new_x, new_y])

        explore_moves(*self.current_position, max_depth)

    @property
    def all_actions(self) -> Dict[str, List[int]]:
        """Return a dictionary of all possible actions."""
        return {
            "PossibleMovement": self._possible_movements,
            "PossibleAttack": self._possible_attacks,
            "PossibleItem": self._possible_items,
            "PossibleLever": self._possible_levers
        }