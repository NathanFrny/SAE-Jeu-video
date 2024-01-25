from .RoomGenerationStrategy import RoomGenerationStrategy
from .configuration.GroundConfigurationStrategy import GroundConfigurationStrategy
from gameboard import Gameboard, GraphicGameboard
from tiles.data.DataTiles import *
from tiles import GroundTile, WallTile
from random import randint
from tiles import TileFactory

class BasicRoomStrategy(RoomGenerationStrategy):
    
    def __init__(self, room: Gameboard, graphic_room: GraphicGameboard):
        """ Initialize the strategy
        """
        self._room = room
        self._graphic_room = graphic_room
        self._tile_factory = TileFactory()
        self._tile_config_strategies = {
            'ground': GroundConfigurationStrategy(room),
        }
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def room(self):
        return self._room
    @room.setter
    def room(self, room):
        self._room = room
        
    @property
    def graphic_room(self):
        return self._graphic_room
    @graphic_room.setter
    def graphic_room(self, graphic_room):
        self._graphic_room = graphic_room
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    # --- Initialization methods --- #
    
    def initialize_room(self):
        """ Initialize the room
        """
        self.ground_initialization()
        self.walls_initialization()
        
    def ground_initialization(self):
        """ Initialize the ground of the room
        """
        for row in range(self._room.nb_row):
            for col in range(self._room.nb_col):
                tile = self.room.get_tile(row, col)
                image_variants = tile.data_tile.variants["full"]
                image = tile.data_tile.random_tile(image_variants)
                self._graphic_room.set_image(row, col, image)
                
    def walls_initialization(self):
        """ Initialize the walls of the room
        """
        for row in range(self._room.nb_row):
            for col in range(self._room.nb_col):
                if row == 0 or row == self._room.nb_row - 1 or col == 0 or col == self._room.nb_col - 1: # if the tile is on the border of the room
                    wall_tile = self._tile_factory.create_tile("wall", WallTileData()) # create a wall tile
                    wall_image_variants = wall_tile.dataTile.variants["full"]
                    image = wall_tile.data_tile.random_tile(wall_image_variants)
                    self._room.set_tile(row, col, wall_tile)
                    self._graphic_room.set_image(row, col, image)
                    
    # --- Walls generation methods --- #
    
    def set_walls(self):
        """ Initialize the walls of the room with correct sprites based on ground positions.
        """
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if randint(1, 4) == 1:  
                    self.set_wall_tile(row, col)
                    if not self.ensure_global_connectivity():
                        self.set_ground_tile(row, col)  


    def ensure_global_connectivity(self) -> bool:
        """ Check if the room is globally connected (i.e. there is no ground tile that is not connected to the rest of the room).

        Returns:
            bool: True if the room is globally connected, False otherwise
        """
        start_row, start_col = self.find_ground_tile()

        visited = self.traverse(start_row, start_col)

        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if not isinstance(self._room.get_tile(row, col), WallTile) and not visited[row][col]:
                    return False 

        return True
    
    def traverse(self, start_row: int, start_col: int):
        """ Traverse the room from a given position and return a matrix of visited tiles.

        Args:
            start_row (int): The row of the starting position
            start_col (int): The column of the starting position

        Returns:
            list[list[bool]]: A matrix of visited tiles
        """
        visited = [[False for _ in range(self._room.nb_col)] for _ in range(self._room.nb_row)]
        stack = [(start_row, start_col)]

        while stack:
            row, col = stack.pop()
            if not visited[row][col]:
                visited[row][col] = True
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row, new_col = row + dx, col + dy
                    if 1 <= new_row < self._room.nb_row-1 and 1 <= new_col < self._room.nb_col-1:
                        if not isinstance(self._room.get_tile(new_row, new_col), WallTile):
                            stack.append((new_row, new_col))

        return visited

    def find_ground_tile(self):
        """ Find a ground tile to start the connectivity check.

        Returns:
            tuple(int, int): The row and column of the ground tile
        """
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if not isinstance(self._room.get_tile(row, col), WallTile):
                    return row, col
        raise ValueError("Aucune GroundTile trouvée pour démarrer la vérification de la connectivité.")

            
    def set_ground_tile(self, row: int, col: int):
        """ Set a ground tile at the given position.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile
        """
        ground_tile = self._tile_factory.create_tile("ground", GroundTileData())
        self._room.set_tile(row, col, ground_tile)
        ground_image_variant = ground_tile.dataTile.variants["full"]
        image = ground_tile.dataTile.random_tile(ground_image_variant)
        self._graphic_room.set_image(row, col, image)

    def set_wall_tile(self, row: int, col: int):
        """ Set a wall tile at the given position.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile
        """
        wall_tile = self._tile_factory.create_tile("wall", WallTileData())
        self._room.set_tile(row, col, wall_tile)
        wall_image_variants = wall_tile.dataTile.variants["full"]
        image = wall_tile.dataTile.random_tile(wall_image_variants)
        self._graphic_room.set_image(row, col, image)
        
    
    # --- Ground generation methods --- #
    
    def set_ground(self):
        """ Initialize the ground of the room with correct sprites based on wall positions. """
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                self.set_ground_sprite(row, col)

    def set_ground_sprite(self, row: int, col: int):
        """ Set the sprite for a ground tile based on its configuration. 
        
            Args:
                row (int): the row of the tile
                col (int): the column of the tile
        """
        tile = self._room.get_tile(row, col)
        if isinstance(tile, GroundTile):
            configuration_strategy = self._tile_config_strategies.get('ground')
            if configuration_strategy:
                configuration_key = configuration_strategy.get_configuration_key(row, col)
                if configuration_key in tile.dataTile.variants:
                    image = tile.dataTile.random_tile(tile.dataTile.variants[configuration_key])
                else:
                    image = tile.dataTile.random_tile(tile.dataTile.variants["full"])
                self._graphic_room.set_image(row, col, image)