from __future__ import annotations
import pygame
from entities import Entity

class HealthBar:
    """
    Class that represent a player healthbar drawn on the graphic interface
    """
    
    def __init__ (self: HealthBar, x: int, y: int, width: int, height: int, entity: Entity):
        """
        Initialization of the healthbar
        Args:
            x (int): The x position of the healthbar
            y (int): The y position of the healthbar
            width (int): The width of the healthbar
            height (int): The height of the healthbar
            entity (Entity): The entity who is connected to the healthbar
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._entity = entity
    
    
    # Getter and Setter
    
    @property
    def x(self: HealthBar) -> int:
        return self._x
    @x.setter
    def x(self: HealthBar, x: int):
        self._x = x
    
    @property
    def y(self: HealthBar) -> int:
        return self._y
    @y.setter
    def y(self: HealthBar, y: int):
        self._y = y
        
    @property
    def width(self: HealthBar) -> int:
        return self.width
    @width.setter
    def width(self:HealthBar, width: int):
        self._width = width
    
    @property
    def height(self: HealthBar) -> int:
        return self._height
    @height.setter
    def height(self: HealthBar, height: int):
        self._height = height
        
    @property
    def entity(self: HealthBar) -> Entity:
        return self._entity
    @entity.setter
    def entity(self: HealthBar, entity: Entity):
        self._entity = entity
        
    
    ########## Methods ##########################################
    
    def draw(self: HealthBar, screen: pygame.Surface):
        """ Draw an healthbar into the graphic interface

        Args:
            self (HealthBar): The Healtbar
            screen (pygame.Surface): The graphic interface
        """
        ratio = self._entity.current_health / self._entity.max_health
        pygame.draw.rect(screen, "red", (self._x, self._y, self._width, self._height))
        pygame.draw.rect(screen, "green", (self._x, self._y, self._width * ratio, self._height))