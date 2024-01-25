from __future__ import annotations
from utils.constants import NB_COL, NB_ROW, CASE_SIZE, BOARD_X
from pygame import image, transform, Surface

class GraphicGameboard:
    _instance = None # static variable to hold the singleton instance of the graphic gameboard

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern to ensure that only one instance of the graphic gameboard is created

        Returns:
            GraphicGameboard: the graphic gameboard instance of the game
        """
        if not cls._instance:
            cls._instance = super(GraphicGameboard, cls).__new__(cls)
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
    
    def get_image(self, row, col) -> Surface:
        """ Get the image at the given position

        Args:
            row (int): the row of the image
            col (int): the column of the image

        Returns:
            Surface: the image at the given position
        """
        return self._graphic_grid[row][col]
    
    def set_image(self, row, col, image_path: str):
        """ Set the image at the given position

        Args:
            row (int): the row of the image
            col (int): the column of the image
            image_path (str): the image to load and set
        """
        img = image.load(image_path)
        img = transform.scale(img, (CASE_SIZE, CASE_SIZE))
        self._graphic_grid[row][col] = img
        
    def draw(self, screen):
        for row in range(self.nb_row):
            for col in range(self.nb_col):
                x = BOARD_X + col * CASE_SIZE
                y = row * CASE_SIZE
                screen.blit(self._graphic_grid[row][col], (x, y))
        
    def __str__(self) -> str:
        for row in range(self._nb_row):
            for col in range(self._nb_col):
                print(self._graphic_grid[row][col], end=" ")
            print()
        return ''
    
    
            
    