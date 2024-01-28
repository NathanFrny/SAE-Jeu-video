from gameboard import GameboardAdapter
from components import TransformComponent, SpriteRendererComponent
from entities.Player import Player
from utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

def main():
    players = [
        Player("Player 1", "images/player1.png"),
        Player("Player 2", "images/player2.png"),
        Player("Player 3", "images/player3.png"),
        Player("Player 4", "images/player4.png")
    ]

    players[0].get_component(TransformComponent).position = [3, 4]
    players[1].get_component(TransformComponent).position = [4, 4]
    players[2].get_component(TransformComponent).position = [5, 4]
    players[3].get_component(TransformComponent).position = [6, 4]

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

    for player in players:
        position = player.get_component(TransformComponent).position
        tile = adapter.gameboard.get_tile(position[0], position[1])
        tile.is_player_on = True
    
    # Mettez à jour l'affichage
    pygame.display.flip()
    
    # Boucle d'événements pour garder la fenêtre ouverte
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Effacez l'écran à chaque tour de boucle
        screen.fill((0, 0, 0))

        # Dessinez le plateau de jeu
        adapter.graphic_gameboard.draw(screen)

        # Mettez à jour et dessinez chaque joueur
        for player in players:
            player.update()
            sprite = player.get_component(SpriteRendererComponent)
            if sprite:
                screen.blit(sprite.image, sprite.rect)

        # Actualisez l'écran
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()