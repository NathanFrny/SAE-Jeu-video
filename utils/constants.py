import pygame

# Initialisation de Pygame
pygame.init()

# Color constants
TRANSPARENT = (0, 0, 0, 200)

# Font constants
PIXELIFY = "font/PixelifySans.ttf"

# Screen constants
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h

# Grid constants
CASE_SIZE = SCREEN_WIDTH // 28
BOARD_X = (SCREEN_WIDTH - 16 * CASE_SIZE) / 2

# Gameboard constants
NB_ROW = 12
NB_COL = 16

# Player Stats constants
PLAYER_STATS_X = (SCREEN_WIDTH - 28 * CASE_SIZE) / 2
ICON_SIZE = SCREEN_WIDTH // 14
GAP = SCREEN_HEIGHT / 8
PLAYER_HEALTH = 100
PLAYER_ACTION_POINT = 3
PLAYER_DAMAGES = 20
PLAYER_EXIT_ACTION = False
PLAYER_MAX_COINS = 99

# Player Inventory constants
INVENTORY_X = SCREEN_WIDTH - PLAYER_STATS_X - ICON_SIZE * 2 - 100 

# Monsters constants
SLIME = 2
SKELETON = 4
BAT = 2
GOLEM = 6

# Golem constants
GOLEM_IMAGE = "images/golem.png"
GOLEM_HEALTH = 120
GOLEM_ACTION_POINT = 1
GOLEM_DAMAGES = 25
GOLEM_COST = 40

# Slime constants
SLIME_IMAGE = "images/slime.png"
SLIME_HEALTH = 50
SLIME_ACTION_POINT = 2
SLIME_DAMAGES = 10
SLIME_COST = 10

# Skeleton constants
SKELETON_IMAGE = "images/skeleton.png"
SKELETON_HEALTH = 80
SKELETON_ACTION_POINT = 2
SKELETON_DAMAGES = 20
SKELETON_COST = 25

# Bat constants
BAT_IMAGE = "images/bat.png"
BAT_HEALTH = 50
BAT_ACTION_POINT = 3
BAT_DAMAGES = 15
BAT_COST = 15

# Items constants
APPLE = "images/apple.png"
RUNE = "images/rune.png"
FEATHER = "images/feather.png"
ITEMS_LIST = ["apple", "feather", "rune"]


# Other constants
COIN = "images/coin.png"
TITLE = "images/title.png"


# Exit Constants
LEVER_COUNT = 4
EXIT_LEVERS = 4
TRAPPED = False
MOVABLE = False
USE_ITEM = False

# Tiles digit constants
TRAP_STRENGTH = 10
WATER_SLOWNESS = 2
MARKET_SPAWN_PROBABILITY = 0.5

