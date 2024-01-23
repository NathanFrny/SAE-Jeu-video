from __future__ import annotations
import pygame
from random import randint, choice
from math import sqrt
from graphics import MovementSprite, ItemSprite
from items import Apple, Feather, Rune, Item
from cases import Case, Wall, Trap, Water, Lever, Exit, Portal, Market
from entities import Player, Slime, Golem, Bat, Skeleton, Entity
from constant import CASE_SIZE, BOARD_X, SLIME, SLIME_IMAGE, BAT, BAT_IMAGE, SKELETON, SKELETON_IMAGE, GOLEM, GOLEM_IMAGE, NB_ROW, NB_COL, DIRT, STONE, WATER, TRAP, APPLE, RUNE, FEATHER, LEVER, PORTAL, EXIT, MARKET


class Gameboard():
    """
    The gameboard of the game (The most important feature of the game). It's here that we can play the main game.
    """
    
    def __init__(self):
        """
        Initalization of the gameboard
        """
        
        self._nb_row, self._nb_col = NB_ROW, NB_COL
        
        # Créer une grille vide
        self._grid = [[None for _ in range(self._nb_col)] for _ in range(self._nb_row)]
        self._graphicGrid = [[None for _ in range(self._nb_col)] for _ in range(self._nb_row)]
        
        
        # Remplir la grille avec des Cases et y insérer l'image de base
        for row in range(self._nb_row):
            for col in range(self._nb_col):
                case = Case([row, col], Gameboard.randomCase(DIRT))
                self._grid[row][col] = case
        
        for row in range(self._nb_row ):
            for col in range(self._nb_col):
                # On récupère la case du Gameboard
                case = self._grid[row][col]
                image_source = pygame.image.load(case.tile)
                # Redimensionner l'image source pour qu'elle corresponde à la taille de la case
                image_source = pygame.transform.scale(image_source, (CASE_SIZE, CASE_SIZE))
                self._graphicGrid[row][col] = image_source
    
    # Getter and Setter       
         
    @property
    def nb_row(self) -> int:
        return self._nb_row
    @nb_row.setter
    def nb_row(self, row: int):
        self._nb_row = row
    
    @property
    def nb_col(self) -> int:
        return self._nb_col
    @nb_col.setter
    def nb_col(self, col: int):
        self._nb_col = col
    
    @property
    def grid(self) -> list:
        return self._grid
    @grid.setter
    def grid(self, nb_col: int, nb_row: int):
        [[None for _ in range(nb_col)] for _ in range(nb_row)]
    
    @property
    def graphicGrid(self) -> list:
        return self._grid
    @graphicGrid.setter
    def graphicGrid(self, nb_col: int, nb_row: int):
        [[None for _ in range(nb_col)] for _ in range(nb_row)]
    
    
        
    #################### Methods #########################################################################""
          
                            
    def drawRoom(self: Gameboard, screen: pygame.Surface):
        """ Draw the current room on the main interface.

        Args:
            self (Gameboard): The gameboard
            screen (pygame.Surface): The graphic interface
        """
        for row in range(self._nb_row ):
            for col in range(self._nb_col):
                # On récupère la case du Gameboard
                case = self._grid[row][col]
                image_source = pygame.image.load(case.tile)
                # Redimensionner l'image source pour qu'elle corresponde à la taille de la case
                image_source = pygame.transform.scale(image_source, (CASE_SIZE, CASE_SIZE))
                self._graphicGrid[row][col] = image_source
        
        for row in range(self.nb_row):
            for col in range(self.nb_col):
                x = BOARD_X + col * CASE_SIZE
                y = row * CASE_SIZE
                screen.blit(self._graphicGrid[row][col], (x, y))
     
     
    def createRoom(self: Gameboard, walls_number: int, traps: int, waters: int, players: list[Player], enemies: list[Entity], items: list[ItemSprite], item: list[Item]):
        """ Create the current room

        Args:
            self (Gameboard): The Gameboard
            walls_number (int): The initial number of walls (Not counting those that will be deleted.)
        """
        self.setWalls(walls_number)
        self.setLevers()
        self.setExit()
        self.setTraps(traps)
        self.setWaters(waters)
        self.setPortals()
        self.setMarket()
        self.setPlayers(players)
        self.setEnemies(enemies)
        self.setItems(items, item)
              
    
    def setWalls(self: Gameboard, wall_number: int):
        """Set the walls on the room
        
        Args:
            self (Gameboard): The gameboard
            wall_number (int): The initial number of walls (Not counting those that will be deleted.)
        """
        while wall_number >= 0:
            for row in range(self._nb_row):
                for col in range(self._nb_col):
                    random = randint(1,5)
                    if (random == 1):
                        if 0 < row < self._nb_col - 5 and 0 < col < self._nb_row + 3:
                            self.grid[row][col] = Wall([row, col], Gameboard.randomCase(STONE))
                            wall_number -= 1
                            if wall_number <= 0:
                                for row in range(self._nb_row):
                                    for col in range(self._nb_col):
                                        if (not isinstance(self.grid[row][col], Wall)):
                                            self.isDirtCaseAlone(self.grid[row][col])
                                self.deleteWallGroup()
       
               
    def deleteWallGroup(self: Gameboard):
        """ Remove excess Wall tiles. This helps prevent overly large walls or isolated tiles.
        
        Args:
            self (Gameboard): The gameboard
        """
        adjacent_indices = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        for row in range(self._nb_row):
            for col in range(self._nb_col): 
                if (isinstance(self.grid[row][col], Wall)):
                    wallTiles = [self.grid[row][col]]
                    group = 1
                    while wallTiles:
                        for direction in adjacent_indices:
                            new_x = row + direction[0]
                            new_y = col + direction[1]
                            if (isinstance(self.grid[new_x][new_y], Wall)):
                                wallTiles = [self.grid[new_x][new_y]]
                                group += 1
                                if group >= 4:
                                    self.grid[new_x][new_y] = Case([new_x, new_y], Gameboard.randomCase(DIRT))
                        wallTiles.pop()
                                             
                        
    def isDirtCaseAlone(self: Gameboard, tile: Case):
        """Prevent the appearance of isolated tiles during room construction (reliability of 80%, requires the deleteWallGroup method for optimal efficiency).

        Args:
            self (Gameboard): the gameboard
            tile (Case): the tile that is checked
        """
        pos = tile.pos
        adjacent_indices = [[-1,0],[1,0],[0,1],[0,-1]]
        group = 0
        for dx, dy in adjacent_indices:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if 0 <= new_x < self._nb_col and 0 <= new_y < self._nb_row:
                if (isinstance(self._grid[new_y][new_x], Wall) or isinstance(self._grid[new_y][new_x], Lever)):
                    group += 1
        if (group >= 4):
            self.grid[pos[0]][pos[1]] = Case(pos, Gameboard.randomCase(DIRT))
                            
    
    def setLevers(self: Gameboard, lever_number: int = 4):
        """set the four levers on the room.

        Args:
            self (Gameboard): the Gameboard
            lever_number (int, optional): number of levers in the room. Defaults to 4.
        """
        lever_list = []
        while lever_number > 0:
            for row in range(self._nb_row ):
                for col in range(self._nb_col): 
                    if 0 < row < self._nb_col - 5 and 0 < col < self._nb_row + 3:
                        if (isinstance(self.grid[row][col], Case) and (not isinstance(self.grid[row][col], Lever))):
                            random = randint(1,100)
                            if (random == 50):
                                self.grid[row][col] = Lever([row, col], LEVER)
                                lever_list.append([row, col])
                                
                                
                                # The likelihood of two levers being adjacent or close to each other is significantly reduced (not eliminated, as it's part of the game).
                                if (len(lever_list) >= 2):
                                    # Calculate distance between the 2 levers
                                    distance = Gameboard.calculateDistance(lever_list[0], lever_list[1])
                                    # If too close, replaced
                                    if (distance <= 5):
                                        self.grid[row][col] = Case([row, col], Gameboard.randomCase(DIRT))
                                        lever_list.remove(lever_list[1])
                                    else:
                                        lever_list.remove(lever_list[0])
                                        lever_number -= 1
                                        if (lever_number <= 0):
                                            self.isDirtCaseAlone(self.grid[row][col])
                                            return
                                else:  
                                    lever_number -= 1
                                    if (lever_number <= 0):
                                        self.isDirtCaseAlone(self.grid[row][col])
                                        return
    
    
    def setExit(self: Gameboard):
        """set the exit of the room

        Args:
            self (Gameboard): The gameboard
        """
        is_exit = False
        while not is_exit:
            for row in range(self._nb_row - 4): # exit don't spawn below the 8th line.
                for col in range(self._nb_col):
                    case = self.grid[row][col]
                    if (not isinstance(case, Wall) and not isinstance(case, Lever)):
                        random = randint(1,50)
                        if (random == 25):
                            self.grid[row][col] = Exit([row, col], EXIT)
                            return
    
    
    def setTraps(self: Gameboard, trap_number: int):
        """ Set the traps on the gameboard

        Args:
            self (Gameboard): The gameboard
            trap_number (int): The number of traps in the room
        """
        adjacent_indices = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        while trap_number >= 1:
            for row in range(self._nb_row - 3): # exit don't spawn below the 10th line.
                for col in range(self._nb_col):
                    case = self.grid[row][col]
                    if 0 < row < self._nb_col - 5 and 0 < col < self._nb_row + 3:
                        if(not isinstance(case, Wall) and not isinstance(case, Lever) and not isinstance(case, Exit) and not isinstance(case, Trap)):
                            random = randint(1,50)
                            if (random == 25):
                                self.grid[row][col] = Trap([row,col], TRAP)
                                trap_number -= 1
                                if trap_number <= 0:
                                    return
                                for indice in adjacent_indices:
                                    if (not isinstance(self.grid[row + indice[0]][col + indice[1]], Wall) and not isinstance(self.grid[row + indice[0]][col + indice[1]], Lever) and not isinstance(self.grid[row + indice[0]][col + indice[1]], Exit) and not isinstance(self.grid[row + indice[0]][col + indice[1]], Trap)):
                                        self.grid[row + indice[0]][col + indice[1]] = Trap([row + indice[0],col + indice[1]], TRAP)
                                        trap_number -= 1
                                        if trap_number <= 0:
                                            return
    
    
    def setWaters(self: Gameboard, waters_number: int):
        """ Set the waters case on the gameboard

        Args:
            self (Gameboard): The gameboard
            waters_number (int): The number of water case
        """
        adjacent_indices = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        while waters_number >= 1:
            for row in range(self._nb_row - 3): # exit don't spawn below the 10th line.
                for col in range(self._nb_col):
                    case = self.grid[row][col]
                    if 0 < row < self._nb_col - 5 and 0 < col < self._nb_row + 3:
                        if(not isinstance(case, Wall) and not isinstance(case, Lever) and not isinstance(case, Exit) and not isinstance(case, Trap) and not isinstance(case, Water)):
                            random = randint(1,50)
                            if (random == 25):
                                self.grid[row][col] = Water([row,col], Gameboard.randomCase(WATER))
                                waters_number -= 1
                                if waters_number <= 0:
                                    return
                                for indice in adjacent_indices:
                                    if (not isinstance(self.grid[row + indice[0]][col + indice[1]], Wall) and not isinstance(self.grid[row + indice[0]][col + indice[1]], Lever) and not isinstance(self.grid[row + indice[0]][col + indice[1]], Exit) and not isinstance(self.grid[row + indice[0]][col + indice[1]], Trap) and not isinstance(self.grid[row + indice[0]][col + indice[1]], Water)):
                                        self.grid[row + indice[0]][col + indice[1]] = Water([row + indice[0],col + indice[1]], Gameboard.randomCase(WATER))
                                        waters_number -= 1
                                        if waters_number <= 0:
                                            return
                          
                          
    def setPortals(self: Gameboard):
        """ Set the 2 portals on the 

        Args:
            self (Gameboard): _description_
        """
        portals_number = 2
        first_portal_position = []
        first_portal = None
        while portals_number >= 1:
            for row in range(self._nb_row - 3): # exit don't spawn below the 10th line.
                for col in range(self._nb_col):
                    case = self.grid[row][col]
                    if 0 < row < self._nb_col - 5 and 0 < col < self._nb_row + 3:
                        if(not isinstance(case, Wall) and not isinstance(case, Lever) and not isinstance(case, Exit) and not isinstance(case, Trap) and not isinstance(case, Water) and not isinstance(case, Portal)):
                            random = randint(1,50)
                            if (random == 25):
                                if (first_portal_position != []):
                                    distance = Gameboard.calculateDistance(first_portal_position, [row, col])
                                    if (distance >= 7):
                                        # Add the second portal and connect it to the first (connect also the first to the second with the portal __init__)
                                        self.grid[row][col] = Portal([row,col], PORTAL, target= first_portal)
                                        return
                                else:
                                    first_portal = Portal([row,col], PORTAL)
                                    self.grid[row][col] = first_portal
                                    first_portal_position = [row, col]
                                    portals_number -= 1
                                    if portals_number <= 0:
                                        return
        
        
    def setMarket(self: Gameboard):
        for row in range(self._nb_row - 3): # exit don't spawn below the 10th line.
                for col in range(self._nb_col):
                    case = self.grid[row][col]
                    if 0 < row < self._nb_col - 5 and 0 < col < self._nb_row + 3:
                        if(not isinstance(case, Wall) and not isinstance(case, Lever) and not isinstance(case, Exit) and not isinstance(case, Trap) and not isinstance(case, Water) and not isinstance(case, Portal)):
                            random = randint(1,50)
                            if (random == 25):
                                self.grid[row][col] = Market([row,col], MARKET)
                                return
        
        
    def createPlayers(self: Player, number_of_players: int = 4) -> list[Player]:
        """ Create all the players

        Args:
            self (Player): The gameboard
            number_of_players (int): The number of players

        Returns:
            list[Player]: the list of all the players
        """
        players = []
        for i in range(number_of_players):
            path = f"images/player{i+1}.png"
            player = Player(path, f"Player{i+1}")
            players.append(player)
        return players
    
    
    def setPlayers(self: Gameboard, players: list[Player]):
        """ set the players instance start position and locate them on the screen

        Args:
            self (Gameboard): The gameboard
            players (list[Player]): the list of Players instance created
        """
        last_line = self._grid[-1] # Players are located at the bottom line
        player_number = len(players)
        forbidden_case = [] # Prevent players for getting the same start case
        while player_number >= 1:
            for case in last_line:
                random = randint(1,5)
                if (random == 1) and (case.pos not in forbidden_case):
                    # Set the player location (on the grid and on the screen)
                    players[player_number - 1].location = case.pos
                    players[player_number - 1].rect.x = players[player_number - 1].location[1] * CASE_SIZE + BOARD_X
                    players[player_number - 1].rect.y = players[player_number - 1].location[0] * CASE_SIZE
                    # Prevent that the case contain an entity
                    case.entity = players[player_number - 1]
                    forbidden_case.append(case.pos)
                    player_number -= 1
                    if (player_number < 1):
                        return
        
        
    def createEnemies(self: Gameboard, room_level: int) -> list[Entity]:
        """ Create all the enemies instance based on the room level.

        Args:
            self (Gameboard): The gameboard
            room_level (int): The level of the room (The difficulty increases depending on the value)

        Returns:
            list[Entity]: the list of enemies instance created
        """
        enemies_list = []
        all_enemy = ["Slime", "Skeleton", "Bat", "Golem"]
        while (room_level > 0):
            match choice(all_enemy):
                case "Slime":
                    if room_level >= SLIME:
                        slime = Slime(SLIME_IMAGE)
                        enemies_list.append(slime)
                        room_level -= SLIME
                case "Skeleton":
                    if room_level >= SKELETON:
                        skeleton = Skeleton(SKELETON_IMAGE)
                        enemies_list.append(skeleton)
                        room_level -= SKELETON
                case "Bat":
                    if room_level >= BAT:
                        bat = Bat(BAT_IMAGE)
                        enemies_list.append(bat)
                        room_level -= BAT
                case "Golem":
                    if room_level >= GOLEM:
                        golem = Golem(GOLEM_IMAGE)
                        enemies_list.append(golem)
                        room_level -= GOLEM
        return enemies_list
            
    
    def setEnemies(self: Gameboard, enemies: list[Entity]):
        """ set the enemies start position and locate them on the screen

        Args:
            self (Gameboard): The gameboard
            enemies (list[Entity]): the list of enemies
        """
        enemies_number = len(enemies)
        forbidden_case = [] # Prevent enemies for getting the same start case
        while enemies_number >= 1:
            for row in range(self._nb_row - 4): # enemies don't spawn below the 8th line.
                for col in range(self._nb_col):
                    case = self.grid[row][col]
                    if (not isinstance(case, Wall) and not isinstance(case, Lever) and not isinstance(case, Exit) and not isinstance(case, Trap)):
                        random = randint(1,25)
                        if (random == 5) and (case.pos not in forbidden_case):
                            enemies[enemies_number - 1].location = case.pos
                            enemies[enemies_number - 1]. rect.x = enemies[enemies_number - 1].location[1] * CASE_SIZE + BOARD_X
                            enemies[enemies_number - 1]. rect.y = enemies[enemies_number - 1].location[0] * CASE_SIZE
                            # Prevent that the case contain an entity
                            case.entity = enemies[enemies_number - 1]
                            forbidden_case.append(case.pos)
                            enemies_number -= 1
                            if (enemies_number < 1):
                                return
          
                
    def chooseItem(self: Gameboard, item_number: int) -> list[ItemSprite]:
        """ Define which item are in the room

        Args:
            self (Gameboard): The gameboard
            item_number (int): The number of item needed

        Returns:
            list[ItemSprite]: The list of the items in the room
        """
        items = ["Apple", "Feather", "Rune"]
        items_sprite_list = []
        items_list = []
        while item_number > 0:
            match (choice(items)):
                case "Apple":
                    apple = Apple(APPLE)
                    items_list.append(apple)
                    item_sprite = ItemSprite(apple)
                    items_sprite_list.append(item_sprite)
                    item_number -= 1
                case "Feather":
                    feather = Feather(FEATHER)
                    items_list.append(feather)
                    item_sprite = ItemSprite(feather)
                    items_sprite_list.append(item_sprite)
                    item_number -= 1
                case "Rune":
                    rune = Rune(RUNE)
                    items_list.append(rune)
                    item_sprite = ItemSprite(rune)
                    items_sprite_list.append(item_sprite)
                    item_number -= 1
        return items_sprite_list, items_list
    
    
    def setItems(self: Gameboard, items: list[ItemSprite], item: list[Item]):
        """ Set all the item into the gameboard

        Args:
            self (Gameboard): the gameboard
            items (list[ItemSprite]): The list of items
        """
        items_number = len(items)
        forbidden_case = []
        while items_number >= 1:
            for row in range(self._nb_row - 4): # items don't spawn below the 8th line.
                for col in range(self._nb_col):
                    case = self.grid[row][col]
                    if (not isinstance(case, Wall) and not isinstance(case, Lever) and not isinstance(case, Exit) and not isinstance(case, Portal) and not isinstance(case, Market)):
                        random = randint(1,25)
                        if (random == 5) and (case.pos not in forbidden_case):
                            items[items_number -1].location = case.pos
                            item[items_number -1].location = case.pos
                            items[items_number -1].rect.x = int(items[items_number -1].location[1]) * CASE_SIZE + BOARD_X
                            items[items_number -1].rect.y = items[items_number -1].location[0] * CASE_SIZE
                            forbidden_case.append(case.pos)
                            items_number -= 1
                            if (items_number < 1):
                                return
                    
      
    def drawPossibleMovements(self: Gameboard, movements: list[int, int], attacks: list[list[int, int]], levers: list[list[int, int]], items: list[list[int, int]], groups: pygame.sprite.Group) -> pygame.sprite.Group:
        """ draw all possible movements of a player

        Args:
            self (Gameboard): The gameboard
            movements (list[int, int]): All the possible movements
            groups (pygame.sprite.Group): The sprite group (where to add all the movement sprites)

        Returns:
            pygame.sprite.Group: The sprite group modified
        """
        for group in groups:
            groups.remove(group)
        for movement in movements:
            target = MovementSprite("images/movement.png", "images/target.png", movement)
            target.rect.x = movement[1] * CASE_SIZE + BOARD_X
            target.rect.y = movement[0] * CASE_SIZE
            groups.add(target)
        for attack in attacks:
            target = MovementSprite("images/action.png", "images/target.png", attack, "attack")
            target.rect.x = attack[1] * CASE_SIZE + BOARD_X
            target.rect.y = attack[0] * CASE_SIZE
            groups.add(target)
        for lever in levers:
            target = MovementSprite("images/action.png", "images/target.png", lever, "lever")
            target.rect.x = lever[1] * CASE_SIZE + BOARD_X
            target.rect.y = lever[0] * CASE_SIZE
            groups.add(target)
        for item in items:
            target = MovementSprite("images/item.png", "images/target.png", item, "item")
            target.rect.x = item[1] * CASE_SIZE + BOARD_X
            target.rect.y = item[0] * CASE_SIZE
            groups.add(target)
        return groups
        
        
    @staticmethod
    def calculateDistance(first_pos: list[int, int], second_pos: list[int, int]) -> float:
        """calculate the distance between 2 positions

        Args:
            first_pos (list[int, int]): position one
            second_pos (list[int, int]): position two

        Returns:
            float: the distance between the two position
        """
        fp_x, fp_y = first_pos[0], first_pos[1]
        sp_x, sp_y = second_pos[0], second_pos[1]
        return sqrt(((fp_x - sp_x) * (fp_x - sp_x)) + ((fp_y - sp_y) * (fp_y - sp_y)))

    
    @staticmethod
    def randomCase(cases: list[str]) -> str:
        """ Return a random case image

        Args:
            cases (list[str]): the list of cases images path

        Returns:
            str: a random case image
        """
        return choice(cases)
