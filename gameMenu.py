from __future__ import annotations
import pygame
from constant import SCREEN_HEIGHT, SCREEN_WIDTH, EXIT_OPEN, TRANSPARENT, PIXELIFY, ICON_SIZE
from gameloop import Gameloop
from cases import Water, Trap, Portal, Exit, Market
from entities import Player, Skeleton, Slime, Bat, Golem
from graphics import Button, Slider


class GameMenu:
    """
    The game menu which draw all the contents about the game menu (gameboard, inventory, informations, etc...)
    """
    

    def __init__(self, screen_mode: str = "Fullscreen"):
        """
        Initialization of the game menu
        Args:
            screen_mode (str): The current screen mode of the graphic interface. Default to fullscreen
        """
        self.game_running = True
        self.screen_mode = screen_mode
        self.initialize_game()

    def initialize_game(self):
        """
        Initialization of the game (Background image, creating the gameboard, etc...)
        """
        pygame.init()

        self.background = pygame.image.load("images/background.png")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        if self.screen_mode == "Fullscreen":
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 60))
        self.screen.blit(self.background, (0,0))

        self.menu_actif = "Main"
        self.main_menu = True

        self.gameloop = Gameloop(1, None, 0, pygame.sprite.Group())

        self.entity_group = self.gameloop.entity_group
        self.sprite_group = pygame.sprite.Group()

        self.InitializeButton()

        self.gameloop.createLevel(self.screen)
        
        self.turn = 0
        self.gameloop.updateRoom(self.screen, self.turn)

        self.movable = True

    def InitializeButton(self: GameMenu):
        """
        Initialize all the game menu buttons
        """
        self.buttons = self.gameloop.buttons

        # Initialize all menu button (execpt inventories button)
        self.menu_buttons = []
        self.options_buttons = []

        self.menu_buttons.append(Button(50, SCREEN_HEIGHT // 1.25 - 20, 200, 50, "Settings", self.openSettings))
        self.menu_buttons.append(Button(SCREEN_WIDTH // 1.25, SCREEN_HEIGHT // 1.125 - 20, 200, 50, "Skip", self.skipTurn))

        self.options_buttons.append(Button(SCREEN_WIDTH - 50, 0, 50, 50, "X", self.setMenu))
        self.options_buttons.append(Button(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT // 3 + 80, 50, 50, "Leave", self.backToMainMenu))
        self.slider = Slider(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 3, 400, 50, 0.25, 0.0, 0.25, self.setVolume)

    def backToMainMenu(self: GameMenu):
        """
        Come back to the main menu
        """
        self.game_running = False
        self.main_menu = True
        
    def openSettings(self: GameMenu):
        """
        Open the settings menu
        """
        self.menu_actif = "Settings"
        pygame.display.flip()

    def setMenu(self):
        """
        Set the menu to the main menu of the game menu.
        """
        self.menu_actif = "Main"
        self.update()
    
    def setVolume(self, volume: float):
        """
        Set the music volume
        Args:
            volume(float): the volume of the music
        """
        pygame.mixer.music.set_volume(volume)

    def skipTurn(self):
        """
        Skip the current entity turn and go to the next
        """
        self.turn += 1
        if self.turn >= len(self.gameloop.turn_list):
            self.turn = 0
        self.gameloop.tour += 1
        self.gameloop.turn.current_action_point = self.gameloop.turn.action_point
        self.sprite_group.empty()

    def drawSettingsScreen(self):
        """
        Draw the settings menu
        """
        font = pygame.font.Font(PIXELIFY, 36)

        text_above = font.render("Settings", True, (255, 255, 255))
        text_above_rect = text_above.get_rect()
        text_above_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 - 50)
        self.screen.blit(text_above, text_above_rect)

        text_volume = font.render("Volume", True, (255, 255, 255))
        text_volume_rect = text_volume.get_rect()
        text_volume_rect.center = (SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 3 + 25)
        self.screen.blit(text_volume, text_volume_rect)

    def run(self):
        """
        What the game menu do while it is activated
        """
        self.update()
        while self.game_running:
            self.handle_events()        

    def update(self):
        """
        Update all the contents of the game menu interface
        """
        self.gameloop.updateRoom(self.screen, self.turn)
        self.entity_group.update()
        self.entity_group.draw(self.screen)
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)

        if self.menu_actif == "Main":
            for button in self.menu_buttons:
                button.draw(self.screen)
              
        font = pygame.font.Font(PIXELIFY, 28)
        for player in self.gameloop.players:
            if player == self.gameloop.turn:  
                image = pygame.image.load(player.image_path)
                image = pygame.transform.scale(image, (ICON_SIZE, ICON_SIZE))
                rect = image.get_rect()
                rect.x = 100
                rect.y = SCREEN_HEIGHT // 1.25 + 20
                self.screen.blit(image, rect)
                
                # Define the position of the player actions points information text
                text_action_point = font.render(f"Action points : {player.current_action_point}", True, (255, 255, 255))
                text_action_point_rect = text_action_point.get_rect()
                text_action_point_rect.x = SCREEN_WIDTH // 4
                text_action_point_rect.y = SCREEN_HEIGHT - 150
                self.screen.blit(text_action_point, text_action_point_rect)
                
                # Define the position of the player dmages information text
                text_damage = font.render(f"Damages : {player.damage}", True, (255, 255, 255))
                text_damage_rect = text_damage.get_rect()
                text_damage_rect.x = SCREEN_WIDTH // 4
                text_damage_rect.y = SCREEN_HEIGHT - 120
                self.screen.blit(text_damage, text_damage_rect)
                
                # Define the position of the room created number text
                text_room = font.render(f"Rooms : {self.gameloop.room}", True, (255, 255, 255))
                text_room_rect = text_room.get_rect()
                text_room_rect.x = SCREEN_WIDTH // 2
                text_room_rect.y = SCREEN_HEIGHT - 120
                self.screen.blit(text_room, text_room_rect)
                
                # Define the position of the tour played number text
                text_round = font.render(f"Round : {self.gameloop.tour}", True, (255, 255, 255))
                text_round_rect = text_round.get_rect()
                text_round_rect.x = SCREEN_WIDTH // 2
                text_round_rect.y = SCREEN_HEIGHT - 150
                self.screen.blit(text_round, text_round_rect)
                
                # Define the position of the levers left text
                text_lever = font.render(f"Levers Left : {self.gameloop.exit_levers}", True, (255, 255, 255))
                text_lever_rect = text_lever.get_rect()
                text_lever_rect.x = SCREEN_WIDTH // 1.5
                text_lever_rect.y = SCREEN_HEIGHT - 150
                self.screen.blit(text_lever, text_lever_rect)
                


        pygame.display.flip()

    def handle_events(self):
        """
        All pygame events (button pressed, player move, player attack, entities turn, etc...)
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False

            # Keyboard events
            if event.type == pygame.KEYDOWN:

                # If escape pressed, leave the game
                if event.key == pygame.K_ESCAPE:
                    self.backToMainMenu()

                # Right key events
                if event.key == pygame.K_RIGHT:

                    # Change turn
                    self.turn += 1
                    if self.turn >= len(self.gameloop.turn_list):
                        self.turn = 0
                    self.gameloop.tour += 1
                    self.gameloop.turn.current_action_point = self.gameloop.turn.action_point

                    USE_ITEM = False
                    self.buttons = self.gameloop.buttons
                    self.sprite_group.empty()
                    self.update()
                    
                    # If an entity start on a water case, he have less action point
                    if self.gameloop.isCell(self.gameloop.turn, Water):
                        self.gameloop.turn.current_action_point = self.gameloop.turn.action_point - self.gameloop.getCell(self.gameloop.turn).slowness
                        if self.gameloop.turn.current_action_point < 0:
                            self.gameloop.turn.current_action_point = 0


            # Mouse buttons events
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Left click events
                if event.button == 1:


                    PLAYER_EXIT_ACTION = False
                    USE_ITEM = False
                    MARKET = False
                    
                    if self.menu_actif == "Main":
                        for sprite in self.sprite_group:

                            # When a player move
                            if sprite.rect.collidepoint(event.pos) and sprite.utility == "movement" and isinstance(self.gameloop.turn, Player) and self.movable:
                                TRAPPED = False
                                self.gameloop.setCellEntity(self.gameloop.turn, None)
                                self.gameloop.entity_group = self.gameloop.turn.move(sprite.location, self.gameloop.entity_group)
                                self.update()
                                self.movable = False

                                # if move on the exit (and the exit is open)
                                if self.gameloop.isCell(self.gameloop.turn, Exit) and self.gameloop.getCell(self.gameloop.turn).tile == EXIT_OPEN:
                                    PLAYER_EXIT_ACTION = True
                                    if self.gameloop.turn not in self.gameloop.exit_list:
                                        self.gameloop.exit_list.append(self.gameloop.turn)
                                    self.gameloop.turn_list.remove(self.gameloop.turn)
                                    for entity in self.gameloop.entity_group:
                                        if entity == self.gameloop.turn:
                                            self.gameloop.entity_group.remove(entity)
                                            entity.kill()
                                            self.turn += 1
                                            if self.turn >= len(self.gameloop.turn_list):
                                                self.turn = 0
                                            self.gameloop.turn.current_action_point = self.gameloop.turn.action_point
                                            USE_ITEM = False
                                            self.sprite_group.empty()

                                # When the player is on a water case
                                if self.gameloop.isCell(self.gameloop.turn, Water):
                                    self.gameloop.turn.current_action_point -= self.gameloop.gameboard.grid[self.gameloop.turn.location[0]][self.gameloop.turn.location[1]].slowness
                                    if self.gameloop.turn.current_action_point < 0:
                                        self.gameloop.turn.current_action_point = 0
                                    self.update()

                                # When a player is on a trap
                                if self.gameloop.isCell(self.gameloop.turn, Trap) and not TRAPPED:
                                    TRAPPED = True
                                    self.gameloop.setCellEntity(self.gameloop.turn, self.gameloop.turn)
                                    self.gameloop.turn.current_health -= self.gameloop.getCell(self.gameloop.turn).damage
                                    if self.gameloop.turn.current_health <= 0:
                                        self.gameloop.turn.is_dead = True
                                        self.gameloop.current_action_point = 0
                                        self.turn += 1
                                        if self.turn >= len(self.gameloop.turn_list):
                                            self.turn = 0
                                        self.gameloop.tour += 1
                                        self.gameloop.turn.current_action_point = self.gameloop.turn.action_point
                                        USE_ITEM = False
                                        self.update()

                                # When a player go throught a portal
                                if self.gameloop.isCell(self.gameloop.turn, Portal):
                                    self.gameloop.entity_group = self.gameloop.turn.move(self.gameloop.getCell(self.gameloop.turn).target.pos, self.gameloop.entity_group)
                                    self.gameloop.setCellEntity(self.gameloop.turn, self.gameloop.turn)
                                    self.gameloop.turn.current_action_point = 0
                                    self.update()

                                # When a player is in a market place
                                if self.gameloop.isCell(self.gameloop.turn, Market) and not MARKET:
                                    MARKET = True
                                    self.gameloop.getCell(self.gameloop.turn).buyRandomItem(self.gameloop.turn)
                                    self.gameloop.setCellEntity(self.gameloop.turn, self.gameloop.turn)
                                    self.update()
                                
                                # If just a normal case
                                else:
                                    self.gameloop.setCellEntity(self.gameloop.turn, self.gameloop.turn)

                                # Verify if all players are left
                                if len(self.gameloop.exit_list) >= len(self.gameloop.players):
                                    for entity in self.entity_group:
                                        if not isinstance(entity, Player):
                                            self.gameloop.entity_group.remove(entity)
                                    self.gameloop.entity_group = self.entity_group
                                    self.gameloop.resetGameLoop()
                                    self.gameloop.createLevel(self.screen)
                                    self.turn = 0
                                    self.gameloop.turn.current_action_point = self.gameloop.turn.action_point
                                    USE_ITEM = False
                                    break
                                self.sprite_group.empty()
                                self.update()

                            # When a player attack an entity
                            elif sprite.rect.collidepoint(event.pos) and sprite.utility == "attack":
                                self.gameloop.entity_group, self.gameloop.turn_list = self.gameloop.turn.attack(self.gameloop.gameboard.grid[sprite.location[0]][sprite.location[1]].entity, self.gameloop.gameboard.grid, self.gameloop.turn_list, self.entity_group)
                                possible_position, possible_attack, possible_levers, items_possible = self.gameloop.turn.getAllActions(self.gameloop.gameboard.grid, self.gameloop.items_sprite_location, self.gameloop.gameboard.nb_row, self.gameloop.gameboard.nb_col)
                                self.sprite_group = self.gameloop.gameboard.drawPossibleMovements(possible_position, possible_attack, possible_levers, items_possible,self.sprite_group)
                                self.update()
                            
                            # When a player activate a lever
                            elif sprite.rect.collidepoint(event.pos) and sprite.utility == "lever":
                                self.sprite_group = self.gameloop.turn.activateLever(self.gameloop.gameboard.grid[sprite.location[0]][sprite.location[1]],self.sprite_group)
                                self.gameloop.exit_levers -= 1
                                possible_position, possible_attack, possible_levers, items_possible = self.gameloop.turn.getAllActions(self.gameloop.gameboard.grid, self.gameloop.items_sprite_location, self.gameloop.gameboard.nb_row, self.gameloop.gameboard.nb_col)
                                self.sprite_group = self.gameloop.gameboard.drawPossibleMovements(possible_position, possible_attack, possible_levers, items_possible,self.sprite_group)
                                self.update()

                            # When a player take an item
                            elif sprite.rect.collidepoint(event.pos) and sprite.utility == "item":
                                self.gameloop.setCellEntity(self.gameloop.turn, None)
                                self.gameloop.entity_group = self.gameloop.turn.move(sprite.location, self.gameloop.entity_group)
                                self.gameloop.setCellEntity(self.gameloop.turn, self.gameloop.turn)
                                for item in self.gameloop.items:
                                    if self.gameloop.turn.location == item.location:
                                        self.gameloop.turn = item.itemProperties(self.gameloop.turn)
                                        for item_sprite in self.gameloop.items_sprite:
                                            if item_sprite.location == item.location:
                                                self.gameloop.entity_group.remove(item_sprite)
                                                self.gameloop.items_sprite_location.remove(item_sprite.location)
                                                self.gameloop.items.remove(item)
                                                item_sprite.kill()
                                possible_position, possible_attack, possible_levers, items_possible = self.gameloop.turn.getAllActions(self.gameloop.gameboard.grid, self.gameloop.items_sprite_location, self.gameloop.gameboard.nb_row, self.gameloop.gameboard.nb_col)
                                self.sprite_group = self.gameloop.gameboard.drawPossibleMovements(possible_position, possible_attack, possible_levers, items_possible,self.sprite_group)
                                self.update()

                    # inventory buttons display
                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos) and not USE_ITEM:
                            USE_ITEM = True
                            button.useItem(self.gameloop.turn)
                            self.buttons.remove(button)
                            possible_position, possible_attack, possible_levers, items_possible = self.gameloop.turn.getAllActions(self.gameloop.gameboard.grid, self.gameloop.items_sprite_location, self.gameloop.gameboard.nb_row, self.gameloop.gameboard.nb_col)
                            self.sprite_group = self.gameloop.gameboard.drawPossibleMovements(possible_position, possible_attack, possible_levers, items_possible,self.sprite_group)
                            self.update()

                    # Draw all actions when the current player is clicked
                    if self.gameloop.turn.rect.collidepoint(event.pos):
                        if (isinstance(self.gameloop.turn, Player) and not PLAYER_EXIT_ACTION):
                            possible_position, possible_attack, possible_levers, items_possible = self.gameloop.turn.getAllActions(self.gameloop.gameboard.grid, self.gameloop.items_sprite_location, self.gameloop.gameboard.nb_row, self.gameloop.gameboard.nb_col)
                            self.sprite_group = self.gameloop.gameboard.drawPossibleMovements(possible_position, possible_attack, possible_levers, items_possible,self.sprite_group)
                            self.movable = True
                            self.update()

                    # When pressed a menu button
                    for button in self.menu_buttons:
                            if button.rect.collidepoint(event.pos):
                                button.action()

                    # When pressed a menu button (Settings menu)
                    if self.menu_actif == "Settings":
                        for button in self.options_buttons:
                            if button.rect.collidepoint(event.pos):
                                button.action()

                    # When you are clicking on the slider, you are dragging it
                    if self.menu_actif == "Settings":
                        if self.slider.rect.collidepoint(event.pos):
                            self.slider.dragging = True

            # Mouse Motion events
            if event.type == pygame.MOUSEMOTION:

                mouse_pos = pygame.mouse.get_pos()

                # Draw the action sprite hover when the cursor is on the sprite
                if self.menu_actif == "Main":
                    for sprite in self.sprite_group:
                        if not sprite.is_target() and sprite.rect.collidepoint(mouse_pos):
                            sprite.set_target()
                            self.sprite_group.update()
                            self.sprite_group.draw(self.screen)
                            pygame.display.flip()
                        elif sprite.is_target() and not sprite.rect.collidepoint(mouse_pos):
                            sprite.set_movement()
                            self.sprite_group.update()
                            self.sprite_group.draw(self.screen)
                            pygame.display.flip()

                
                # Hover when the cursor is on a button
                for button in self.menu_buttons:
                    button.clicked = button.isHovered()
                    if button.clicked:
                        button.draw(self.screen)

                # Hover when the cursor is on a button (Settings menu)
                for button in self.options_buttons:
                    button.clicked = button.isHovered()
                    if button.clicked:
                        button.draw(self.screen)

                # Dragging the slider to set the music volume
                if self.slider.rect.collidepoint(event.pos) and self.slider.dragging:
                    x = event.pos[0]
                    x = max(self.slider.rect.x, min(self.slider.rect.right - 20, x))
                    self.slider.value = self.slider.min + (x - self.slider.rect.x) / (self.slider.rect.width - 20) * (self.slider.max - self.slider.min)
                    self.slider.action(self.slider.value)

            # Verify if all player are dead
            dead = 0
            for player in self.gameloop.players:
                if player.is_dead:
                    dead += 1
                    player.current_action_point = 0
                    if dead >= len(self.gameloop.players):
                        self.game_running = False

                # If player alive, entities turn
                if isinstance(self.gameloop.turn, (Skeleton, Bat, Golem, Slime)):
                    self.gameloop.entityTurn(self.entity_group)
                    self.turn += 1
                    if self.turn >= len(self.gameloop.turn_list):
                        self.turn = 0
                    self.gameloop.tour += 1
                    self.gameloop.turn.current_action_point = self.gameloop.turn.action_point
                    self.sprite_group.empty()

                    self.update()

            # When left button is up, it means you are not dragging anymore
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.slider.dragging = False

            if self.menu_actif == "Main":
                self.update()
            elif self.menu_actif == "Settings":
                self.renderSettings()
            


        pygame.display.flip()

    def renderSettings(self: GameMenu):
        """
        Update the settings menu
        """
        self.gameloop.updateRoom(self.screen, self.turn)
        
        self.overlay.fill(TRANSPARENT)
        self.screen.blit(self.overlay, (0, 0))

        for button in self.options_buttons:
            button.draw(self.screen)
        self.slider.draw(self.screen, (255, 255, 255))

        self.drawSettingsScreen()
        
        pygame.display.flip()