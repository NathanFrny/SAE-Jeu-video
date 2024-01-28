# TODO - Faire en sorte de faire des abstraction des DataTile pour chaque Tile déjà défini
# Permettra d'implémenter des biomes pour chaque tiles plus facilement
# Permettra à la strategy de configuration de pouvoir utiliser n'importe quel DataTile sans se soucier de son biome

# TODO - Implémenter les différentes entities concrètes
# Faire en sorte que ces entités soit initialisées (à l'aide de leur SpriteRenderer) dans le jeu (à part des gameboard -> utiliser les pygame.sprite.Group() / pygame.sprite.Sprite

# TODO - Implémenter un MovementManager qui gère les déplacements des entités (abstract)
# Faire un PlayerMovementManager qui hérite de MovementManager et qui gère les déplacements des joueurs
# Faire un EnemyMovementManager qui hérite de MovementManager et qui gère les déplacements des ennemis (abstract ?)