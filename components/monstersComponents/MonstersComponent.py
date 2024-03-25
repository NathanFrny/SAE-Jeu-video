from components import Component
from abc import ABC

class MonstersComponent(Component, ABC):

    def __init__(self, parent_entity):
        super().__init__(parent_entity)

        self._possible_movements = []
        self._possible_attacks = []

        self._gameboard = []

    # ------------------------------------------------------------------------------- #
    # ------------------------------ Getters & Setters ------------------------------ #
    # ------------------------------------------------------------------------------- #
        
    @property
    def possible_movements(self):
        return self._possible_movements
    @possible_movements.setter
    def possible_movements(self, possible_movement):
        self._possible_movements = possible_movement

    @property
    def possible_attacks(self):
        return self._possible_attacks
    @possible_attacks.setter
    def possible_attacks(self, possible_attacks):
        self._possible_attacks = possible_attacks

    @property
    def gameboard(self):
        return self._gameboard
    @gameboard.setter
    def gameboard(self, gameboard):
        self._gameboard = gameboard

    # ------------------------------------------------------------------------------- #
    # ----------------------------------- Methods ----------------------------------- #
    # ------------------------------------------------------------------------------- #
        
    def update(self):
        # Ajoutez ici le code pour mettre à jour le composant
        pass

    def all_actions(self):
        """ Get the possible movement of the monster
        """
        pass




    