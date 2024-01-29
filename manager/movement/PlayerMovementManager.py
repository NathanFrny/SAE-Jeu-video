from .MovementManager import MovementManager
from typing import Dict, List
from tiles import GroundTile, Lever
from entities import Monster

class PlayerMovementManager(MovementManager):
        
        def __init__(self, gameboard):
            super().__init__(gameboard)
        
        # ------------------------------------------------------------------------------- #
        # ----------------------------------- Methods ----------------------------------- #
        # ------------------------------------------------------------------------------- #
        
        
            