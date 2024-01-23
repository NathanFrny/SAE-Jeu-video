from __future__ import annotations
from items import Item
from constant import BOARD_X, CASE_SIZE
import pygame



class ItemSprite(pygame.sprite.Sprite):
    """
    The item sprite which allow to draw an item to the graphic interface
    """
    
    def __init__(self: ItemSprite, item: Item, location: list[int, int] = [0,0]):
        """
        Initialization of the item sprite
        Args:
            item (Item): The item that is represented in the item sprite
            location (list[int, int]): The location of the item in the gameboard
        """
        super().__init__()
        self._item = item
        self._location = location
        self._image = pygame.image.load(item._image)
        self._image = pygame.transform.scale(self._image, (CASE_SIZE, CASE_SIZE))
        self.rect = self._image.get_rect()
        self.rect.x = BOARD_X
        
    
    @property
    def item(self: ItemSprite) -> Item:
        return self._item
    @item.setter
    def item(self: ItemSprite, item: Item):
        self._item = item
        
    @property
    def location(self: ItemSprite) -> list[int, int]:
        return self._location
    @location.setter
    def location(self: ItemSprite, location: list[int, int]):
        self._location = location
        
    @property
    def image(self: ItemSprite):
        return self._image
    @image.setter
    def image(self: ItemSprite, image: str):
        self._image = pygame.image.load(image)
        self._image = pygame.transform.scale(self._image, (CASE_SIZE, CASE_SIZE))
        
    
    