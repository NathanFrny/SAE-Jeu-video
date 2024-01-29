from .Entity import Entity
from components import SpriteRendererComponent, TransformComponent, HealthComponent

class Monster(Entity):
    
    def __init__(self, image_path: str):
        super().__init__()
        
        self.add_component(SpriteRendererComponent(image_path, self))
        self.add_component(TransformComponent([0,0], self))
        self.add_component(HealthComponent(100, self))
        
        
        
        