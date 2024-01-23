from __future__ import annotations
from entities import Entity
from cases import Case

class Exit(Case):
    """
    The Exit class that represent the exit cell on the gameboard
    """
    
    def __init__(self: Exit, pos: list,  tile: str = "", entity: Entity = None):
        """
        Initialization of the Exit cell
        Args:
            pos (list[int, int]): The position of the exit cell on the gameboard
            tile (str): The image path of the exit
            entity (Entity|None): The entity that is on the cell
        """
        super().__init__(pos, tile, entity)
        self._player_list = [] # The list of player that reached the exit
        self._is_open = False # Is the exit open or not
        
        
    @property
    def player_list(self: Exit):
        return self._player_list
    @player_list.setter
    def player_list(self: Exit, player_list: list):
        self._player_list = player_list
    
    @property
    def is_open(self: Exit):
        return self._is_open
    @is_open.setter
    def is_open(self: Exit, is_open: bool):
        self._is_open = is_open