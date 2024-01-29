from abc import ABC
from .data.DataTiles import TileData
from entities import Monster

class Tile(ABC):
    def __init__(self, dataTile: TileData):
        self._data_tile: TileData = dataTile
        self._is_player_on: bool = False
        self._entity: Monster = None
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def data_tile(self) -> TileData:
        return self._data_tile
    @data_tile.setter
    def dataTile(self, dataTile: TileData):
        self._data_tile = dataTile

    @property
    def is_player_on(self) -> bool:
        return self._is_player_on
    @is_player_on.setter
    def is_player_on(self, isPlayerOn: bool):
        self._is_player_on = isPlayerOn
        
    @property
    def entity(self) -> Monster:
        return self._entity
    @entity.setter
    def entity(self, entity: Monster):
        self._entity = entity
    
    
    