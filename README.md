# SAE-Jeu-de-Plateau

Auteur : Nathan Fourny  
Développement : Nathan Fourny  
Graphisme : Nathan Fourny  
Musique : Waterflame - Glorious Morning 2  

[Lien vers vidéo de présentation](https://www.youtube.com/watch?v=W2thb5c7FjI)

## Réalisation

Le jeu Escape The Dungeons a été réalisé entièrement en python grâce au module pygame principalement.  
Les graphismes du jeu ont été réalisés entièrement par mes soins à l'aide du logiciel Asperite et de Photoshop.  

Ce travail a été réalisé dans le cadre de la SAE jeu pendant mon troisième semestre de BUT informatique à l'IUT du Littoral Côte d'Opale à Calais.

[Retrouvez ici la musique utilisée pour le jeu](https://www.youtube.com/watch?v=yolbGaJD4AY)

*Toutes les fonctions contiennent des docstring et l'entièreté du jeu a été codé suivant la langue anglaise.*

## Utilisation

Pour lancer le jeu vous devez télécharger le projet. Ensuite il vous faudra vous placer dans le répertoire contenant le fichier main.py et lancer le script via vscode  
ou à l'aide de la commande suivante

```python
python main.py
```

**Remarque : Assurez-vous de bien vous situer dans le répertoire contenant le fichier main.py lorsque vous voulez le lancer**

## Présentation

Escape the Dungeons est un jeu de plateau coopératif en tour par tour. 4 joueurs sont placés sur un plateau de jeu et ils doivent activer 4 leviers pour pouvoir sortir de la salle.  
Le jeu ne se termine que lorsque les 4 joueurs sont morts (Ou quand le joueur n'a plus envie de jouer évidemment).  
  
Pour l'instant le jeu ne possède qu'un mode solo (le joueur contrôlant les 4 personnages). Ils doient réussir à établir une startégie pour éviter de perdre.  
  
**Les features du jeu :**

* **Le joueur possède 3 points d'actions par tour (pouvant varié suivant le déroulement du jeu)**

    Chaque action suivante coûte un point d'action :

    * Se déplacer
    * Attaquer
    * Utiliser un item
    * Activer un levier

* **Il existe 3 items de le jeu**

    * Les pommes

    Permette au joueur de regagner de la vie

    * Les runes

    Permette au joueur d'infliger plus de dégât

    * Les plumes

    Accordent 2 points d'actions bonus au joueur

* **Il existe des plusieurs types de cases**!SECTION

    * Les murs

    Infranchissable par le joueur sauf si un golem vient à le détruire

    * L'eau

    Si le joueur s'y arrête son tour se termine, lorsqu'il commence son tour sur une case d'eau il n'a que 2 points d'action pour le tour

    * Les pièges

    Si le joueur s'y arrête il subit 10 points de dégâts

    * Les téléporteurs

    Il y a 2 par salle, en prendre vous téléporte à l'autre et arrête votre tour

    * Les marchés

    Si un joueur va sur un marché avec suffisament de pièces, il obtient un item aléatoire qui va dans son inventaire (Les joueurs peuvent alors l'utiliser quand ils le veulent)

* **Il existe 4 type d'ennemis**

    * Les slimes

    Se déplace de 2 cases par 2 cases à l'horizontal ou la vertical  
    Peuvent sauter au dessus des murs

    * Les squelettes

    Une réplique des joueurs possèdent moins de point de vie (et moins de peau aussi)

    * Les Chauves-Souris

    N'ont pas beaucoup de point de vie mais peuvent survoler les murs

    * Les Golem

    Très lent mais beaucoup de point de vie et sont capable de détruire les murs (Les joueurs peuvent se déplacer sur un mur détruit)

* **Chaque ennemies tuées accordent un taux différents de pièces gagné au joueur**

* **Les salles sont toutes générées aléatoirement (Suivant quelque règle tout de même)**

