from __future__ import annotations
from entities import Entity
from cases import Case

class Wall(Case):
    """
    The Wall class that represent the wall cell on the gameboard (A wall cell cannot be reached by an entity except the golem)
    """
    
    def __init__(self: Wall, pos: list,  tile: str = "", entity: Entity = None, canCross: bool = False):
        """
        Initialization of the Wall cell
        Args:
            pos (list[int, int]): The position of the wall cell on the gameboard
            tile (str): The image path of the wall
            entity (Entity|None): The entity that is on the cell
            canCross (bool): Is the wall crossable by a player (if a golem destroy it)
        """
        super().__init__(pos, tile, entity)
        self._canCross = canCross
        
    
    @property
    def canCross(self: Wall) -> bool:
        return self._canCross
    @canCross.setter
    def canCross(self: Wall, canCross: bool):
        self._canCross = canCross
            