from .Tile import Tile
from .data.DataTiles import TileData
from utils.PyDecoratorFunc import register_tile_type

@register_tile_type("wall")
class WallTile(Tile):
    def __init__(self, dataTile: TileData):
        super().__init__(dataTile)
        self.__is_walkable = False
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def is_walkable(self) -> bool:
        return self.__is_walkable
    @is_walkable.setter
    def is_walkable(self, is_walkable: bool):
        self.__is_walkable = is_walkable