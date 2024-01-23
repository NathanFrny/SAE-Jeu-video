from __future__ import annotations
from items import Item
from entities import Entity

class Feather(Item):
    """
    The Feather item class which contain all the statistics and advanced functions of the Feather item
    """

    def __init__(self: Feather, image: str, location: list[int, int] = [0,0], value: int = 10, description: str = "Give a bonus action point to the player"):
        """
        Initialization of the Feather
        Args:
            image (str): The image path of the feather
            location (list[int, int]) his location on the gameboard
            value (int): The amount of action point to give to the player
            description (str): The description of the item
        """
        super().__init__(image, location, value, description)

    

    def itemProperties(self: Item, player: Entity):
        """
        The properties of the feather when a player use it
        Args:
            player (Entity): The player that use the feather
        """
        super().itemProperties()
        player.current_action_point += 2
        return player