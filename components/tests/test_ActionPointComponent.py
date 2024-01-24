import unittest
from ..ActionPointComponent import ActionPointComponent

class TestActionPointComponent(unittest.TestCase):
    def setUp(self):
        self.action_point_component = ActionPointComponent(100)
        
    def test_initialization(self):
        self.assertEqual(self.action_point_component.max_action_points, 100)
        self.assertEqual(self.action_point_component.current_action_points, 100)
        
    def test_reset_action_point(self):
        self.action_point_component.use_action_point(50)
        self.action_point_component.reset_action_point()
        self.assertEqual(self.action_point_component.current_action_points, 100)
        
    def test_use_action_point(self):
        self.action_point_component.use_action_point(50)
        self.assertEqual(self.action_point_component.current_action_points, 50)
        
    def test_give_action_point(self):
        self.action_point_component.give_action_point(50)
        self.assertEqual(self.action_point_component.current_action_points, 100)
        
    def test_is_action_point_empty(self):
        self.assertFalse(self.action_point_component.is_action_point_empty())
        self.action_point_component.use_action_point(100)
        self.assertTrue(self.action_point_component.is_action_point_empty())
        
    def test_is_action_point_full(self):
        self.assertTrue(self.action_point_component.is_action_point_full())
        self.action_point_component.use_action_point(50)
        self.assertFalse(self.action_point_component.is_action_point_full())
        
if __name__ == '__main__':
    unittest.main()