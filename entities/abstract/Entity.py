from typing import Type
from abc import ABC, abstractmethod
from components import Component

class Entity(ABC):
    """ Abstract class for all entities.

    Args:
        ABC : Abstract class
    """
    
    def __init__(self, components: list[Component] | Component = []):
        """ Constructor of the Entity class.

        Args:
            components (list[Component] | Component): The list of components of the entity or a single component (convert into a list)
        """
        # If components is a single Component, convert it to a list
        if isinstance(components, Component):
            components = [components]
        
        # protected attributes
        self._components = components
        
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def components(self):
        return self._components
    @components.setter
    def components(self, components: list[Component]):
        self._components = components
        
        
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
        if not self.has_component(type(component)):
            self._components.append(component)
        
    def get_component(self, component_type: Type[Component]) -> Component:
        """ Get a component from the entity.

        Args:
            component_type (Type[Component]): The type of the component to get

        Returns:
            Component: The component of the entity
        """
        for component in self._components:
            if isinstance(component, component_type):
                return component
            
    def has_component(self, component_type: Type[Component]) -> bool:
        """ Check if the entity has a component.

        Args:
            component_type (Type[Component]): The type of the component to check

        Returns:
            bool: True if the entity has the component, False otherwise
        """
        for component in self._components:
            if isinstance(component, component_type):
                return True
        return False
    
    
    
    