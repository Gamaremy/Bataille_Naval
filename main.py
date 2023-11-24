from Bateau import Bateau 
from util import Grille 



def main():
    grilleA = Grille()
    grilleB = Grille()
    #Afficher la Grille A
    print("Grille du Joueur 1:")
    print(grilleA)
    #Afficher la Grille B
    print("Grille du Joueur 2:")
    print(grilleB)
     # Supposons que le bateau est touché à la position (1, 2)
    grilleA.avance(1, 2, True)
    grilleB.avance(3, 4, False)

    test = Bateau(1, 1, 3, True)
    print(test.est_touche(1,1))
    print(test.get_x())
    print(test.get_y())
    print(test.est_coule())
   
    
if __name__ == '__main__':
   main()



