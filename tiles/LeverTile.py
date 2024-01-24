from .Tile import Tile
from .data.DataTiles import TileData

class LeverTile(Tile):
    def __init__(self, dataTile: TileData):
        super().__init__(dataTile)
        self.__isOn = False
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def isOn(self) -> bool:
        return self.__isOn
    @isOn.setter
    def isOn(self, isOn: bool):
        self.__isOn = isOn