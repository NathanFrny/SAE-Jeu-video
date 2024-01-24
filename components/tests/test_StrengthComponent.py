import unittest
from ..StrengthComponent import StrengthComponent

class TestStrengthComponent(unittest.TestCase):
    def setUp(self):
        self.strength_component = StrengthComponent(10)
        
    def test_initialization(self):
        self.assertEqual(self.strength_component.initial_strength, 10)
        self.assertEqual(self.strength_component.strength, 10)
        
    def test_reset_strength(self):
        self.strength_component.decrease_strength(5)
        self.strength_component.reset_strength()
        self.assertEqual(self.strength_component.strength, 10)
        
    def test_increase_strength(self):
        self.strength_component.increase_strength(5)
        self.assertEqual(self.strength_component.strength, 15)
        
    def test_decrease_strength(self):
        self.strength_component.decrease_strength(5)
        self.assertEqual(self.strength_component.strength, 5)
        
if __name__ == '__main__':
    unittest.main()