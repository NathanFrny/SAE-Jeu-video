from __future__ import annotations
from cases import Case
from entities import Entity



class Portal(Case):
    """
    The Portal class that represent the portal cell on the gameboard (A portal cell allow player to teleport into the other portal cell)
    """
    
    def __init__(self: Portal, pos: list[int], tile: str = "", entity: Entity = None, target: Portal | None = None):
        """
        Initialization of the Portal cell
        Args:
            pos (list[int, int]): The position of the portal cell on the gameboard
            tile (str): The image path of the portal
            entity (Entity|None): The entity that is on the cell
            target (Portal|None): The other portal of the room (The one the player is teleported if he go on the cell)
        """
        super().__init__(pos, tile, entity)
        self._target = target
        # connect also the target to him if exist
        if target != None:
            target.target = self
        
    
    @property
    def target(self: Portal) -> Portal:
        return self._target
    @target.setter
    def target(self: Portal, target: Portal | None):
        self._target = target