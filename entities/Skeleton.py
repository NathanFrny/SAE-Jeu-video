from .abstract.Monster import Monster

class Skeleton(Monster):
    def __init__(self, image_path: str, health: int, action_point: int, damages: int):
        super().__init__(image_path, health, action_point, damages)
        
    # ---------------------------------------------------------------- #
    # ------------------------ Methods ------------------------------- #
    # ---------------------------------------------------------------- #
    
    def update(self):
        """ Update the entity.
        """
        super().update()  