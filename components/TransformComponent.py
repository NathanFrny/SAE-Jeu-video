from .Component import Component

class TransformComponent(Component):
    """ The TransformComponent class is a component that contains the position of the entity on the grid
        and the functions to move the entity and get the distance between the entity and a target position
        
        Args:
            Component (Component): The parent class representing a component
    """
    def __init__(self, position: list[int, int], parent_entity):
        """ Constructor of the TransformComponent class.

        Args:
            position (list[int, int]): The position of the entity on the grid
        """
        super().__init__(parent_entity)
        
        # private attributes
        self.__position = position
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: list[int, int]):
        self.__position = position
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    def update(self):
        pass

    def move(self, target: list[int, int]):
        """ Move the entity into the target position

        Args:
            target (list[int, int]): The target position on the grid
        """
        self.__position = target
        
    def get_distance(self, target: list[int, int]) -> int:
        """ Get the distance between the entity and the target position in the grid

        Args:
            target (list[int, int]): The target position on the grid

        Returns:
            int: The distance between the entity and the target position
        """
        return abs(self.__position[0] - target[0]) + abs(self.__position[1] - target[1])
    
    def __str__(self):
        return f"TransformComponent: {self.__position}"

