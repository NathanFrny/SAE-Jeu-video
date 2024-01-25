# FILEPATH: /C:/Users/Asus/Documents/GitHub/SAE-Jeu-video/tiles/tests/test_TileFactory.py

import unittest
from ..TileFactory import TileFactory
from .. import GroundTile, WallTile, TrapTile, WaterTile, MarketTile, PortalTile
from ..data.DataTiles import TileData, GroundTileData, WallTileData, TrapTileData, WaterTileData, MarketTileData, PortalTileData

class TestTileFactory(unittest.TestCase):
    def setUp(self):
        self.tile_factory = TileFactory()

    def test_create_ground_tile(self):
        tile = self.tile_factory.create_tile("ground", GroundTileData())
        self.assertIsInstance(tile, GroundTile)

    def test_create_wall_tile(self):
        tile = self.tile_factory.create_tile("wall", WallTileData())
        self.assertIsInstance(tile, WallTile)

    def test_create_trap_tile(self):
        tile = self.tile_factory.create_tile("trap", TrapTileData())
        self.assertIsInstance(tile, TrapTile)

    def test_create_water_tile(self):
        tile = self.tile_factory.create_tile("water", WaterTileData())
        self.assertIsInstance(tile, WaterTile)

    def test_create_market_tile(self):
        tile = self.tile_factory.create_tile("market", MarketTileData())
        self.assertIsInstance(tile, MarketTile)

    def test_create_portal_tile(self):
        tile = self.tile_factory.create_tile("portal", PortalTileData())
        self.assertIsInstance(tile, PortalTile)

    def test_create_unknown_tile(self):
        with self.assertRaises(ValueError):
            self.tile_factory.create_tile("unknown", TileData())

if __name__ == '__main__':
    unittest.main()