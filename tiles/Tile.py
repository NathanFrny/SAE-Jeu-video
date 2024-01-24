from abc import ABC
from .data.DataTiles import TileData

class Tile(ABC):
    def __init__(self, dataTile: TileData):
        self._dataTile: TileData = dataTile
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def dataTile(self) -> TileData:
        return self._dataTile
    @dataTile.setter
    def dataTile(self, dataTile: TileData):
        self._dataTile = dataTile
    
    
    