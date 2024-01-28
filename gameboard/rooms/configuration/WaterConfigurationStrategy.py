from .TileConfigurationStrategy import TileConfigurationStrategy
from tiles.data.DataTiles import WaterTileData
from tiles import Tile, WaterTile
from gameboard import Gameboard

class WaterConfigurationStrategy(TileConfigurationStrategy):
    def __init__(self, room: Gameboard):
        self._room = room
    
    def get_configuration_key(self, row: int, col: int) -> str:
        """ Determine the configuration key for a water tile based on its neighboring tiles. """
        configuration_matrix = self.get_configuration_matrix(row, col)

        # Compare the matrix with the configurations defined in WaterTileData.positions
        water_tile_data = WaterTileData()
        for key, position_matrix in water_tile_data.positions.items():
            if self.compare_matrices(configuration_matrix, position_matrix):
                return key

        return "full"  # Default to "full" if no specific configuration matches
    
    def compare_matrices(self, matrix_a: list, matrix_b: tuple) -> bool:
        """ Compare a 3x3 matrix with a given configuration matrix, considering '5' as a wildcard. """
        for i in range(3):
            for j in range(3):
                if matrix_b[i][j] != 5 and matrix_a[i][j] != matrix_b[i][j]:
                    return False
        return True

    def get_configuration_matrix(self, row: int, col: int) -> list:
        """ Build a 3x3 matrix representing the configuration of tiles around a water tile. """
        matrix = []
        for dy in range(-1, 2):
            row_matrix = []
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    row_matrix.append(9)  # The current water tile
                else:
                    adjacent_tile = self._room.get_tile(row + dy, col + dx)
                    # Define how you treat different types of tiles here
                    if isinstance(adjacent_tile, Tile) and not isinstance(adjacent_tile, WaterTile):
                        row_matrix.append(1)
                    elif isinstance(adjacent_tile, WaterTile):
                        row_matrix.append(0)
                    else:
                        row_matrix.append(5)  # '5' for tiles that are not considered
            matrix.append(row_matrix)
        return matrix