# Comment utiliser "Is my series worth watching?"
## I. Les fichiers
### 1) Le dossier static
Il contient
#### a. Le dossier css
Il contient les fichiers .css qui nous permettent d'éditer le style du site : les couleurs, les formes, la mise en page...
#### b. Le dossier lib
Il contient les libraires externes que nous avons utilisées pour les sites, notamment la librairie fontawesome qui nous permet d'ajouter des icônes
### 2) Le dossier templates
Il contient les fichiers html nous permettant de gérer les éléments qui constituent les pages web:

* Le fichier *homepage.html* contient les données de la page d'accueil.
* Le fichier *index.html* contient les données de la page de résultats.

### 3) Les fichiers .tsv
Ce sont les fichiers qui contiennent les données d'IMDB et dont nous avons besoin :

* Le fichier *title.series.tsv*, que l'on a créé à partir du fichier *title.basics.tsv*, contient les id alphanumériques correspondant à chaque série ainsi que le titre le plus utilisé.
* Le fichier *title.episode.tsv* contient les id alphanumériques correspondant à chaque épisode, l'id alphanumérique de la série dont ils proviennent, la saison dont ils proviennent et leur numéro dans la saison.
* Le fichier *title.ratings.tsv* contient les id alphanumériques correspondant à chaque épisode, la note moyenne qui leur a été attribuée par les utilisateurs ainsi que le nombre de personnes qui ont voté.

### 4) Les fichiers .py
Ce sont les fichiers qui contiennent notre code python.

* Le fichier *functions.py* contient toutes les fonctions nécessaires au programme pour qu'il puisse créer un tableau de données à partir de la série entrée par l'utilisateur.
* Le fichier *main.py* est notre programme principal. Il contient la fonction principale de notre programme qui prend en entrée un nom de série et renvoie une matrice de la forme dont on a besoin.
* Le fichier *hello.py* est celui qui permet de créer une page html où l'on exporte les résultats de notre code et de créer une interface pour l'utilisateur.

### 5) Le fichier requirements.txt
* Il contient la liste des packages nécessaires au fonctionnement du programme.

## II. Comment faire fonctionner le programme?
### 1ère étape :
Après avoir téléchargé tous les fichiers, il faut installer les packages nécessaires à l'aide du fichier requirements.txt. Pour cela, il suffit de taper la commande <'pip install'> dans le terminal.

### 2ème étape :
Ensuite, pour accéder à la page web il suffit de taper la commande <'flask run'> dans le terminal ; puis de cliquer sur lien qui sera affiché dans le terminal après "Running on...".

### 3ème étape :
Pour obtenir les résultats des notes obtenues par une série, il suffit de taper le nom de la série dans la barre de recherche sans se soucier des majuscules ou des caractères spéciaux puis de cliquer sur la loupe.

### 4ème étape :
Aller regarder la série en question if its worth watching, ou bien en choisir une autre.