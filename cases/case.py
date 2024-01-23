from __future__ import annotations
from entities import Entity

class Case():
    """
    The default Case class that represent a cell on the gameboard
    """
    
    def __init__(self: Case, pos: list[int, int],  tile: str = "", entity: Entity = None):
        """
        Initialization of the Cell
        Args:
            pos (list[int, int]): The position of the cell on the gameboard
            tile (str): The image path of the cell
            entity (Entity|None): The entity that is on the cell
        """
        self._pos = pos
        self._tile = tile
        self._entity = entity
    
    # Getter and Setter
    
    @property
    def tile(self: Case) -> str:
        """ get the tile (image) of the case

        Args:
            self (Case): The case

        Returns:
            str: the path of the tile
        """
        return self._tile
    @tile.setter
    def tile(self: Case, image: str):
        self._tile = image
        
    @property
    def pos(self: Case) -> list[int, int]:
        return self._pos
    @pos.setter
    def pos(self: Case, x: int, y: int):
        self._pos = [x,y]
        
    @property
    def entity(self: Case) -> Entity:
        return self._entity
    @entity.setter
    def entity(self: Case, entity: Entity):
        self._entity = entity
        