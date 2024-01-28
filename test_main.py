from gameboard import GameboardAdapter
from components import TransformComponent, SpriteRendererComponent
from manager import GameManager

if __name__ == "__main__":
    gameManager = GameManager(4)
    gameManager.start()