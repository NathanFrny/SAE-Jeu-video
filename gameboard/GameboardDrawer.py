from __future__ import annotations
from .Gameboard import Gameboard
from .GraphicGameboard import GraphicGameboard

class GameboardDrawer:
    _instance = None # static variable to hold the singleton instance of the graphic gameboard

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern to ensure that only one instance of the graphic gameboard is created

        Returns:
            GraphicGameboard: the graphic gameboard instance of the game
        """
        if not cls._instance:
            cls._instance = super(GameboardDrawer, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, gameboard: Gameboard, graphic_gameboard: GraphicGameboard):
        self._gameboard = gameboard
        self._graphic_gameboard = graphic_gameboard
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def gameboard(self):
        return self._gameboard
    @gameboard.setter
    def gameboard(self, gameboard):
        self._gameboard = gameboard
        
    @property
    def graphic_gameboard(self):
        return self._graphic_gameboard
    @graphic_gameboard.setter
    def graphic_gameboard(self, graphic_gameboard):
        self._graphic_gameboard = graphic_gameboard
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    
