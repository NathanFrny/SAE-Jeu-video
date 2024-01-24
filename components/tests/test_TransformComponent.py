import unittest
from ..TransformComponent import TransformComponent

class TestTransformComponent(unittest.TestCase):
    def setUp(self):
        self.transform_component = TransformComponent([0, 0])
        
    def test_initialization(self):
        self.assertEqual(self.transform_component.location, [0, 0])
        
    def test_location_setter(self):
        new_location = [1, 2]
        self.transform_component.location = new_location
        self.assertEqual(self.transform_component.location, new_location)
        
    def test_move(self):
        target = [3, 4]
        self.transform_component.move(target)
        self.assertEqual(self.transform_component.location, target)
        
    def test_get_distance(self):
        target = [5, 6]
        distance = self.transform_component.get_distance(target)
        self.assertEqual(distance, 11)  # abs(0-5) + abs(0-6) = 5 + 6 = 11
        
if __name__ == '__main__':
    unittest.main()