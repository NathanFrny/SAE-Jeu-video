from .Tile import Tile
from .data.DataTiles import TileData

class MarketTile(Tile):
    def __init__(self, dataTile: TileData):
        super().__init__(dataTile)
        