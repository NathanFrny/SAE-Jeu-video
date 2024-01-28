from .RoomGenerationStrategy import RoomGenerationStrategy
from .configuration.GroundConfigurationStrategy import GroundConfigurationStrategy
from .configuration.WaterConfigurationStrategy import WaterConfigurationStrategy
from entities import Player
from components import TransformComponent
from gameboard import Gameboard, GraphicGameboard
from tiles.data.DataTiles import *
from typing import Tuple
from utils.PyFunc import distance_calcul
from tiles import GroundTile, WallTile, LeverTile, ExitTile, WaterTile
from random import randint, sample
from tiles import TileFactory

class BasicRoomStrategy(RoomGenerationStrategy):
    
    def __init__(self, room: Gameboard, graphic_room: GraphicGameboard):
        """ Initialize the strategy
        """
        self._room = room
        self._graphic_room = graphic_room
        self._tile_factory = TileFactory()
        self._tile_config_strategies = {
            'ground': GroundConfigurationStrategy(room),
            'water': WaterConfigurationStrategy(room)
        }
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def room(self):
        return self._room
    @room.setter
    def room(self, room):
        self._room = room
        
    @property
    def graphic_room(self):
        return self._graphic_room
    @graphic_room.setter
    def graphic_room(self, graphic_room):
        self._graphic_room = graphic_room
        
    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
    
    # --- Initialization methods --- #
    
    def initialize_room(self):
        """ Initialize the room
        """
        self.ground_initialization()
        self.walls_initialization()
        
    def ground_initialization(self):
        """ Initialize the ground of the room
        """
        for row in range(self._room.nb_row):
            for col in range(self._room.nb_col):
                tile = self.room.get_tile(row, col)
                image_variants = tile.data_tile.variants["full"]
                image = tile.data_tile.random_tile(image_variants)
                self._graphic_room.set_image(row, col, image)
                
    def walls_initialization(self):
        """ Initialize the walls of the room
        """
        for row in range(self._room.nb_row):
            for col in range(self._room.nb_col):
                if row == 0 or row == self._room.nb_row - 1 or col == 0 or col == self._room.nb_col - 1: # if the tile is on the border of the room
                    wall_tile = self._tile_factory.create_tile("wall", WallTileData()) # create a wall tile
                    wall_image_variants = wall_tile.dataTile.variants["full"]
                    image = wall_tile.data_tile.random_tile(wall_image_variants)
                    self._room.set_tile(row, col, wall_tile)
                    self._graphic_room.set_image(row, col, image)
                    
    # --- Walls generation methods --- #
    
    def set_walls(self):
        """ Initialize the walls of the room with correct sprites based on ground positions.
        """
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if randint(1, 4) == 1:  
                    self.set_wall_tile(row, col)
                    if not self.ensure_global_connectivity():
                        self.set_ground_tile(row, col)  


    def ensure_global_connectivity(self) -> bool:
        """ Check if the room is globally connected (i.e. there is no ground tile that is not connected to the rest of the room).

        Returns:
            bool: True if the room is globally connected, False otherwise
        """
        start_row, start_col = self.find_ground_tile()

        visited = self.traverse(start_row, start_col)

        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if not isinstance(self._room.get_tile(row, col), WallTile) and not visited[row][col]:
                    return False 

        return True
    
    def traverse(self, start_row: int, start_col: int):
        """ Traverse the room from a given position and return a matrix of visited tiles.

        Args:
            start_row (int): The row of the starting position
            start_col (int): The column of the starting position

        Returns:
            list[list[bool]]: A matrix of visited tiles
        """
        visited = [[False for _ in range(self._room.nb_col)] for _ in range(self._room.nb_row)]
        stack = [(start_row, start_col)]

        while stack:
            row, col = stack.pop()
            if not visited[row][col]:
                visited[row][col] = True
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row, new_col = row + dx, col + dy
                    if 1 <= new_row < self._room.nb_row-1 and 1 <= new_col < self._room.nb_col-1:
                        if not isinstance(self._room.get_tile(new_row, new_col), WallTile):
                            stack.append((new_row, new_col))

        return visited

    def find_ground_tile(self):
        """ Find a ground tile to start the connectivity check.

        Returns:
            tuple(int, int): The row and column of the ground tile
        """
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                if not isinstance(self._room.get_tile(row, col), WallTile):
                    return row, col
        raise ValueError("Aucune GroundTile trouvée pour démarrer la vérification de la connectivité.")

            
    def set_ground_tile(self, row: int, col: int):
        """ Set a ground tile at the given position.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile
        """
        ground_tile = self._tile_factory.create_tile("ground", GroundTileData())
        self._room.set_tile(row, col, ground_tile)
        ground_image_variant = ground_tile.dataTile.variants["full"]
        image = ground_tile.dataTile.random_tile(ground_image_variant)
        self._graphic_room.set_image(row, col, image)

    def set_wall_tile(self, row: int, col: int):
        """ Set a wall tile at the given position.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile
        """
        wall_tile = self._tile_factory.create_tile("wall", WallTileData())
        self._room.set_tile(row, col, wall_tile)
        wall_image_variants = wall_tile.dataTile.variants["full"]
        image = wall_tile.dataTile.random_tile(wall_image_variants)
        self._graphic_room.set_image(row, col, image)
        
    
    # --- Ground generation methods --- #
    
    def set_ground(self):
        """ Initialize the ground of the room with correct sprites based on wall positions. """
        for row in range(1, self._room.nb_row - 1):
            for col in range(1, self._room.nb_col - 1):
                self.set_ground_sprite(row, col)

    def set_ground_sprite(self, row: int, col: int):
        """ Set the sprite for a ground tile based on its configuration. 
        
            Args:
                row (int): the row of the tile
                col (int): the column of the tile
        """
        tile = self._room.get_tile(row, col)
        if isinstance(tile, GroundTile):
            configuration_strategy = self._tile_config_strategies.get('ground')
            if configuration_strategy:
                configuration_key = configuration_strategy.get_configuration_key(row, col)
                if configuration_key in tile.dataTile.variants:
                    image = tile.dataTile.random_tile(tile.dataTile.variants[configuration_key])
                else:
                    image = tile.dataTile.random_tile(tile.dataTile.variants["full"])
                self._graphic_room.set_image(row, col, image)
                
    # --------------------------------- #
    
    # --- Levers generation methods --- #
    
    def set_levers(self, lever_count: int = 4):
        lever_count = lever_count
        placed_levers = 0
        lever_positions = []

        while placed_levers < lever_count:
            row = randint(1, self._room.nb_row - 2)
            col = randint(1, self._room.nb_col - 2)

            # Vérifier si la position est valide (ni un mur, ni un levier déjà placé)
            if self.is_valid_lever_position(row, col):
                lever_tile = self._tile_factory.create_tile("lever", LeverTileData())
                self._room.set_tile(row, col, lever_tile)
                lever_positions.append([row, col])

                # Définir l'image du levier dans la représentation graphique
                lever_image_variant = lever_tile.dataTile.variants["close"]  # Ou une autre clé si vous avez plusieurs variantes
                image = lever_tile.dataTile.random_tile(lever_image_variant)
                self._graphic_room.set_image(row, col, image)

                placed_levers += 1
        self.check_and_reposition_levers(lever_positions)
                
    def is_valid_lever_position(self, row: int, col: int) -> bool:
        return not self._room.is_tile(row, col, WallTile) and not self._room.is_tile(row, col, LeverTile)
    
    def check_and_reposition_levers(self, lever_positions: List[List[int]], min_distance: float = 5.0):
        for i in range(len(lever_positions)):
            for j in range(i + 1, len(lever_positions)):
                if distance_calcul(lever_positions[i], lever_positions[j]) < min_distance:
                    new_position = self.find_new_position_for_lever(lever_positions, min_distance)
                    self.update_lever_position(lever_positions[j], new_position, lever_positions)  # Passer lever_positions comme argument


    def find_new_position_for_lever(self, lever_positions: List[List[int]], min_distance: float) -> List[int]:
        while True:
            new_row = randint(1, self._room.nb_row - 2)
            new_col = randint(1, self._room.nb_col - 2)
            new_position = [new_row, new_col]

            # Vérifier si la nouvelle position est valide et pas trop proche des autres leviers
            if self.is_valid_lever_position(new_row, new_col) and all(distance_calcul(new_position, pos) >= min_distance for pos in lever_positions):
                return new_position

    def update_lever_position(self, old_position: List[int], new_position: List[int], lever_positions: List[List[int]]):
        # Supprimer l'ancien levier de la grille et de la liste des positions
        self.set_ground_tile(old_position[0], old_position[1])
        lever_positions.remove(old_position)  # Retirer l'ancienne position de la liste

        # Placer le nouveau levier et l'ajouter à la liste des positions
        self.set_lever_tile(new_position[0], new_position[1])
        lever_positions.append(new_position)  # Ajouter la nouvelle position à la liste


    def set_lever_tile(self, row: int, col: int):
        lever_tile = self._tile_factory.create_tile("lever", LeverTileData())
        self._room.set_tile(row, col, lever_tile)
        lever_image_variant = lever_tile.dataTile.variants["close"]
        image = lever_tile.dataTile.random_tile(lever_image_variant)
        self._graphic_room.set_image(row, col, image)

    
    # ------------------------------- #
    
    # --- Exit generation methods --- #
    
    def set_exit(self):
        """ Initialize the exit of the room with correct sprites based on ground positions. """
        exit_row, exit_col = self.find_exit_position()
        self.set_exit_sprite(exit_row, exit_col)
        
    def find_exit_position(self):
        """ Find a ground tile to start the connectivity check.
        """
        while True:
            row = randint(1, self._room.nb_row - 2)
            col = randint(1, self._room.nb_col - 2)
            if self.is_valid_exit_position(row, col):
                return row, col
            
    def is_valid_exit_position(self, row: int, col: int) -> bool:
        return not self._room.is_tile(row, col, WallTile) and not self._room.is_tile(row, col, LeverTile)
    
    def set_exit_sprite(self, row: int, col: int):
        """ Set the sprite for a ground tile based on its configuration. 
        
            Args:
                row (int): the row of the tile
                col (int): the column of the tile
        """
        exit_tile = self._tile_factory.create_tile("exit", ExitTileData())
        self._room.set_tile(row, col, exit_tile)
        exit_image_variant = exit_tile.dataTile.variants["close"]
        image = exit_tile.dataTile.random_tile(exit_image_variant)
        self._graphic_room.set_image(row, col, image)
        
    # ------------------------------ #
    
    # --- Trap generation methods --- #
    
    def set_traps(self):
        """ Initialize the traps of the room with correct sprites based on ground positions.
        """
        num_trap_packs = randint(2, 3)

        for _ in range(num_trap_packs):
            num_traps = randint(5, 6)
            start_row, start_col = self.find_valid_trap_start()

            for _ in range(num_traps):
                if self.is_valid_trap_position(start_row, start_col):
                    self.set_trap_sprite(start_row, start_col)
                else:
                    start_row, start_col = self.find_valid_trap_start()

                direction = self.choose_adjacent_direction(start_row, start_col)
                start_row += direction[0]
                start_col += direction[1]

    def choose_adjacent_direction(self, row: int, col: int) -> Tuple[int, int]:
        """ Choose a direction for a trap to be placed in an adjacent tile.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile

        Returns:
            Tuple[int, int]: the direction to move in
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while True:
            direction = choice(directions)
            new_row, new_col = row + direction[0], col + direction[1]

            if 1 <= new_row < self._room.nb_row - 1 and 1 <= new_col < self._room.nb_col - 1:
                if self.is_valid_trap_position(new_row, new_col):
                    return direction
                else:
                    directions.remove(direction)  
                    if not directions:  
                        break
        return (0, 0)

    def find_valid_trap_start(self):
        """ Find a valid position for a trap
        
            Returns:
                Tuple(int, int): the row and column of the position
        """
        attempts = 0 
        while attempts < 100: 
            row = randint(1, self._room.nb_row - 2)
            col = randint(1, self._room.nb_col - 2)
            if self.is_valid_trap_position(row, col):
                return row, col
            attempts += 1
        raise ValueError("Impossible de trouver une position valide pour un piège après 100 tentatives.")
                
    def is_valid_trap_position(self, row: int, col: int) -> bool:
        """ Check if the given position is a valid position for a trap.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile

        Returns:
            bool: True if the position is valid, False otherwise
        """
        if row < 1 or row >= self._room.nb_row - 1 or col < 1 or col >= self._room.nb_col - 1:
            return False
        return (
            not self._room.is_tile(row, col, WallTile) and
            not self._room.is_tile(row, col, ExitTile)
        )
                
    def find_valid_trap_start(self)-> Tuple[int, int]:
        """ Find a valid position for a trap

        Returns:
            Tuple(int, int): the row and column of the position
        """
        while True:
            row = randint(1, self._room.nb_row - 2)
            col = randint(1, self._room.nb_col - 2)
            if self.is_valid_trap_position(row, col):
                return row, col
            
    def set_trap_sprite(self, row: int, col: int):
        """ Set the sprite for a ground tile based on its configuration. 
        
            Args:
                row (int): the row of the tile
                col (int): the column of the tile
        """
        trap_tile = self._tile_factory.create_tile("trap", TrapTileData())
        self._room.set_tile(row, col, trap_tile)
        trap_image_variant = trap_tile.dataTile.variants["full"]
        image = trap_tile.dataTile.random_tile(trap_image_variant)
        self._graphic_room.set_image(row, col, image)

    # -------------------------------- #
    # --- Water generation methods --- #
        
    def set_water(self):
        num_water_groups = randint(2, 3)
        water_positions = []

        for _ in range(num_water_groups):
            num_water_tiles = randint(5, 6)
            start_row, start_col = self.find_valid_water_start()

            for _ in range(num_water_tiles):
                if self.is_valid_water_position(start_row, start_col):
                    self.set_water_tile(start_row, start_col, "full")
                    water_positions.append((start_row, start_col))

                direction = self.choose_water_adjacent_direction(start_row, start_col, "water")
                start_row += direction[0]
                start_col += direction[1]

        for position in water_positions:
            row, col = position
            self.update_water_tile_configuration(row, col)

    def update_water_tile_configuration(self, row: int, col: int):
        """ Mettre à jour la configuration d'une tuile d'eau en fonction de ses tuiles voisines. """
        tile = self._room.get_tile(row, col)
        if isinstance(tile, WaterTile):
            configuration_strategy = self._tile_config_strategies.get('water')
            if configuration_strategy:
                configuration_key = configuration_strategy.get_configuration_key(row, col)
                image = tile.dataTile.random_tile(tile.dataTile.variants.get(configuration_key, ["full"]))
                self._graphic_room.set_image(row, col, image)

    def set_water_tile(self, row: int, col: int, configuration_key: str):
        """ Placer une tuile d'eau avec une configuration spécifiée. """
        water_tile = self._tile_factory.create_tile("water", WaterTileData())
        image = water_tile.dataTile.random_tile(water_tile.dataTile.variants[configuration_key])
        self._room.set_tile(row, col, water_tile)
        self._graphic_room.set_image(row, col, image)

    def choose_water_adjacent_direction(self, row: int, col: int, tile_type: str) -> Tuple[int, int]:
        """ Choose a direction for a tile to be placed in an adjacent tile.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile
            tile_type (str): the type of tile ('water' or 'trap')

        Returns:
            Tuple[int, int]: the direction to move in
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while directions:
            direction = choice(directions)
            new_row, new_col = row + direction[0], col + direction[1]

            valid_position_check = self.is_valid_water_position if tile_type == "water" else self.is_valid_trap_position
            if 1 <= new_row < self._room.nb_row - 1 and 1 <= new_col < self._room.nb_col - 1:
                if valid_position_check(new_row, new_col):
                    return direction
                else:
                    directions.remove(direction)
        return (0, 0)  # Retourner une direction par défaut si aucune direction n'est valide

    def find_valid_water_start(self) -> Tuple[int, int]:
        """ Find a valid position for a water tile.

        Returns:
            Tuple[int, int]: the row and column of the position
        """
        attempts = 0
        while attempts < 100:
            row = randint(1, self._room.nb_row - 2)
            col = randint(1, self._room.nb_col - 2)
            if self.is_valid_water_position(row, col):
                return row, col
            attempts += 1
        raise ValueError("Impossible de trouver une position valide pour une tuile d'eau après 100 tentatives.")

    def is_valid_water_position(self, row: int, col: int) -> bool:
        """ Check if the given position is a valid position for a water tile.

        Args:
            row (int): the row of the tile
            col (int): the column of the tile

        Returns:
            bool: True if the position is valid, False otherwise
        """
        if row < 1 or row >= self._room.nb_row - 1 or col < 1 or col >= self._room.nb_col - 1:
            return False
        return not self._room.is_tile(row, col, WallTile)
    
    # ------------------------------- #
    # Players generation methods #

    def set_players(self, players: List[Player]):
        """ Place players on adjacent ground tiles starting from a random ground tile.

        Args:
            players (List[Player]): List of player entities to place on the gameboard.
        """
        start_position = self.get_random_ground_position()
        current_position = start_position

        for player in players:
            # Assurez-vous que la position actuelle est une GroundTile et non occupée
            while not isinstance(self._room.get_tile(*current_position), GroundTile) or self._room.get_tile(*current_position).is_player_on:
                # Déplacer à une position adjacente
                current_position = self.move_to_adjacent_position(current_position)

            # Placez le joueur sur la position actuelle
            transform_component = player.get_component(TransformComponent)
            if transform_component:
                transform_component.position = [current_position[1], current_position[0]]

            # Marquer la case comme occupée par un joueur
            self._room.get_tile(*current_position).is_player_on = True

    def get_random_ground_position(self):
        """ Trouver une position aléatoire de GroundTile sur le plateau.

        Returns:
            tuple[int, int]: Position aléatoire de GroundTile.
        """
        available_positions = self.get_available_ground_positions()
        if not available_positions:
            raise ValueError("Pas de cases de terrain disponibles")
        return choice(available_positions)

    def move_to_adjacent_position(self, position):
        """ Déplacez-vous à une position adjacente valide (GroundTile non occupée).

        Args:
            position (tuple[int, int]): La position actuelle.

        Returns:
            tuple[int, int]: Nouvelle position adjacente valide.
        """
        row, col = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Haut, droite, bas, gauche

        # Essayer toutes les directions jusqu'à trouver une position valide
        shuffled_directions = sample(directions, len(directions))
        for direction in shuffled_directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            # Vérifiez si la nouvelle position est à l'intérieur des limites et est une GroundTile non occupée
            if 0 <= new_row < self._room.nb_row and 0 <= new_col < self._room.nb_col:
                tile = self._room.get_tile(new_row, new_col)
                if isinstance(tile, GroundTile) and not tile.is_player_on:
                    return (new_row, new_col)

        # Si aucune position adjacente valide n'est trouvée, retourner la position actuelle
        return position

    def get_available_ground_positions(self):
        """ Retourne une liste de positions des cases de terrain disponibles.

        Returns:
            list[tuple[int, int]]: Liste des positions des cases de terrain disponibles.
        """
        available_positions = []
        for row in range(self._room.nb_row):
            for col in range(self._room.nb_col):
                tile = self._room.get_tile(row, col)
                if isinstance(tile, GroundTile) and not tile.is_player_on:
                    available_positions.append((row, col))
        
        return available_positions