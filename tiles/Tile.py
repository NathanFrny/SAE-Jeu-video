from abc import ABC
from .data.DataTiles import TileData

class Tile(ABC):
    def __init__(self, dataTile: TileData):
        self._data_tile: TileData = dataTile
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def data_tile(self) -> TileData:
        return self._data_tile
    @data_tile.setter
    def dataTile(self, dataTile: TileData):
        self._data_tile = dataTile
    
    
    