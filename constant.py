import pygame

# Initialisation de Pygame
pygame.init()

# Color constants
TRANSPARENT = (0, 0, 0, 200)

# Font constants
PIXELIFY = "polices/PixelifySans.ttf"

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

# Cases constants
DIRT = ["images/dirt.png", "images/dirt2.png", "images/dirt3.png"]
STONE = ["images/stone.png", "images/stone2.png"]
WATER = ["images/water.png", "images/water2.png"]
TRAP = "images/trap.png"
LEVER = "images/lever2.png"
LEVER_ACTIVATED = "images/lever1.png"
PORTAL = "images/portal.png"
EXIT = "images/exit2.png"
EXIT_OPEN = "images/exit1.png"
MARKET = "images/market.png"
BROKEN_WALL = "images/broken_wall.png"

# Items constants
APPLE = "images/apple.png"
RUNE = "images/rune.png"
FEATHER = "images/feather.png"
ITEMS_LIST = ["apple", "feather", "rune"]


# Other constants
COIN = "images/coin.png"
TITLE = "images/title.png"


# Exit Constants
EXIT_LEVERS = 4
TRAPPED = False
MOVABLE = False
USE_ITEM = False