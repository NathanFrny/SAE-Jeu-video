from dataclasses import dataclass, field
from typing import Tuple, List, Dict
from random import choice
from utils.constants import *

@dataclass
class TileData:
    
    @staticmethod
    def random_tile(variants: list[str]) -> str:
        """ returns random tile from list of variants

        Args:
            variants (list[str]): list of variants

        Returns:
            str: random variant
        """
        return choice(variants)  

@dataclass
class GroundTileData(TileData):
    variants: Dict[str, List[str]] = field(default_factory=lambda:{
        "full": FULL_GROUND,
        "corner_top_left": TOP_LEFT_GROUND,
        "corner_top_right": TOP_RIGHT_GROUND,
        "corner_bottom_left": BOTTOM_LEFT_GROUND,
        "corner_bottom_right": BOTTOM_RIGHT_GROUND,
        "left": LEFT_GROUND,
        "right": RIGHT_GROUND,
        "top": TOP_GROUND,
        "bottom": BOTTOM_GROUND,
        "left_right": LEFT_RIGHT_GROUND,
        "top_bottom": TOP_BOTTOM_GROUND
    })
    
    positions: Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]] = field(default_factory=lambda:{
        "full": ((5, 0, 5),
                          (0, 9, 0),
                          (5, 0, 5)),
        "corner_top_left": ((5, 1, 5),
                                     (1, 9, 0),
                                     (5, 0, 5)),
        "corner_top_right": ((5, 1, 5),
                                      (0, 9, 1),
                                      (5, 0, 5)),
        "corner_bottom_right": ((5, 0, 5),
                                         (0, 9, 1),
                                         (5, 1, 5)),
        "corner_bottom_left": ((5, 0, 5),
                                        (1, 9, 0),
                                        (5, 1, 5)),
        "left": ((5, 0, 5),
                          (1, 9, 0),
                          (5, 0, 5)),
        "right": ((5, 0, 5),
                           (0, 9, 1),
                           (5, 0, 5)),
        "top": ((5, 1, 5),
                         (0, 9, 0),
                         (5, 0, 5)),
        "bottom": ((5, 0, 5),
                            (0, 9, 0),
                            (5, 1, 5)),
        "left_right": ((5, 0, 5),
                                (1, 9, 1),
                                (5, 0, 5)),
        "top_bottom": ((5, 1, 5),
                                (0, 9, 0),
                                (5, 1, 5))
    })

@dataclass
class WallTileData(TileData):
    variants: Dict[str, List[str]] = field(default_factory=lambda:{"full": WALL,
                                 "broken": BROKEN_WALL})                                                     
    
@dataclass 
class WaterTileData(TileData):
    slowness: int = WATER_SLOWNESS
    
    variants: Dict[str, List[str]] = field(default_factory=lambda:{
        "full": FULL_WATER,
        "corner_top_left": [""],
        "corner_top_right": [""],
        "corner_bottom_left": [""],
        "corner_bottom_right": [""],
        "left": [""],
        "right": [""],
        "top": [""],
        "bottom": [""],
        "left_right": [""],
        "top_bottom": [""]
    })
    
    positions: Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]] = field(default_factory=lambda:{
        "full": ((5, 0, 5),
                          (0, 9, 0),
                          (5, 0, 5)),
        "corner_top_left": ((5, 1, 5),
                                     (1, 9, 0),
                                     (5, 0, 5)),
        "corner_top_right": ((5, 1, 5),
                                      (0, 9, 1),
                                      (5, 0, 5)),
        "corner_bottom_right": ((5, 0, 5),
                                         (0, 9, 1),
                                         (5, 1, 5)),
        "corner_bottom_left": ((5, 0, 5),
                                        (1, 9, 0),
                                        (5, 1, 5)),
        "left": ((5, 0, 5),
                          (1, 9, 0),
                          (5, 0, 5)),
        "right": ((5, 0, 5),
                           (0, 9, 1),
                           (5, 0, 5)),
        "top": ((5, 1, 5),
                         (0, 9, 0),
                         (5, 0, 5)),
        "bottom": ((5, 0, 5),
                            (0, 9, 0),
                            (5, 1, 5)),
        "left_right": ((5, 0, 5),
                                (1, 9, 1),
                                (5, 0, 5)),
        "top_bottom": ((5, 1, 5),
                                (0, 9, 0),
                                (5, 1, 5))
    })
  
@dataclass  
class TrapTileData(TileData):
    variants: Dict[str, List[str]] = field(default_factory=lambda:{"full": TRAP})
    strength: int = TRAP_STRENGTH

@dataclass
class PortalTileData(TileData):
    variants: Dict[str, List[str]] = field(default_factory=lambda:{"full": PORTAL})
   
@dataclass 
class MarketTileData(TileData):
    variants: Dict[str, List[str]] = field(default_factory=lambda:{"full": MARKET})
    spawn_probability: float = MARKET_SPAWN_PROBABILITY
    
@dataclass
class ExitTileData(TileData):
    variants: Dict[str, List[str]] = field(default_factory=lambda:{"close": EXIT_CLOSE,
                                 "open": EXIT_OPEN})
    number_players_out: int = 0
 
@dataclass   
class LeverTileData(TileData):
    variants: Dict[str, List[str]] = field(default_factory=lambda:{"close": LEVER_DISACTIVATED,
                                 "open": LEVER_ACTIVATED})
    number_activated: bool = 0
    