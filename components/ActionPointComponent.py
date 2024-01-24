from .Component import Component

class ActionPointComponent(Component):
    """ The ActionPointComponent class is a component that contains the action point of the entity
        and the functions to use and give action point to the entity
        
        Args:
            Component (Component): The parent class representing a component
    """
    
    def __init__(self, action_points: int):
        """ Constructor of the ActionComponent class.

        Args:
            action_point (int): The amount of action point that the entity has
        """
        super().__init__() # call the constructor of the parent class
        
        # private attributes
        self.__max_action_points = action_points
        
        # protected attributes
        self._current_action_points = action_points
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
        
    @property
    def max_action_points(self):
        return self.__max_action_points
    @max_action_points.setter
    def action_point(self, action_points: int):
        self.__max_action_points = action_points
            
    @property
    def current_action_points(self):
        return self._current_action_points
    @current_action_points.setter
    def current_action_points(self, action_points: int):
        self._current_action_points = action_points
        if self._current_action_points < 0:
            self._current_action_points = 0
        elif self._current_action_points > self.__max_action_points:
            self._current_action_points = self.__max_action_points
        
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    
    def reset_action_point(self):
        """ Reset the action point of the entity.
        """
        self._current_action_points = self.__max_action_points
    
    def use_action_point(self, amount: int):
        """ Use action point from the entity.

        Args:
            amount (int): The amount of action point to use
        """
        self._current_action_points -= amount
        if self._current_action_points < 0:
            self._current_action_points = 0
        
    def give_action_point(self, amount: int):
        """ Give action point to the entity.

        Args:
            amount (int): The amount of action point to give
        """
        self._current_action_points += amount
        if self._current_action_points > self.__max_action_points:
            self._current_action_points = self.__max_action_points
        
    def is_action_point_empty(self) -> bool:
        """ Check if the entity has no action point left.

        Returns:
            bool: True if the entity has no action point left, False otherwise
        """
        return self._current_action_points <= 0
    
    def is_action_point_full(self) -> bool:
        """ Check if the entity has full action point.

        Returns:
            bool: True if the entity has full action point, False otherwise
        """
        return self._current_action_points >= self.__max_action_points
    
    def __str__(self) -> str:
        return f"ActionPointComponent: {self._current_action_points}/{self.__max_action_points}"
    
    
        