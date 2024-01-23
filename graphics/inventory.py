from __future__ import annotations
import pygame
from entities import Player
from items import Item
from constant import ICON_SIZE, GAP, INVENTORY_X, PIXELIFY



class Inventory():
    """
    The inventory class that represent the players common inventory
    """

    def __init__(self: Inventory):
        """
        Initialization of the inventory
        """
        self._buttons = []
        
    @property
    def buttons(self: Inventory):
        return self._buttons
    @buttons.setter
    def buttons(self: Inventory, buttons: list[Button]):
        self._buttons = buttons

    def drawInventory(self: Inventory, player: Player, screen: pygame.Surface):
        """
        Draw the inventory of the player on the screen
        Args:
            player(Player): The player inventories that we have to draw
            screen(pygame.Surface): The screen
        """
        # definine default position
        item_posx = INVENTORY_X
        item_posy = ICON_SIZE // 1.5
        
        self.buttons = []

        # Define the inventory name
        font = pygame.font.Font(PIXELIFY, 28)
        sub_font = pygame.font.Font(PIXELIFY, 22)
        text = font.render(f"{player.name}'s Inventory", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.centerx = INVENTORY_X + ICON_SIZE // 2 + 100
        text_rect.y = ICON_SIZE // 4
        screen.blit(text, text_rect)

        for item in player.inventory:
            # Define the item icon
            item_image = pygame.image.load(item.image)
            item_image = pygame.transform.scale(item_image, (ICON_SIZE // 1.5, ICON_SIZE // 1.5))
            item_rect = item_image.get_rect()
            item_rect.x = item_posx
            item_rect.y = item_posy
            screen.blit(item_image, item_rect)

            # Define the item name text
            item_name_text = font.render(type(item).__name__, True, (255, 255, 255))
            item_name_rect = item_name_text.get_rect()
            item_name_rect.x = item_posx + ICON_SIZE // 1.5 + 10
            item_name_rect.centery = item_posy + ICON_SIZE // 3 - 25
            screen.blit(item_name_text, item_name_rect)

            # Define the item description text
            max_description_width = 200  # max depht of the description
            item_description_lines = []
            description_words = item.description.split()
            current_line = ""
            
            # Vertify if don't bigger than max depth
            for word in description_words:
                test_line = current_line + " " + word if current_line else word
                test_text = sub_font.render(test_line, True, (255, 255, 255))
                
                if test_text.get_width() <= max_description_width:
                    current_line = test_line
                else:
                    item_description_lines.append(current_line)
                    current_line = word
            
            if current_line:
                item_description_lines.append(current_line)
            
            item_description_y = item_posy + ICON_SIZE // 1.5
            
            # Set the texte line by line
            for line in item_description_lines:
                item_description_text = sub_font.render(line, True, (255, 255, 255))
                item_description_rect = item_description_text.get_rect()
                item_description_rect.x = item_posx + ICON_SIZE // 1.5 + 10
                item_description_rect.y = item_description_y - 50
                screen.blit(item_description_text, item_description_rect)
                item_description_y += item_description_text.get_height()

            use_button = Button(item_posx + 25, item_description_y - 20, 100, 40, "Use", item.itemProperties, item, player)
            use_button.draw(screen)
            self.buttons.append(use_button)

            item_posy += GAP * 1.5
            

class Button:
    """
    Class button that it used to make all the game buttons
    """
    def __init__(self: Button, x: int, y: int, width: int, height: int, text: pygame.font.Font, action: callable, item: Item = None, player: Player = None):
        """
        Initialization of the button
        Args:
            x (int): the x position of the button
            y (int): the y position of the button
            width (int): the width o the button
            height (int): the height of the button
            text (pygame.font.Font): The text that is writted on the button
            action (callable): the fonction that is call when the button is pressed
            item (Item|None): The item that is used when the button is pressed. If it exist. By default to None
            player (Player|None): The player that represent the button. If it exist. By default to None
        """
        self.rect = pygame.Rect(x, y, width, height)    
        self.text = text
        self.action = action
        self.font = pygame.font.Font(PIXELIFY, 36)
        self.clicked = False
        self.item = item
        self.player = player

    def draw(self, screen):
        """
        Draw the button on the screen
        Args:
            screen (pygame.Surface): The screen
        """
        if self.clicked:
            text_color = (80, 80, 80)  # Couleur du texte lorsqu'il est survolé
        else:
            text_color = (255, 255, 255)  # Couleur du texte par défaut

        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)
        
    def drawTriangleLeft(self, screen):
        """
        Draw a left positioned triangle on the screen
        Args:
            screen (pygame.Surface): The screen
        """
        # Dimensions du triangle
        triangle_width = 20
        triangle_height = self.rect.height

        # Coordonnées du triangle
        x = self.rect.left  # Même x que le bouton
        y = self.rect.top  # Même y que le bouton

        # Points du triangle
        points = [(x, y + triangle_height // 2),  # Point gauche
                  (x + triangle_width, y),         # Point supérieur droit
                  (x + triangle_width, y + triangle_height)]  # Point inférieur droit

        pygame.draw.polygon(screen, (255, 255, 255), points)  # Dessine un triangle noir

    def drawTriangleRight(self, screen):
        """
        Draw a right positioned triangle on the screen
        Args:
            screen (pygame.Surface): The screen
        """
        # Dimensions du triangle
        triangle_width = 20
        triangle_height = self.rect.height

        # Coordonnées du triangle
        x = self.rect.right - triangle_width  # Même x que le bouton, ajusté pour pointer vers la droite
        y = self.rect.top  # Même y que le bouton
        # Points du triangle
        points = [(x, y),  # Point supérieur gauche
                  (x + triangle_width, y + triangle_height // 2),  # Point droit
                  (x, y + triangle_height)]  # Point inférieur gauche

        pygame.draw.polygon(screen, (255, 255, 255), points)  # Dessine un triangle noir

    def isHovered(self: Button):
        """
        Return if a button is hovered by the cursor
        """
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def useItem(self: Button, player: Player):
        """
        Use the item selected in the inventory menu of the player
        Args:
            player(Player): the player that use the item
        """
        self.action(player)
        for item in player.inventory:
            if self.item.equals(item):
                player.inventory.remove(item)
        del self