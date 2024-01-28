from abc import ABC, abstractmethod

class RoomGenerationStrategy(ABC):
    
    @abstractmethod
    def initialize_room(self):
        pass
    
    @abstractmethod
    def set_walls(self):
        pass
    
    @abstractmethod
    def set_ground(self):
        pass
    
    @abstractmethod
    def set_levers(self):
        pass
    
    @abstractmethod
    def set_exit(self):
        pass
    
    @abstractmethod
    def set_traps(self):
        pass

    @abstractmethod
    def set_water(self):
        pass