# Tiles images_path constants
# Dirts Ground ---- Basic Biome ---
FULL_GROUND = ["images/basicRoom/dirt/dirt1_full.png", "images/basicRoom/dirt/dirt2_full.png", "images/basicRoom/dirt/dirt3_full.png"]
TOP_LEFT_GROUND = ["images/basicRoom/dirt/dirt1_top_left.png", "images/basicRoom/dirt/dirt2_top_left.png", "images/basicRoom/dirt/dirt3_top_left.png"]
TOP_RIGHT_GROUND = ["images/basicRoom/dirt/dirt1_top_right.png", "images/basicRoom/dirt/dirt2_top_right.png", "images/basicRoom/dirt/dirt3_top_right.png"]
BOTTOM_LEFT_GROUND = ["images/basicRoom/dirt/dirt1_bottom_left.png", "images/basicRoom/dirt/dirt2_bottom_left.png", "images/basicRoom/dirt/dirt3_bottom_left.png"]
BOTTOM_RIGHT_GROUND = ["images/basicRoom/dirt/dirt1_bottom_right.png", "images/basicRoom/dirt/dirt2_bottom_right.png", "images/basicRoom/dirt/dirt3_bottom_right.png"]
LEFT_GROUND = ["images/basicRoom/dirt/dirt1_left.png", "images/basicRoom/dirt/dirt2_left.png", "images/basicRoom/dirt/dirt3_left.png"]
RIGHT_GROUND = ["images/basicRoom/dirt/dirt1_right.png", "images/basicRoom/dirt/dirt2_right.png", "images/basicRoom/dirt/dirt3_right.png"]
TOP_GROUND = ["images/basicRoom/dirt/dirt1_top.png", "images/basicRoom/dirt/dirt2_top.png", "images/basicRoom/dirt/dirt3_top.png"]
BOTTOM_GROUND = ["images/basicRoom/dirt/dirt1_bottom.png", "images/basicRoom/dirt/dirt2_bottom.png", "images/basicRoom/dirt/dirt3_bottom.png"]
TOP_BOTTOM_GROUND = ["images/basicRoom/dirt/dirt1_top_bottom.png", "images/basicRoom/dirt/dirt2_top_bottom.png", "images/basicRoom/dirt/dirt3_top_bottom.png"]
LEFT_RIGHT_GROUND = ["images/basicRoom/dirt/dirt1_left_right.png", "images/basicRoom/dirt/dirt2_left_right.png", "images/basicRoom/dirt/dirt3_left_right.png"]
# ----------------------------------
# Water Tiles ---- Basic Biome ---
FULL_WATER = ["images/basicRoom/water/water1_full.png", "images/basicRoom/water/water2_full.png"]
TOP_LEFT_WATER = ["images/basicRoom/water/water1_top_left.png", "images/basicRoom/water/water2_top_left.png"]
TOP_RIGHT_WATER = ["images/basicRoom/water/water1_top_right.png", "images/basicRoom/water/water2_top_right.png"]
BOTTOM_LEFT_WATER = ["images/basicRoom/water/water1_bottom_left.png", "images/basicRoom/water/water2_bottom_left.png"]
BOTTOM_RIGHT_WATER = ["images/basicRoom/water/water1_bottom_right.png", "images/basicRoom/water/water2_bottom_right.png"]
LEFT_WATER = ["images/basicRoom/water/water1_left.png", "images/basicRoom/water/water2_left.png"]
RIGHT_WATER = ["images/basicRoom/water/water1_right.png", "images/basicRoom/water/water2_right.png"]
TOP_WATER = ["images/basicRoom/water/water1_top.png", "images/basicRoom/water/water2_top.png"]
BOTTOM_WATER = ["images/basicRoom/water/water1_bottom.png", "images/basicRoom/water/water2_bottom.png"]
TOP_BOTTOM_WATER = ["images/basicRoom/water/water1_top_bottom.png", "images/basicRoom/water/water2_top_bottom.png"]
LEFT_RIGHT_WATER = ["images/basicRoom/water/water1_left_right.png", "images/basicRoom/water/water2_left_right.png"]
LEFT_TOP_RIGHT_WATER = ["images/basicRoom/water/water1_left_top_right.png", "images/basicRoom/water/water2_left_top_right.png"]
LEFT_RIGHT_BOTTOM_WATER = ["images/basicRoom/water/water1_left_right_bottom.png", "images/basicRoom/water/water2_left_right_bottom.png"]
TOP_RIGHT_BOTTOM_WATER = ["images/basicRoom/water/water1_top_right_bottom.png", "images/basicRoom/water/water2_top_right_bottom.png"]
LEFT_TOP_BOTTOM_WATER = ["images/basicRoom/water/water1_left_top_bottom.png", "images/basicRoom/water/water2_left_top_bottom.png"]
LEFT_TOP_RIGHT_BOTTOM_WATER = ["images/basicRoom/water/water1_left_top_right_bottom.png", "images/basicRoom/water/water2_left_top_right_bottom.png"]


WALL = ["images/stone1.png", "images/stone2.png"]
BROKEN_WALL = ["images/broken_wall.png"]
TRAP = ["images/trap.png"]
PORTAL = ["images/portal.png"]
EXIT_CLOSE = ["images/exit2.png"]
EXIT_OPEN = ["images/exit1.png"]
MARKET = ["images/market.png"]
LEVER_DISACTIVATED = ["images/lever1.png"]
LEVER_ACTIVATED = ["images/lever2.png"]




