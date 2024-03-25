from .Entity import Entity
from components import SpriteRendererComponent, TransformComponent, HealthComponent, ActionPointComponent, StrengthComponent

class Monster(Entity):
    
    def __init__(self, image_path: str, health: int, action_point: int, damages: int):
        super().__init__()
        
        self.add_component(SpriteRendererComponent(image_path, self))
        self.add_component(TransformComponent([0,0], self))
        self.add_component(HealthComponent(health, self))
        self.add_component(ActionPointComponent(action_point, self))
        self.add_component(StrengthComponent(damages, self))
        
    # ---------------------------------------------------------------- #
    # ------------------------ Methods ------------------------------- #
    # ---------------------------------------------------------------- #
    
    def update(self):
        """ Update the entity.
        """
        super().update()    
        