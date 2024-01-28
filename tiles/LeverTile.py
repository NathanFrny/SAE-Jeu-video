from .Tile import Tile
from .data.DataTiles import TileData
from utils.PyDecoratorFunc import register_tile_type

@register_tile_type("lever")
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

    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
        
    def __str__(self):
        return "lever"