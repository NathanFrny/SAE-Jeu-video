from .Component import Component

class HealthComponent(Component):
    """ The HealthComponent class is a component that contains the health of the entity
        and the functions to take damage, heal and check if the entity is dead
    """
    
    def __init__(self, max_health: int):
        """ Constructor of the HealthComponent class.

        Args:
            max_health (int): The maximum amount of health that can be reached
        """
        super().__init__() # call the constructor of the parent class
        
        # private attributes
        self.__max_health = max_health
        
        # protected attributes
        self._current_health = max_health
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #    
    
    # Max health attributes
    @property
    def max_health(self):
        return self.__max_health
    @max_health.setter
    def max_health(self, max_health: int):
        self.__max_health = max_health
        
    # Current health attributes
    @property
    def current_health(self):
        return self._current_health
    @current_health.setter
    def current_health(self, health: int):
        self._current_health = health
        # Check if the current health is not above the max health or below 0
        if self._current_health > self.__max_health:
            self._current_health = self.__max_health
        elif self._current_health < 0:
            self._current_health = 0
        
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    def is_dead(self) -> bool:
        """ Check if the entity is dead.
        
            Returns:
                bool: True if the entity is dead, False otherwise
        """
        return self._current_health <= 0
    
    def take_damage(self, damage: int):
        """ Take damage from an entity.

            Args:
                damage (int): The amount of damage to take
        """
        self._current_health -= damage
        if self._current_health < 0:
            self._current_health = 0
        
    def heal(self, heal: int):
        """ Heal the entity.

            Args:
                heal (int): The amount of health to heal
        """
        self._current_health += heal
        if self._current_health > self.__max_health:
            self._current_health = self.__max_health
        
    def reset_health(self):
        """ Reset the health of the entity to the maximum health.
        """
        self._current_health = self.__max_health
        
    def __str__(self):
        """ String representation of the HealthComponent class.
        """
        return f"HealthComponent(max_health={self.__max_health}, current_health={self._current_health})"

