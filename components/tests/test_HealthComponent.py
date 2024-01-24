import unittest
from ..HealthComponent import HealthComponent

class TestHealthComponent(unittest.TestCase):
    def setUp(self):
        self.health_component = HealthComponent(100)
        
    def test_initialization(self):
        self.assertEqual(self.health_component.max_health, 100)
        self.assertEqual(self.health_component.current_health, 100)
        
    def test_take_damage(self):
        self.health_component.take_damage(50)
        self.assertEqual(self.health_component.current_health, 50)
        
    def test_heal(self):
        self.health_component.take_damage(50)
        self.health_component.heal(30)
        self.assertEqual(self.health_component.current_health, 80)
        self.health_component.heal(30)
        self.assertEqual(self.health_component.current_health, 100)
        
    def test_reset_health(self):
        self.health_component.take_damage(50)
        self.health_component.reset_health()
        self.assertEqual(self.health_component.current_health, 100)
        
    def test_is_dead(self):
        self.assertFalse(self.health_component.is_dead())
        self.health_component.take_damage(100)
        self.assertTrue(self.health_component.is_dead())
        
    def test_max_health_setter(self):
        self.health_component.max_health = 150
        self.assertEqual(self.health_component.max_health, 150)
        self.assertEqual(self.health_component.current_health, 100)
        
    def test_current_health_setter(self):
        self.health_component.current_health = 80
        self.assertEqual(self.health_component.current_health, 80)
        self.health_component.current_health = 120
        self.assertEqual(self.health_component.current_health, 100)
        
if __name__ == '__main__':
    unittest.main()