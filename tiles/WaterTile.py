from .Tile import Tile
from .data.DataTiles import TileData
from utils.PyDecoratorFunc import register_tile_type

@register_tile_type("water")
class WaterTile(Tile):
    def __init__(self, dataTile: TileData):
        super().__init__(dataTile)
        
    def __str__(self):
        return "Water"
        