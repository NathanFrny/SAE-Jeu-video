from __future__ import annotations
from cases import Case
from entities import Entity

class Water(Case):
    """
    The Water class that represent the water cell on the gameboard (A water cell slow the player)
    """
    
    def __init__(self: Water, pos: list[int, int], tile: str = "", entity: Entity = None, slowness: int = 1):
        """
        Initialization of the Water cell
        Args:
            pos (list[int, int]): The position of the water cell on the gameboard
            tile (str): The image path of the water
            entity (Entity|None): The entity that is on the cell
            slowness (int): The number of action point that is remove when the player is on the water cell
        """
        super().__init__(pos, tile, entity)
        self._slowness = slowness
        
    
    @property
    def slowness(self: Water) -> int:
        return self._slowness
    @slowness.setter
    def slowness(self: Water, slowness: int):
        self._slowness = slowness