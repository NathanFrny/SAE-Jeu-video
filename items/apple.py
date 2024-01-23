from __future__ import annotations
from items import Item
from entities import Entity

class Apple(Item):
    """
    The Apple item class which contain all the statistics and advanced functions of the Apple item
    """

    def __init__(self: Apple, image: str, location: list[int, int] = [0,0], value: int = 20, description: str = "Give 20 hp to the player"):
        """
        Initialization of the Apple
        Args:
            image (str): The image path of the apple
            location (list[int, int]) his location on the gameboard
            value (int): The amount of hp to give to the player
            description (str): The description of the item
        """
        super().__init__(image, location, value, description)

    def itemProperties(self: Item, player: Entity):
        """
        The properties of the apple when a player use it
        Args:
            player (Entity): The player that use the apple
        """
        super().itemProperties()
        player.current_health += 20
        if player.current_health > 100:
            player.current_health = 100
        return player
