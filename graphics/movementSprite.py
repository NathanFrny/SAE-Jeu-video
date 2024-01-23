from __future__ import annotations
from constant import BOARD_X, CASE_SIZE
import pygame

class MovementSprite(pygame.sprite.Sprite):
    """
    Class that represent all the circles drawn for the actions of the players (red to deplacement action, green to attack and lever action, purple to get an item)
    """
    def __init__(self: MovementSprite, image: str, image_target, location: list[int, int], utility: str = "movement"):
        """
        Initalization of the movement sprite
        Args:
            image (str): the path of the image that we have to draw
            location (list[int, int]): the location of the ItemSprite on the gameboard
            utility (str): the representation of what the ItemSprite is for (movement, action, item, etc...)
        """
        super().__init__()
        self._location = location
        self._image_path = image
        self._image_path_target = image_target
        self._is_target = False
        self._utility = utility
        self._image = pygame.image.load(image)
        self._image = pygame.transform.scale(self._image, (CASE_SIZE, CASE_SIZE))
        self.rect = self._image.get_rect()
        self.rect.x = BOARD_X
        
    
    @property
    def location(self: MovementSprite) -> list[int, int]:
        return self._location
    @location.setter
    def location(self: MovementSprite, location: list[int, int]):
        self._location = location
        
    def set_target(self: MovementSprite):
        self._image = pygame.image.load(self._image_path_target)
        self._image = pygame.transform.scale(self._image, (CASE_SIZE, CASE_SIZE))
        self._is_target = True

    def set_movement(self: MovementSprite):
        self._image = pygame.image.load(self._image_path)
        self._image = pygame.transform.scale(self._image, (CASE_SIZE, CASE_SIZE))
        self._is_target = False


    def is_target(self: MovementSprite):
        """
        return if the item sprite is hovered
        """
        return self._is_target
    
    @property
    def utility(self: MovementSprite):
        return self._utility
    @utility.setter
    def utility(self: MovementSprite, utility: str):
        self._utility = utility
        
    @property
    def image(self: MovementSprite):
        return self._image
    @image.setter
    def image(self: MovementSprite, image: str):
        self._image_path = image
    
    @property
    def image_path(self: MovementSprite):
        return self._image_path
    @image_path.setter
    def image_path(self: MovementSprite, image_path: str):
        self._image_path = image_path
        
    @property
    def image_path_target(self: MovementSprite):
        return self._image_path_target
    @image_path_target.setter
    def image_path_target(self: MovementSprite, image_path: str):
        self._image_path_target = image_path

        