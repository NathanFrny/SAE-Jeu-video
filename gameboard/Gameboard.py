from __future__ import annotations
from utils.constants import NB_COL, NB_ROW
from tiles import GroundTile

class Gameboard:
    _instance = None # static variable to hold the singleton instance of the gameboard

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern to ensure that only one instance of the gameboard is created

        Returns:
            Gameboard: the gameboard instance of the game
        """
        if not cls._instance:
            cls._instance = super(Gameboard, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self._nb_row, self._nb_col = NB_ROW, NB_COL
        self._grid = [[GroundTile() for _ in range(self._nb_col)] for _ in range(self._nb_row)]
        
    
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def grid(self):
        return self._grid
    @grid.setter
    def grid(self, grid):
        self._grid = grid
        
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
        return self._grid[row][col]
    
    def set_tile(self, row, col, tile):
        """ Set the tile at the given position

        Args:
            row (int): the row of the tile
            col (int): the column of the tile
            tile (Tile): the tile to set
        """
        self._grid[row][col] = tile
        
    def get_neighbours(self, row, col):
        """ Get the neighbours of the tile at the given position
        """
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.is_on_board(row + i, col + j) and (i != 0 or j != 0)):
                    neighbours.append(self._grid[row + i][col + j])
        return neighbours
        
    def is_on_board(self, row, col):
        """ Check if the given position is on the board

        Args:
            row (int): the row of the position
            col (int): the column of the position

        Returns:
            bool: True if the position is on the board, False otherwise
        """
        return 0 <= row < self._nb_row and 0 <= col < self._nb_col
        
    
        
        
    