import unittest
from ..CoinsComponent import CoinsComponent
from utils.constants import PLAYER_MAX_COINS

class TestCoinsComponent(unittest.TestCase):
    def setUp(self):
        self.coins_component = CoinsComponent(0)
        
    def test_initialization(self):
        self.assertEqual(self.coins_component.coins, 0)
        
    def test_coins_setter(self):
        new_coins = 10
        self.coins_component.coins = new_coins
        self.assertEqual(self.coins_component.coins, new_coins)
        
    def test_add_coins(self):
        self.coins_component.add_coins(5)
        self.assertEqual(self.coins_component.coins, 5)
        
        self.coins_component.add_coins(1000)
        self.assertEqual(self.coins_component.coins, PLAYER_MAX_COINS)
        
    def test_remove_coins(self):
        self.coins_component.coins = 20
        self.coins_component.remove_coins(5)
        self.assertEqual(self.coins_component.coins, 15)
        
        self.coins_component.remove_coins(20)
        self.assertEqual(self.coins_component.coins, 0)
        
if __name__ == '__main__':
    unittest.main()