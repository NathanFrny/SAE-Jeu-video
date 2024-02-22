from entities import Entity
from components import TransformComponent, SpriteRendererComponent, ActionPointComponent
from utils.PyFunc import distance_calcul

class Action(Entity):
    
    def __init__(self, name: str, image_path: str):
        super().__init__()
        
        self.add_component(TransformComponent([-100, -100], self))
        self.add_component(SpriteRendererComponent(image_path, self))
        self._name = name
        
    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name
        
    # ------------------------------------------------------------------------------- #
    # ---------------------------------- Methods ------------------------------------ #
    # ------------------------------------------------------------------------------- #
    
    def update(self):
        """ Update the entity.
        """
        super().update()
        
    def on_click(self, entity: Entity):
        """ Method called when the action is clicked.
        """
        match (self.name):
            case "Move":
                entity_position = entity.get_component(TransformComponent).position
                action_used = distance_calcul(entity_position, self.get_component(TransformComponent).position)
                entity.get_component(ActionPointComponent).use_action_point(int(action_used))
                entity.get_component(TransformComponent).position = self.get_component(TransformComponent).position
            case "Attack":
                print("Attack")
            case "Lever":
                print("Lever")
            case "Item":
                print("Item")
            case _:
                print("Action not implemented yet")
            
