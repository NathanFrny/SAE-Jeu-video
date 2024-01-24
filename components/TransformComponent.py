from .Component import Component

class TransformComponent(Component):
    """ The TransformComponent class is a component that contains the position of the entity on the grid
        and the functions to move the entity and get the distance between the entity and a target position
    """
    def __init__(self, position: list[int, int]):
        """ Constructor of the TransformComponent class.

        Args:
            position (list[int, int]): The position of the entity on the grid
        """
        super().__init__() # call the constructor of the parent class
        
        # private attributes
        self.__location = position
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, position: list[int, int]):
        self.__location = position
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    def move(self, target: list[int, int]):
        """ Move the entity into the target position

        Args:
            target (list[int, int]): The target position on the grid
        """
        self.__location = target
        
    def get_distance(self, target: list[int, int]) -> int:
        """ Get the distance between the entity and the target position in the grid

        Args:
            target (list[int, int]): The target position on the grid

        Returns:
            int: The distance between the entity and the target position
        """
        return abs(self.__location[0] - target[0]) + abs(self.__location[1] - target[1])
    
    def __str__(self):
        return f"TransformComponent: {self.__location}"

