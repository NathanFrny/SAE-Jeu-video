from .abstract import Entity
from components import HealthComponent, ActionPointComponent, StrengthComponent, TransformComponent, SpriteRendererComponent, CoinsComponent

from components import PlayerActionsComponent
from utils.constants import PLAYER_HEALTH, PLAYER_ACTION_POINT, PLAYER_DAMAGES

class Player(Entity):
    
    def __init__(self, name: str, image_path: str):
        super().__init__()
        
        self.add_component(HealthComponent(PLAYER_HEALTH, self))
        self.add_component(ActionPointComponent(PLAYER_ACTION_POINT, self))
        self.add_component(StrengthComponent(PLAYER_DAMAGES, self))
        self.add_component(TransformComponent([0, 0], self))
        self.add_component(SpriteRendererComponent(image_path, self))
        self.add_component(CoinsComponent(0, self))
        self.add_component(PlayerActionsComponent(self))
        # ------------------------ #
        
        self._name = name
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Methods ---------------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    def update(self):
        """ Update the entity.
        """
        super().update()
    
    def __str__(self) -> str:
        """ Display the name of the entity on the console and all his component.

        Returns:
           str : The name of the entity
        """
        components_str = ', '.join(str(component) for component in self._components)
        return f'{self._name} ({components_str})'
        
    
    