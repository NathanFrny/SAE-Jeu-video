from __future__ import annotations
from typing import List
from entities import Player, Entity
from tiles import WallTile, LeverTile, TrapTile
from components import TransformComponent
from .GraphicGameboard import GraphicGameboard
from .RoomBuilder import RoomBuilder
from random import choice

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
    def graphic_gameboard(self, graphic_gameboard: GraphicGameboard):
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
        
    def spawn_entities_randomly(self, entities_list: list[Entity]):
        available_tiles = self.get_available_tiles()
        for entity in entities_list:
            position = choice(available_tiles)
            entity.get_component(TransformComponent).position = position
    
    def get_available_tiles(self):
        """ Get all the available tiles on the gameboard.

        Returns:
            List[Tile]: All the available tiles on the gameboard
        """
        grid = self.gameboard.grid
        available_list = []
        for row in range(self.gameboard.nb_row):
            for col in range(self.gameboard.nb_col):
                tile = grid[row][col]
                if not isinstance(tile, WallTile) and not isinstance(tile, LeverTile) and not isinstance(tile, TrapTile) and not tile.is_player_on and not tile.entity:
                    available_list.append([row, col])
                    
        return available_list