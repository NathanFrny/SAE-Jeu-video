from graphics import MainMenu
from gameMenu import GameMenu
import pygame

if __name__ == "__main__":
    main_menu = MainMenu()
    running = True
    while running:
        
        if not main_menu.game_running:
            main_menu.run()

        if not main_menu.running and not main_menu.game_running:
            running = False

        if main_menu.game_running:
            game_menu = GameMenu(main_menu.actual_screen)
            game_menu.run()

            if game_menu.main_menu == True:
                main_menu.running = True
                main_menu.game_running = False
            else:
                running = False

        

    pygame.quit()