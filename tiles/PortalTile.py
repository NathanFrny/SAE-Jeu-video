from __future__ import annotations
from .Tile import Tile
from .data.DataTiles import TileData

class PortalTile(Tile):
    def __init__(self, dataTile: TileData):
        super().__init__(dataTile)
        self.__target: PortalTile = None
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def target(self) -> PortalTile:
        return self.__target
    @target.setter
    def target(self, target: PortalTile):
        self.__target = target