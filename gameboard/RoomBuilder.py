from .Gameboard import Gameboard
from .GraphicGameboard import GraphicGameboard
from tiles import TileFactory, GroundTile, WallTile
from tiles.data.DataTiles import *
from random import shuffle, randint
from gameboard.rooms.BasicRoomStrategy import BasicRoomStrategy

class RoomBuilder:
    """ This class is used to build a room
    """
    
    def __init__(self):
        """ Initialize the room builder
        """
        self._room = Gameboard()
        self._graphic_room = GraphicGameboard()
        self._strategy = BasicRoomStrategy(self._room, self._graphic_room)
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def room(self):
        return self._room
    @room.setter
    def room(self, room):
        self._room = room
        
    @property
    def graphic_room(self):
        return self._graphic_room
    @graphic_room.setter
    def graphic_room(self, graphic_room):
        self._graphic_room = graphic_room
        
    @property
    def strategy(self):
        return self._strategy
    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    def reset(self):
        """ Reset the room to a new one
        """
        self._room = Gameboard()
        
    def build(self):
        """ Build the room
        """
        self._strategy.initialize_room()
        self._strategy.set_walls()
        self._strategy.set_ground()

    


        
            
        