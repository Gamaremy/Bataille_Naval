# Réalisation d'un jeu bataille naval avec Wiam 

# Taches réalisé à la séance 1 du projet
Travail commun sur le fichier Bateau_Classe.py
Les taches de chacun seront pour l'instant : 

- Wiam:
    + 1 est_touche 
    + 2 get_touche 
    + 3 get_horizontal 
    + 4 get_taille 

- Jérémy:
    + 1 éléments*
    + 2 get_y 
    + 3 get_x 
    + 4 est_coule
 
# Taches Seance 2 

Realisé lors de la rewiev de Ludi //La classe bateau permet de créer un bateau d'une certaine taille, avec des index de positions.
Dans le main() on créera directement les grille 10x10 finalement avec 2 grille une par joueur//

Il nous faut 4 grille 2/joueur
    Une grille de nos bateau 
    Une grille de nos attaque (touché) image de la grille du joueur inverse

  

  
- Wiam :
    + Pour la  grille1 du joueur_n Si bateau transformer 0 en 1 
    + Pour la  grille2 du joueur_n
        - Si touche dans l'eau 0 en +
        - Si touche bateau transforme le 0 en X
    + Fonction avancée()
      
- Jérémy:
    +  Lanceur de jeu
    +  Fonction jeu_terminé()
    +  Le joueur devra entrez les coordonnées et horizon pour chaque bateau exemple d'affichage
          -> Ou souhaitez vous placer le bateau de taille 5 (x1,y1)
          User entre x1,y1
            Voulez vous le placer horizontalement (H) ou verticalement (V) ?
