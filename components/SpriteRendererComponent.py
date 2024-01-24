from pygame import sprite, image, transform
from utils.constants import ICON_SIZE
from .Component import Component


class SpriteRendererComponent(Component):
    """ The SpriteRendererComponent class is a component that contains the sprite of the entity
    
        Args:
            Component (Component): The parent class representing a component
    """
    def __init__(self, image_path: str):
        """ Constructor of the SpriteRendererComponent class.

        Args:
            image_path (str): The path of the image of the entity
        """
        super().__init__() # call the constructor of the parent class
        
        # private attributes
        self.__image = image.load(image_path)
        self.__image = transform.scale(self.__image, (ICON_SIZE, ICON_SIZE)) # resize the image (ICON_SIZE by default)
        self.__rect = self.__image.get_rect()
        
        # protected attributes
        self._sprite = sprite.Sprite()
        self._sprite.image = self.__image
        self._sprite.rect = self.__rect
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    # Image attributes
    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image):
        self.__image = image
        self._sprite.image = image # update the sprite too
        
    # Rect attributes
    @property
    def rect(self):
        return self.__rect
    @rect.setter
    def rect(self, rect):
        self.__rect = rect
        self._sprite.rect = self.__rect # update the sprite too
        
    @property
    def sprite(self):
        return self._sprite
    @sprite.setter
    def sprite(self, sprite):
        self._sprite = sprite
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    def image_resize(self, size: tuple[int, int]):
        """ Resize the image sprite of the entity.

        Args:
            size (tuple[int, int]): The new size of the image
        """
        self.__image = transform.scale(self.__image, size)
        self.__rect = self.__image.get_rect()
        self._sprite.image = self.__image # update the sprite too
        self._sprite.rect = self.__rect
        
    def __str__(self):
        return f"SpriteRendererComponent: {self.__image}, {self.__rect}"
        

        