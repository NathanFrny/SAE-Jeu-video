from .abstract import Entity
from components import Component, HealthComponent, ActionPointComponent, StrengthComponent, TransformComponent, SpriteRendererComponent, CoinsComponent
from utils.constants import PLAYER_HEALTH, PLAYER_ACTION_POINT, PLAYER_DAMAGES

class Player(Entity):
    
    def __init__(self, name: str, image_path: str, components: list[Component] = []):
        super().__init__(components)
        
        # Define default components
        default_components = [
            (HealthComponent, PLAYER_HEALTH),
            (ActionPointComponent, PLAYER_ACTION_POINT),
            (StrengthComponent, PLAYER_DAMAGES),
            (TransformComponent, [0, 0]),
            (SpriteRendererComponent, image_path),
            (CoinsComponent, 0)
        ]

        # Check and add default components
        for component_class, default_value in default_components:
            if not self.has_component(component_class):
                self.add_component(component_class(default_value))
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
        pass
    
    def __str__(self) -> str:
        """ Display the name of the entity on the console and all his component.

        Returns:
           str : The name of the entity
        """
        components_str = ', '.join(str(component) for component in self._components)
        return f'{self._name} ({components_str})'
        
    
    