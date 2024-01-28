from abc import ABC, abstractmethod

class Component(ABC):
    """ Abstract class for all components.

    Args:
        ABC : Abstract class
    """
    
    def __init__(self, parent_entity):
        self._parent_entity = parent_entity

    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def parent_entity(self):
        return self._parent_entity
    @parent_entity.setter
    def parent_entity(self, parent_entity):
        self._parent_entity = parent_entity
    
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #

    @abstractmethod
    def update(self):
        pass