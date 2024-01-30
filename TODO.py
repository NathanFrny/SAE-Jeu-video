# TODO - Faire en sorte de faire des abstraction des DataTile pour chaque Tile déjà défini
# Permettra d'implémenter des biomes pour chaque tiles plus facilement
# Permettra à la strategy de configuration de pouvoir utiliser n'importe quel DataTile sans se soucier de son biome

# TODO - Implémenter les différentes entities concrètes
# Faire en sorte que ces entités soit initialisées (à l'aide de leur SpriteRenderer) dans le jeu (à part des gameboard -> utiliser les pygame.sprite.Group() / pygame.sprite.Sprite




################################################################ Sauvegarde du Jeu ####################################################################################
# TODO - Faire un système de sauvegarde qui permet dans un premier temps de sauvegarder la configuration du jeu (gameboard, players, etc...)
# Faire un fichier test permettant de charger une partie à partir d'un json contenant la sauvegarde d'une partie
# Sauvegarder les components et leurs attributs pour chaque entités
# Sauvegarder l'attribut grid du plateau (pour chaque tiles) afin de pouvoir le reconstruire

# Pour sauvegarder (Pour chaque étape référez-vous à ce qui a déjà été codé dans les fichiers (normalement rien de nouveau))
# Fichier InputManager -> Ajouter un Input sur une touche quelconque qui return "save"
# Fichier GameManager -> Détection de l'input "save" -> méthode save_game()
##################### -> Pour chaque joueur, sauvegarder les attributs de chaque components (cf. le dossier components)
##################### -> Sauvegarder le gameboard (cf. le dossier gameboard) (Gameboard contient les Grid / GraphicGameboard permet d'afficher / GameboardAdapter permet des intéractions entre les deux)
#####################################################################################################################################################################