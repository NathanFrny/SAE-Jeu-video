def register_tile_type(type_name):
    """ Register a tile type in the tile factory

    Args:
        type_name (Tile): the type of the tile
    """
    from tiles import TileFactory
    def decorator(tile_class):
        """ Decorator to register a tile type in the tile factory

        Args:
            tile_class (Tile): the type of the tile

        Returns:
            Tile: the type of the tile
        """
        TileFactory.register_tile_type(type_name, tile_class)
        return tile_class
    return decorator