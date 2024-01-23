from __future__ import annotations
from cases import Case
from entities import Entity

class Trap(Case):
    """
    The Trap class that represent the trap cell on the gameboard (A trap cell deal damage to the player)
    """
    
    def __init__(self: Trap, pos: list[int, int], tile: str = "", entity: Entity = None, damage: int = 10):
        """
        Initialization of the Trap cell
        Args:
            pos (list[int, int]): The position of the trap cell on the gameboard
            tile (str): The image path of the trap
            entity (Entity|None): The entity that is on the cell
            slowness (int): The number of hp that is remove when the player is on the trap cell
        """
        super().__init__(pos, tile, entity)
        self._damage = damage
        
    
    @property
    def damage(self: Trap) -> int:
        return self._damage
    @damage.setter
    def damage(self: Trap, damage: int):
        self._damage = damage