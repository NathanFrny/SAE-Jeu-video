from __future__ import annotations
from abc import ABC, abstractmethod


class Item(ABC):
    """
    The Item abstract class which contain all the statistics of an item
    """
    
    def __init__(self: Item, image: str, location: list[int, int] = [0,0], value: int = 20, description: str = "Default item"):
        """
        Initialization of an Item
        Args:
            image (str): The image path of the item
            location (list[int, int]): his location on the gameboard
            value (int): His amount value of bonus statistics
            description (str): The description of the item
        """
        self._location = location
        self._image = image
        self._value = value
        self._description = description
        
    def __repr__(self: Item) -> str:
        """
        The console message that is writtent when an item is print
        """
        return f"<class Item: {self._description}. value = {self._value}"
    
    @property
    def location(self: Item) -> list[int, int]:
        return self._location
    @location.setter
    def location(self: Item, location: list[int, int]):
        self._location = location

    @property
    def value(self: Item) -> int:
        return self._value
    @value.setter
    def value(self: Item, value: int):
        self._value = value
    
    @property
    def description(self: Item) -> str:
        return self._description
    @description.setter
    def description(self: Item, description: str):
        self._description = description

    @property
    def image(self: Item):
        return self._image
    @image.setter
    def image(self: Item, image: str):
        self._image = image
        
        
    
    @abstractmethod
    def itemProperties(self: Item):
        """
        An abstract method of the item properties when it is used by a player
        """
        pass
    
    
    def equals(self: Item, item: Item):
        """
        The equals method of an item which return if an item is equal to another one (by  checking if they have the same class name)
        Args:
            item(Item): The other item that we have to check
        """
        return self.__class__.__name__ == item.__class__.__name__