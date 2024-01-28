from .Component import Component
from utils.constants import PLAYER_MAX_COINS

class CoinsComponent(Component):
    """ CoinsComponent of the player.

    Args:
        Component (Component): The parent class representing a component
    """

    def __init__(self, coins: int, parent_entity):
        """ Constructor of the CoinsComponent class.

        Args:
            coins (int): The number of coins of the player
        """
        super().__init__(parent_entity)
        self._coins = coins
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self, coins: int):
        self._coins = coins
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    def update(self):
        self._coins += 1

    def add_coins(self, coins: int):
        """ Add coins to the player.

        Args:
            coins (int): The number of coins the player get
        """
        self._coins += coins
        if (self._coins > PLAYER_MAX_COINS):
            self._coins = PLAYER_MAX_COINS
    
    def remove_coins(self, coins: int):
        """ Remove coins to the player.

        Args:
            coins (int): The number of coins the player lose
        """
        self._coins -= coins
        if (self._coins < 0):
            self._coins = 0
            
    
    def __str__(self) -> str:
        """ Display the number of coins of the player on the console.

        Returns:
            str : The number of coins of the player
        """
        return f'Coins Component: {self._coins} coins'