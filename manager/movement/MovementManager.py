from abc import ABC, abstractmethod
from typing import Dict, List

class MovementManager(ABC):
    
    def __init__(self, gameboard):
        self._gameboard = gameboard
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------- Getters and Setters ----------------------------- #
    # ------------------------------------------------------------------------------- #
    
    @property
    def gameboard(self):
        return self._gameboard
    @gameboard.setter
    def gameboard(self, gameboard):
        self._gameboard = gameboard
    
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    @abstractmethod
    def getAllActions(self, player) -> Dict[List[int, int]]:
        """ Get all the actions that the player can do.
        
        PossibleMovement;
        PossibleAttack;
        PossibleItem;
        PossibleLever;
        
        Args:
            player (Player): The player who is playing
        
        Returns:
            Dict[List[int, int]]: The actions that the player can do.
        """
        pass