from __future__ import annotations
from utils.constants import NB_COL, NB_ROW

class GraphicGameboard:
    _instance = None # static variable to hold the singleton instance of the graphic gameboard

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern to ensure that only one instance of the graphic gameboard is created

        Returns:
            GraphicGameboard: the graphic gameboard instance of the game
        """
        if not cls._instance:
            cls._instance = super(GraphicGameboard, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self._nb_row, self._nb_col = NB_ROW, NB_COL
        self._graphic_grid = [[None for _ in range(self._nb_col)] for _ in range(self._nb_row)]
        
    
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def graphic_grid(self):
        return self._graphic_grid
    @graphic_grid.setter
    def graphic_grid(self, graphic_grid):
        self._graphic_grid = graphic_grid
    
    @property
    def nb_row(self):
        return self._nb_row
    @nb_row.setter
    def nb_row(self, nb_row):
        self._nb_row = nb_row
    
    @property
    def nb_col(self):
        return self._nb_col
    @nb_col.setter
    def nb_col(self, nb_col):
        self._nb_col = nb_col
        
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    def get_tile(self, row, col):
        """ Get the tile at the given position

        Args:
            row (int): the row of the tile
            col (int): the column of the tile

        Returns:
            Tile: the tile at the given position
        """
        return self._graphic_grid[row][col]
    
    def set_tile(self, row, col, tile):
        """ Set the tile at the given position

        Args:
            row (int): the row of the tile
            col (int): the column of the tile
            tile (Tile): the tile to set
        """
        self._graphic_grid[row][col] = tile
    