from abc import ABC, abstractmethod
from gameboard import Gameboard

class TileConfigurationStrategy(ABC):

    @abstractmethod
    def get_configuration_key(self, room: Gameboard, row: int, col: int) -> str:
        pass

    @abstractmethod
    def get_configuration_matrix(self, room: Gameboard, row: int, col: int) -> list:
        pass
