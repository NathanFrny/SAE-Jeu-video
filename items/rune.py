from __future__ import annotations
from items import Item
from entities import Entity

class Rune(Item):
    """
    The Rune item class which contain all the statistics and advanced functions of the Rune item
    """

    def __init__(self: Rune, image: str, location: list[int, int] = [0,0], value: int = 20, description: str = "Give Damage bonus to the player"):
        """
        Initialization of the Rune
        Args:
            image (str): The image path of the rune
            location (list[int, int]) his location on the gameboard
            value (int): The amount of bonus damages to give to the player
            description (str): The description of the item
        """
        super().__init__(image, location, value, description)

    

    def itemProperties(self: Rune, player: Entity):
        """
        The properties of the rune when a player use it
        Args:
            player (Entity): The player that use the rune
        """
        super().itemProperties()
        player.damage += 10
        return player