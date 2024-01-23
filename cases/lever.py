from __future__ import annotations
from entities import Entity
from cases import Case


class Lever(Case):
    """
    The Lever class that represent the lever cell on the gameboard
    """
    
    def __init__(self, pos: list, tile: str = "", entity: Entity = None, state : str = "inactive"):
        """
        Initialization of the Lever cell
        Args:
            pos (list[int, int]): The position of the lever cell on the gameboard
            tile (str): The image path of the lever
            entity (Entity|None): The entity that is on the cell
            state (str): The state of the lever (if it activate or not). By default inactive
        """
        super().__init__(pos, tile, entity)
        self._state = state
        
    
    @property
    def state(self: Lever) -> str:
        return self._state
    @state.setter
    def state(self: Lever, state: str):
        self._state = state
        