from __future__ import annotations
import pygame
from constant import CASE_SIZE, BOARD_X
from abc import ABC, abstractmethod
from math import sqrt

class Entity(ABC, pygame.sprite.Sprite):
    """
    The entity abstract method that represent any entity of the game
    """
    
    def __init__(self: Entity, image: str,  location: list[int, int]= [0,0], max_health: int = 100, damage: int = 20, action_point: int = 3):
        """
        Initialization of the entity
        Args:
            image (str): The image path of the entity
            location (list[int, int]): his location on the gameboard
            max_health (int): The maximum amount of health
            damage (int): The maximum amount of damage the entity deal
            action_point (int): The action point of the entity
        """
        super().__init__()
        self._max_health = max_health
        self._location = location
        self._current_health = max_health
        self._damage = damage
        self._action_point = action_point
        self._current_action_point = action_point
        self._image_path = image
        self._image = pygame.image.load(image)
        self._image = pygame.transform.scale(self._image, (CASE_SIZE, CASE_SIZE))
        self.rect = self._image.get_rect()
        self.rect.x = BOARD_X
        
    
    @property
    def max_health(self: Entity):
        return self._max_health
    @max_health.setter
    def max_health(self: Entity, max_health: int):
        self._max_health = max_health
        
    
    @property
    def location(self: Entity):
        return self._location
    @location.setter
    def location(self: Entity, location: list[int, int]):
        self._location = location
    
    
    @property
    def damage(self: Entity):
        return self._damage
    @damage.setter
    def damage(self: Entity, damage: int):
        self._damage = damage
    
    
    @property
    def action_point(self: Entity):
        return self._action_point
    @action_point.setter
    def action_point(self: Entity, action_point: int):
        self._action_point = action_point
        
    @property
    def current_action_point(self: Entity):
        return self._current_action_point
    @current_action_point.setter
    def current_action_point(self: Entity, action_point: int):
        self._current_action_point = action_point
    
    @property
    def current_health(self: Entity):
        return self._current_health
    @current_health.setter
    def current_health(self: Entity, health: int):
        self._current_health = health
            
    
    @property
    def image(self: Entity):
        return self._image
    @image.setter
    def image(self: Entity, image: str):
        self._image = image
        
    @property
    def image_path(self: Entity):
        return self._image_path
    @image_path.setter
    def image_path(self: Entity, image_path: str):
        self._image_path = image_path
            

    
    @abstractmethod
    def move(self: Entity, target: list[int, int], group: pygame.sprite.Group) -> pygame.sprite.Group:
        """ Move the player into the target position

        Args:
            self (Entity): The player
            target (list[int, int]): The target position
            group (pygame.sprite.Group): The sprite Group (Allow player to be draw in the graphic interface)

        Returns:
            pygame.sprite.Group: the sprite group modified
        """
        for sprite in group:
            if sprite == self:
                sprite.kill()
        distance = Entity.calculateDistance(self.location, target)
        if distance > 2:
            distance = 5
        self._current_action_point -= int(distance)
        if self._current_action_point < 0:
            self._current_action_point = 0
        self._location = target
        self.rect.x = target[1] * CASE_SIZE + BOARD_X
        self.rect.y = target[0] * CASE_SIZE
        group.add(self)
        return group
    
    @abstractmethod
    def attack(self: Entity, target: Entity, grid: list, turn_list: list[Entity], group: pygame.sprite.Group) -> pygame.sprite.Group:
        """
        The attack function of the entity, which allow them to attack a player
        Args:
            target (Entity): The entity that the bat attack
            grid (list[object]): The console representation of the gameboard
            turn_list (list[Entity]): The list of all the entities still alive on the gameboard
            group (pygame.sprite.Group): The group sprite of the entity 
        """
        target.current_health -= self.damage
        self.current_action_point -= 1
        return group, turn_list


    @staticmethod
    def calculateDistance(first_pos: list[int, int], second_pos: list[int, int]) -> float:
        """calculate the distance between 2 positions

        Args:
            first_pos (list[int, int]): position one
            second_pos (list[int, int]): position two

        Returns:
            float: the distance between the two position
        """
        fp_x, fp_y = first_pos[0], first_pos[1]
        sp_x, sp_y = second_pos[0], second_pos[1]
        return sqrt(((fp_x - sp_x) * (fp_x - sp_x)) + ((fp_y - sp_y) * (fp_y - sp_y)))