import unittest
from entities import Player
from components import HealthComponent, ActionPointComponent, StrengthComponent, TransformComponent, SpriteRendererComponent, CoinsComponent

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("John", "images/image.png")
        print(self.player)
        
    def test_initialization(self):
        self.assertEqual(self.player.name, "John")
        self.assertIsInstance(self.player.get_component(HealthComponent), HealthComponent)
        self.assertIsInstance(self.player.get_component(ActionPointComponent), ActionPointComponent)
        self.assertIsInstance(self.player.get_component(StrengthComponent), StrengthComponent)
        self.assertIsInstance(self.player.get_component(TransformComponent), TransformComponent)
        self.assertIsInstance(self.player.get_component(SpriteRendererComponent), SpriteRendererComponent)
        self.assertIsInstance(self.player.get_component(CoinsComponent), CoinsComponent)
        
    def test_name_setter(self):
        self.player.name = "Jane"
        self.assertEqual(self.player.name, "Jane")
        
if __name__ == '__main__':
    unittest.main()