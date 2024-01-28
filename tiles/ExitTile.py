from .Tile import Tile
from .data.DataTiles import TileData
from utils.PyDecoratorFunc import register_tile_type

@register_tile_type("exit")
class ExitTile(Tile):
    def __init__(self, dataTile: TileData):
        super().__init__(dataTile)
        self._is_closed = True

    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def is_closed(self):
        return self._is_closed
    @is_closed.setter
    def is_closed(self, is_closed):
        self._is_closed = is_closed

    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #

    def __str__(self):
        return "Exit"