from __future__ import annotations
from cases import Case
from entities import Entity
from items import Apple, Feather, Rune
from random import choice
from constant import ITEMS_LIST, APPLE, FEATHER, RUNE

class Market(Case):
    """
    The Market class that represent the market cell on the gameboard (A market cell allow player to buy an item)
    """
    
    def __init__(self: Market, pos: list[int, int], tile: str, entity: Entity = None):
        """
        Initialization of the Water cell
        Args:
            pos (list[int, int]): The position of the water cell on the gameboard
            tile (str): The image path of the water
            entity (Entity|None): The entity that is on the cell
        """
        super().__init__(pos, tile, entity)

    
    def buyRandomItem(self: Market, player: Entity):
        """
        When a player is on a market cell and he have enought money, he buy a random item
        Args:
            player (Entity): The player that is on the market cell
        """
        if len(player.inventory) <= 3 and player.coins >= 20:
            match(choice(ITEMS_LIST)):
                case "apple":
                    apple = Apple(APPLE)
                    player.inventory.append(apple)
                    player.coins -= apple.value
                case "feather":
                    feather = Feather(FEATHER)
                    player.inventory.append(feather)
                    player.coins -= feather.value
                case "rune":
                    rune = Rune(RUNE)
                    player.inventory.append(rune)
                    player.coins -= rune.value