from typing import Type
from abc import ABC, abstractmethod
from pygame import Surface
from components import Component, SpriteRendererComponent

class Entity(ABC):
    """ Abstract class for all entities.

    Args:
        ABC : Abstract class
    """
    
    def __init__(self, components: list[Component]):
        """ Constructor of the Entity class.

        Args:
            components (list[Component]): The list of components of the entity
        """
        # private attributes
        self.__components = components
        
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def components(self):
        return self.__components
    @components.setter
    def components(self, components: list[Component]):
        self.__components = components
        
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    # -- Abstract methods -- #
    
    @abstractmethod
    def update(self):
        """ Update the entity.
        """
        pass
    
    # -- Concrete methods -- #
    
    def add_component(self, component: Component):
        """ Add a component to the entity.

        Args:
            component (Component): The component to add
        """
        self.__components.append(component)
        
    def get_component(self, component_type: Type[Component]) -> Component:
        """ Get a component from the entity.

        Args:
            component_type (Type[Component]): The type of the component to get

        Returns:
            Component: The component of the entity
        """
        for component in self.__components:
            if isinstance(component, component_type):
                return component
            
    def has_component(self, component_type: Type[Component]) -> bool:
        """ Check if the entity has a component.

        Args:
            component_type (Type[Component]): The type of the component to check

        Returns:
            bool: True if the entity has the component, False otherwise
        """
        for component in self.__components:
            if isinstance(component, component_type):
                return True
        return False
    
    
    
    