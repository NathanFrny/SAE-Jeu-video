from .Tile import Tile
from .data.DataTiles import TileData
from utils.PyDecoratorFunc import register_tile_type

@register_tile_type("exit")
class ExitTile(Tile):
    def __init__(self, dataTile: TileData):
        super().__init__(dataTile)