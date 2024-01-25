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