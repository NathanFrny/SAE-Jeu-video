from .Gameboard import Gameboard
from .GraphicGameboard import GraphicGameboard
from tiles import TileFactory, GroundTile, WallTile
from tiles.data.DataTiles import *
from random import shuffle, randint

class RoomBuilder:
    """ This class is used to build a room
    """
    
    def __init__(self):
        """ Initialize the room builder
        """
        self._room = Gameboard()
        self._graphic_room = GraphicGameboard()
        self._tile_factory = TileFactory()
        
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
        
    @property
    def tile_factory(self):
        return self._tile_factory
    @tile_factory.setter
    def tile_factory(self, tile_factory):
        self._tile_factory = tile_factory
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    def reset(self):
        """ Reset the room to a new one
        """
        self._room = Gameboard()
        
    # --- Tiles generation methods --- #
    
    def ground_initialization(self):
        """ Initialize the ground of the room
        """
        for row in range(self._room.nb_row):
            for col in range(self._room.nb_col):
                tile = self.room.get_tile(row, col)
                image_variants = tile.data_tile.variants["full"]
                image = tile.data_tile.random_tile(image_variants)
                self._graphic_room.set_image(row, col, image)
        
    def set_walls(self):
        """ Set the walls of the room
        """
        self.initialize_walls()
        self.generate_walls()
    
    # -------------------------------- #
    
    # --- Walls helper methods --- #
    
    def initialize_walls(self):
        """ Initialize the walls at the border of the room
        """
        for row in range(self._room.nb_row):
            for col in range(self._room.nb_col):
                if row == 0 or row == self._room.nb_row - 1 or col == 0 or col == self._room.nb_col - 1: # if the tile is on the border of the room
                    wall_tile = self._tile_factory.create_tile("wall", WallTileData()) # create a wall tile
                    wall_image_variants = wall_tile.dataTile.variants["full"]
                    image = wall_tile.data_tile.random_tile(wall_image_variants)
                    self._room.set_tile(row, col, wall_tile)
                    self._graphic_room.set_image(row, col, image)
                    
    def generate_walls(self):
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if randint(1, 4) == 1:  # 1 chance sur 4 de placer un mur
                    self.set_wall_tile(row, col)
                    if not self.ensure_global_connectivity():
                        self.set_ground_tile(row, col)  # Retour si la connectivité est rompue


    def ensure_global_connectivity(self):
        # Choisissez un point de départ sur une GroundTile
        start_row, start_col = self.find_ground_tile()

        # Utilisez BFS ou DFS pour parcourir toutes les GroundTile accessibles à partir de ce point
        visited = self.traverse(start_row, start_col)

        # Vérifiez si toutes les GroundTile ont été visitées
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if not isinstance(self._room.get_tile(row, col), WallTile) and not visited[row][col]:
                    return False  # Une GroundTile n'est pas accessible

        return True
    
    def traverse(self, start_row, start_col):
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
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if not isinstance(self._room.get_tile(row, col), WallTile):
                    return row, col
        raise ValueError("Aucune GroundTile trouvée pour démarrer la vérification de la connectivité.")

            
    def set_ground_tile(self, row: int, col: int):
        ground_tile = self._tile_factory.create_tile("ground", GroundTileData())
        self._room.set_tile(row, col, ground_tile)
        ground_image_variant = ground_tile.dataTile.variants["full"]
        image = ground_tile.dataTile.random_tile(ground_image_variant)
        self._graphic_room.set_image(row, col, image)

    def set_wall_tile(self, row: int, col: int):
        wall_tile = self._tile_factory.create_tile("wall", WallTileData())
        self._room.set_tile(row, col, wall_tile)
        wall_image_variants = wall_tile.dataTile.variants["full"]
        image = wall_tile.dataTile.random_tile(wall_image_variants)
        self._graphic_room.set_image(row, col, image)


        
            
        