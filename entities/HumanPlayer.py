from utils.constants import PLAYER_HEALTH, PLAYER_ACTION_POINT, PLAYER_DAMAGES
from components import Component, HealthComponent, ActionPointComponent, StrengthComponent, TransformComponent, SpriteRendererComponent, CoinsComponent
from .Player import Player

class HumanPlayer(Player):
    def __init__(self, name: str, image_path: str, components: list[Component] | Component = []):
        super().__init__(name, image_path, components)
        
        # Define default components
        default_components = [
            
        ]

        # Check and add default components
        for component_class, default_value in default_components:
            if not self.has_component(component_class):
                self.add_component(component_class(default_value))
        
        