from .Component import Component

class StrengthComponent(Component):
    
    def __init__(self, initial_strength: int):
        """ Constructor of the StrengthComponent class.

        Args:
            strength (int): The strength of the entity
        """
        super().__init__() # call the constructor of the parent class
        
        # private attributes
        self.__initial_strength = initial_strength
        self.__strength = initial_strength
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def initial_strength(self):
        return self.__initial_strength
    @initial_strength.setter
    def initial_strength(self, initial_strength):
        self.__initial_strength = initial_strength
    
    @property
    def strength(self):
        return self.__strength
    @strength.setter
    def strength(self, strength):
        self.__strength = strength
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    def reset_strength(self):
        """ Reset the strength of the entity.
        """
        self.__strength = self.__initial_strength
        
    def increase_strength(self, amount: int):
        """ Increase the strength of the entity.

        Args:
            amount (int): The strength to add to the entity
        """
        self.__strength += amount
        
    def decrease_strength(self, amount: int):
        """ Decrease the strength of the entity.

        Args:
            amount (int): The strength to remove to the entity
        """
        self.__strength -= amount
        
    def __str__(self):
        """ Return the string representation of the strength of the entity.
        """
        return f"Strength: {self.__strength}"
        
    