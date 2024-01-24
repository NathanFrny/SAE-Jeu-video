import unittest
from pygame import Surface, Rect, sprite
from ..SpriteRendererComponent import SpriteRendererComponent

class TestSpriteRendererComponent(unittest.TestCase):
    def setUp(self):
        self.sprite_renderer = SpriteRendererComponent("images/image.png")
        
    def test_initialization(self):
        self.assertIsInstance(self.sprite_renderer.image, Surface)
        self.assertIsInstance(self.sprite_renderer.rect, Rect)
        self.assertIsInstance(self.sprite_renderer._sprite, sprite.Sprite)
        
    def test_image_resize(self):
        self.sprite_renderer.image_resize((50, 50))
        self.assertEqual(self.sprite_renderer.image.get_size(), (50, 50))
        self.assertEqual(self.sprite_renderer.rect.size, (50, 50))
        self.assertEqual(self.sprite_renderer._sprite.image.get_size(), (50, 50))
        
    def test_image_setter(self):
        new_image = Surface((100, 100))
        self.sprite_renderer.image = new_image
        self.assertEqual(self.sprite_renderer.image, new_image)
        self.sprite_renderer.image_resize(new_image.get_size())
        self.assertEqual(self.sprite_renderer.rect.size, (100, 100))
        self.assertEqual(str(self.sprite_renderer._sprite.image), str(new_image))
        
    def test_rect_setter(self):
        new_rect = Surface((200, 200)).get_rect()
        self.sprite_renderer.rect = new_rect
        self.assertEqual(self.sprite_renderer.rect, new_rect)
        self.assertEqual(self.sprite_renderer._sprite.rect, new_rect)
        
if __name__ == '__main__':
    unittest.main()