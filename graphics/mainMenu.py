from __future__ import annotations
import pygame
from constant import SCREEN_HEIGHT, SCREEN_WIDTH, TRANSPARENT, PIXELIFY, TITLE
from graphics import Button, Slider


class MainMenu:
    """
    The main menu of the game. It's the first interface we see and allow player to start a new games, go to tutorial or go to settings menu
    """
    def __init__(self):
        """
        Initialization of the main menu
        """
        pygame.init()
        
        # Music Initializer
        pygame.mixer.init()
        pygame.mixer.music.load("musics/gloriousmorning.wav")
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1) # Loop

        pygame.display.set_caption("Escape the Dungeons")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.actual_screen = "Fullscreen"
        self.running = True
        self.game_running = False
        self.menu_actif = "Main"
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.tutorial_buttons = []
        self.options_buttons = []
        self.index = 0
        self.tutorial_screens = ["Gameboard","Players", "Ennemies", "Levers", "Exit", "Items", "Traps", "Water", "Teleporters", "Move", "Attack", "Active levers"]
        self.initialize_buttons()
        self.initaliaze_tutorial_buttons()
        self.initialize_options_buttons()
        self.clock = pygame.time.Clock()
        
        
        self.frames = [pygame.image.load(f"images/backgroundFrames/frame_{i+1}.png") for i in range(35)]
        self.frames = [pygame.transform.scale(frame, (SCREEN_WIDTH, SCREEN_HEIGHT)) for frame in self.frames]
        self.frame_index = 0

    def initialize_buttons(self):
        """
        Initialization of the main menu buttons
        """
        self.buttons = []
        self.buttons.append(Button(SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 2 - 120, 200, 50, "New game", self.startGame))
        self.buttons.append(Button(SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 2 - 60, 200, 50, "Tutorial", self.tutorial))
        self.buttons.append(Button(SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 2, 200, 50, "Settings", self.openSettings))
        self.buttons.append(Button(SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 1.5 + 60, 200, 50, "Quit the game", self.quitGame))

    def initaliaze_tutorial_buttons(self):
        """
        Initialization of the tutorial menu buttons
        """
        self.tutorial_buttons.append(Button(50, SCREEN_HEIGHT // 2 - 100, 50, 50, "Previous", self.previous))
        self.tutorial_buttons.append(Button(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 - 100, 50, 50, "Next", self.next))
        self.tutorial_buttons.append(Button(SCREEN_WIDTH - 50, 0, 50, 50, "X", self.setMenu))
        
    def initialize_options_buttons(self):
        """
        Initialization of the settings menu buttons
        """
        self.options_buttons.append(Button(SCREEN_WIDTH - 50, 0, 50, 50, "X", self.setMenu))
        self.options_buttons.append(Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 80, 50, 50, "Change screen mode", self.changeScreenMode))
        self.slider = Slider(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 3, 400, 50, 0.25, 0.0, 0.25, self.setVolume)

    def setMenu(self):
        """
        Set the menu to "Main" which means that we are in the main menu
        """
        self.menu_actif = "Main"

    def startGame(self):
        """
        Start a new game
        """
        self.game_running = True
        self.running = False

    def openSettings(self):
        """
        Open the settings menu
        """
        self.menu_actif = "Options"
        self.overlay.fill(TRANSPARENT)
        self.screen.blit(self.overlay, (0, 0))
        pygame.display.flip()
    
    def tutorial(self):
        """
        Open the tutorial menu
        """
        self.menu_actif = "Tutorial"
        self.index = 0
        self.tutorial_screens = ["Gameboard","Players", "Ennemies", "Levers", "Exit", "Items", "Traps", "Water", "Teleporters", "Move", "Attack", "Active levers"]
        self.actual_tutorial = self.tutorial_screens[0]
        self.overlay.fill(TRANSPARENT)
        self.screen.blit(self.overlay, (0, 0))
        pygame.display.flip()

    def quitGame(self):
        """
        Quit the game
        """
        self.game_running = False
        self.running = False
        
    def previous(self):
        """
        Go to previous tutorial images
        """
        if self.index >= 1:
            self.actual_tutorial = self.tutorial_screens[self.index - 1]
            self.index -= 1
    
    def next(self):
        """
        Go to next tutorial images
        """
        if self.index <= len(self.tutorial_screens) - 2:
            self.actual_tutorial = self.tutorial_screens[self.index + 1]
            self.index += 1
    
    def drawTutorialScreen(self):
        """
        Draw the tutorial Menu
        """
        image_filename = f"images/tutorial/{self.actual_tutorial}.png"

        try:
            tutorial_image = pygame.image.load(image_filename)

            max_width = SCREEN_WIDTH - 100 
            max_height = SCREEN_HEIGHT - 100 
            if tutorial_image.get_width() > max_width or tutorial_image.get_height() > max_height:
                tutorial_image = pygame.transform.scale(tutorial_image, (max_width // 2, max_height // 2))

            image_x = (SCREEN_WIDTH - tutorial_image.get_width()) // 2
            image_y = (SCREEN_HEIGHT - tutorial_image.get_height()) // 2

            self.screen.blit(tutorial_image, (image_x, image_y))

            font = pygame.font.Font(PIXELIFY, 36)

            text_above = font.render(f"{self.actual_tutorial}", True, (255, 255, 255))
            text_above_rect = text_above.get_rect()
            text_above_rect.center = (SCREEN_WIDTH // 2, image_y - 50)
            self.screen.blit(text_above, text_above_rect)

            text_below = font.render(f"{self.index + 1}", True, (255, 255, 255))
            text_below_rect = text_below.get_rect()
            text_below_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
            self.screen.blit(text_below, text_below_rect)

        except pygame.error:
            font = pygame.font.Font(None, 36)
            text = font.render("Image introuvable", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.screen.blit(text, text_rect)

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

    def setVolume(self, volume: float):
        """
        Set the music volume
        """
        pygame.mixer.music.set_volume(volume)

    def changeScreenMode(self):
        """
        Change the screen mode between fullscreen and windowed
        """
        if self.actual_screen == "Normal":
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
            self.actual_screen = "Fullscreen"
        else:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 60))
            self.actual_screen = "Normal"

    def run(self):
        """
        All the events (when we press a buton, when we leave, all the hovers, etc...)
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Left the game when escape button is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                # Button left events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in self.buttons:
                            if button.rect.collidepoint(event.pos):
                                button.action()

                        for button in self.options_buttons:
                            if button.rect.collidepoint(event.pos):
                                button.action()
                        
                        # Next or Previous image while you are clicking on the right or left arrow (Back to the menu when X button)
                        for button in self.tutorial_buttons:
                            if button.rect.collidepoint(event.pos) and button.text == "Previous":
                                button.action()
                            if button.rect.collidepoint(event.pos) and button.text == "Next":
                                button.action()
                            if button.rect.collidepoint(event.pos) and button.text == "X":
                                button.action()

                    # When you are clicking on the slider, you are dragging it
                    if self.slider.rect.collidepoint(event.pos):
                        self.slider.dragging = True
                                
                # Cursor motion events
                if event.type == pygame.MOUSEMOTION:

                    # Hover when the cursor is on a button
                    for button in self.buttons:
                        button.clicked = button.isHovered()
                        if button.clicked:
                            button.draw(self.screen)

                    # Hover when the cursor is on a button (settings menu)
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
                
                # When left button is up, it means you are not dragging anymore
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.slider.dragging = False

                        
            if self.menu_actif == "Main":
                self.render()
            elif self.menu_actif == "Tutorial":
                self.renderTutorial()
            elif self.menu_actif == "Options":
                self.renderSettings()

    def render(self):
        """
        Render the main menu in the graphic interface
        """
        self.screen.blit(self.frames[self.frame_index], (0, 0))
        self.frame_index = (self.frame_index + 1) % len(self.frames)

        for button in self.buttons:
            if button.text != "X":
                button.draw(self.screen)

        image = pygame.image.load(TITLE)
        rect = image.get_rect()
        rect.x = SCREEN_WIDTH // 4
        rect.y = SCREEN_HEIGHT // 3
        self.screen.blit(image, rect)

        pygame.display.flip()
        self.clock.tick(16)
        
    def renderTutorial(self):
        """
        Render the tutorial menu in the graphic interface
        """
        self.screen.blit(self.frames[self.frame_index], (0, 0))
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.screen.blit(self.overlay, (0, 0))
        
        for button in self.tutorial_buttons:
            if button.text == "Previous":
                button.drawTriangleLeft(self.screen)
            elif button.text == "Next":
                button.drawTriangleRight(self.screen)
            elif button.text == "X":
                button.draw(self.screen)
                
        self.drawTutorialScreen()
            
        pygame.display.flip()
        self.clock.tick(16)
    
    def renderSettings(self):
        """
        Render the settings menu in the graphic interface
        """
        self.screen.blit(self.frames[self.frame_index], (0, 0))
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.screen.blit(self.overlay, (0, 0))
        
        for button in self.options_buttons:
            button.draw(self.screen)
        self.slider.draw(self.screen, (255, 255, 255))
        
        self.drawSettingsScreen()

        pygame.display.flip()
        self.clock.tick(16)