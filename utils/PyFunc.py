from typing import List


def distance_calcul(point1: List[int], point2: List[int]) -> float:
    """ Calculate the distance between two points.

    Args:
        point1 (List[int]): first point
        point2 (List[int]): second point

    Returns:
        float: distance between the two points (euclidean distance)
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5