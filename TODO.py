# TODO - Faire en sorte de faire des abstraction des DataTile pour chaque Tile déjà défini
# Permettra d'implémenter des biomes pour chaque tiles plus facilement
# Permettra à la strategy de configuration de pouvoir utiliser n'importe quel DataTile sans se soucier de son biome

# TODO - Implémenter les différentes entities concrètes
# Faire en sorte que ces entités soit initialisées (à l'aide de leur SpriteRenderer) dans le jeu (à part des gameboard -> utiliser les pygame.sprite.Group() / pygame.sprite.Sprite

# FIXME - Voir Pourquoi il dans BasicRoomStrategy et dans set_players() je suis obligé d'inverser le tuple de position pour que le player se positionne correctement