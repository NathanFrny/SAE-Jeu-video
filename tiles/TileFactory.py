from .data.DataTiles import TileData
from .Tile import Tile

class TileFactory:
    
    tile_types = {}
    
    @classmethod
    def register_tile_type(cls, type: str, tile_class):
        """ Enregistre un type de tuile avec la classe correspondante dans la factory. """
        cls.tile_types[type] = tile_class
    
    @staticmethod
    def create_tile(type: str, dataTile: TileData) -> Tile:
        """ Create a tile from the given type and data

        Args:
            type (str): the type of the tile
            dataTile (TileData): the data of the tile

        Returns:
            Tile: the created tile
        """
        tile_class = TileFactory.tile_types.get(type)
        
        if not tile_class:
            print(TileFactory.tile_types)
            raise ValueError(f"Type de tuile non reconnu: {type}")
        
        return tile_class(dataTile)
    
