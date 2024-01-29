from typing import Dict, List
from components import TransformComponent, ActionPointComponent
from tiles import GroundTile, LeverTile, WaterTile, PortalTile, TrapTile, ExitTile
from entities import Monster


def distance_calcul(point1: List[int], point2: List[int]) -> float:
    """ Calculate the distance between two points.

    Args:
        point1 (List[int]): first point
        point2 (List[int]): second point

    Returns:
        float: distance between the two points (euclidean distance)
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


def getAllActions(player, gameboard) -> Dict[str, List[int]]:
    """ Get all the actions that the player can do.
    
    Args:
        player (Player): The player who is playing

    Returns:
        dict: A dictionary containing possible movements, attacks, items, and levers.
    """
    possible_movements, possible_attacks, possible_items, possible_levers = [], [], [], []
    current_action_point = player.get_component(ActionPointComponent).current_action_points
    grid = gameboard.grid
    
    max_depth = current_action_point

    current_position = player.get_component(TransformComponent).position
    nb_row, nb_col = gameboard.nb_row, gameboard.nb_col

    # index directions list
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # check possible direction recursively
    def explore_moves(x, y, depth_left):
        if depth_left == 0:
            return

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Check if the position is valid (inside the gameboard)
            if 0 <= new_x < nb_row and 0 <= new_y < nb_col:
                tile = grid[new_x][new_y]
                
                print(tile)
                
                # Check for possible movement
                if (not tile.is_player_on):
                    if isinstance(tile, GroundTile) or isinstance(tile, WaterTile) or isinstance(tile, PortalTile) or isinstance(tile, TrapTile) or isinstance(tile, ExitTile) and ([new_x, new_y] not in possible_movements):
                        possible_movements.append([new_x, new_y])
                        explore_moves(new_x, new_y, depth_left - 1)

                    # Check for possible attacks
                    if isinstance(tile.entity, Monster) and ([new_x, new_y] not in possible_attacks):
                        possible_attacks.append([new_x, new_y])

                    
                    # Check for levers and items
                    if isinstance(tile, LeverTile) and ([new_x, new_y] not in possible_levers):
                        possible_levers.append([new_x, new_y])

    explore_moves(*current_position, max_depth)

    return {
        "PossibleMovement": possible_movements,
        "PossibleAttack": possible_attacks,
        "PossibleItem": possible_items,
        "PossibleLever": possible_levers
    }