from .Gameboard import Gameboard
from .GraphicGameboard import GraphicGameboard
from tiles.data.DataTiles import *
from entities import Player
from utils.constants import LEVER_COUNT
from gameboard.rooms.BasicRoomStrategy import BasicRoomStrategy

class RoomBuilder:
    """ This class is used to build a room
    """
    
    def __init__(self, players: List[Player]):
        """ Initialize the room builder
        """
        self._room = Gameboard()
        self._graphic_room = GraphicGameboard()
        self._strategy = BasicRoomStrategy(self._room, self._graphic_room)
        self._players = players
        
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

    @property
    def players(self):
        return self._players
    @players.setter
    def players(self, players):
        self._players = players
        
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
        self._strategy.set_traps()
        self._strategy.set_water()
        self._strategy.set_exit()
        self._strategy.set_levers(LEVER_COUNT)
        self._strategy.set_portals()
        self._strategy.set_market()
        self._strategy.set_ground()
        self._strategy.set_players(self._players)

    
    


        
            
        