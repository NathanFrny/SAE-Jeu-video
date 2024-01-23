from __future__ import annotations
import pygame

class Slider:
    """
    Class that represent a slider for settings menu options
    """
    
    def __init__(self: Slider, x: int, y: int, width: int, height: int, initial: float, minimum: float, maximum: float, action: callable):
        """
        Initialize the slider
        Args:
            x (int): The x position of the slider
            y (int): The y position of the slider
            width (int): The width of the slider
            height (int): The height of the slider
            initial (float): The initial value of the slider
            minimum (float): The minimum value of the slider
            maximum (float): The maximum value of the slider
            action (callable): The fonction that we call when the slider is modified
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.initial = initial
        self.min = minimum
        self.max = maximum
        self.action = action
        self.value = initial
        self.dragging = False

    def draw(self: Slider, screen: pygame.Surface, color: tuple(int, int, int)):
        """
        Draw the slider on the graphic interface
        Args:
            screen (pygame.Surface): The screen
            color (tuple(int, int, int)): The color of the slider
        """
        # Barre du slider
        bar_color = color
        bar_width = self.rect.width - 20
        bar_height = 10
        bar_x = self.rect.x + 10
        bar_y = self.rect.centery - bar_height // 2
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width, bar_height))

        # Curseur du slider
        cursor_width = 20
        cursor_height = self.rect.height
        cursor_x = self.rect.x + (self.value - self.min) / (self.max - self.min) * (self.rect.width - cursor_width)
        cursor_y = self.rect.y
        cursor_color = (255, 255, 0)
        pygame.draw.rect(screen, cursor_color, (cursor_x, cursor_y, cursor_width, cursor_height))