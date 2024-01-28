from __future__ import annotations
from typing import List
from entities import Player
from .GraphicGameboard import GraphicGameboard
from .RoomBuilder import RoomBuilder

class GameboardAdapter:
    _instance = None # static variable to hold the singleton instance of the graphic gameboard

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern to ensure that only one instance of the graphic gameboard is created

        Returns:
            GraphicGameboard: the graphic gameboard instance of the game
        """
        if not cls._instance:
            cls._instance = super(GameboardAdapter, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, players: List[Player]):        
        self._room_builder = RoomBuilder(players)
        self._gameboard = self._room_builder.room
        self._graphic_gameboard = self._room_builder.graphic_room
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def room_builder(self):
        return self._room_builder
    @room_builder.setter
    def room_builder(self, room_builder):
        self._room_builder = room_builder
        
    @property
    def graphic_gameboard(self):
        return self._graphic_gameboard
    @graphic_gameboard.setter
    def graphic_gameboard(self, graphic_gameboard):
        self._graphic_gameboard = graphic_gameboard
        
    @property
    def gameboard(self):
        return self._gameboard
    @gameboard.setter
    def gameboard(self, gameboard):
        self._gameboard = gameboard
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    def draw(self):
        """ Draw the gameboard
        """
        self.room_builder.build()