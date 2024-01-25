from gameboard import GameboardAdapter, GraphicGameboard
from utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

def main():
    # Initialise Pygame
    pygame.init()

    # Créez une fenêtre de la taille du plateau de jeu
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 10))

    # Créez une instance de GameboardAdapter
    adapter = GameboardAdapter()

    # Utilisez la méthode draw pour dessiner le plateau de jeu
    adapter.draw()
    
    # Dessinez le plateau de jeu sur l'écran
    adapter.graphic_gameboard.draw(screen)
    
    # Mettez à jour l'affichage
    pygame.display.flip()
    
    # Boucle d'événements pour garder la fenêtre ouverte
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()