from .abstract.Monster import Monster
from utils.PyFunc import distance_calcul
from components import TransformComponent, ActionPointComponent
from components.monstersComponents.SkeletonComponent import SkeletonComponent

class Skeleton(Monster):
    def __init__(self, name: str, image_path: str, health: int, action_point: int, damages: int):
        super().__init__(image_path, health, action_point, damages)
        self.add_component(SkeletonComponent(self))
        self._name = name
        
    # ---------------------------------------------------------------- #
    # ------------------------ Methods ------------------------------- #
    # ---------------------------------------------------------------- #
    
    def update(self):
        """ Update the entity.
        """
        super().update()   

    def move(self, target):
        """ Move the entity to the target position.
        
        Args:
            target (list[int, int]): The target position
        """
        action_used = distance_calcul(target, self.get_component(TransformComponent).position)
        self.get_component(ActionPointComponent).use_action_point(int(action_used))
        self.get_component(TransformComponent).position = target

    def __str__(self) -> str:
        """ Display the name of the entity on the console and all his component.

        Returns:
           str : The name of the entity
        """
        components_str = ', '.join(str(component) for component in self._components)
        return f'{self._name} ({components_str})'