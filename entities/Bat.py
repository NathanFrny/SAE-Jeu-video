from .abstract.Monster import Monster

class Bat(Monster):
    def __init__(self, name: str, image_path: str, health: int, action_point: int, damages: int):
        super().__init__(image_path, health, action_point, damages)
        self._name = name

    # ---------------------------------------------------------------- #
    # ------------------------ Methods ------------------------------- #
    # ---------------------------------------------------------------- #
    
    def update(self):
        """ Update the entity.
        """
        super().update()  

    def __str__(self) -> str:
        """ Display the name of the entity on the console and all his component.

        Returns:
           str : The name of the entity
        """
        components_str = ', '.join(str(component) for component in self._components)
        return f'{self._name} ({components_str})'