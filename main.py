from Bateau import Bateau 
from util import Grille 




def main():

    grilleA = Grille()
    grilleB = Grille()
    grilleA.afficher_grille("moi")
    grilleB.afficher_grille("adversaire")
    #Afficher la Grille A
    print("Grille du Joueur 1:")
    print(grilleA)
    #Afficher la Grille B
    print("Grille du Joueur 2:")
    print(grilleB)
    #Supposons que le bateau est touché à la position (1, 2)
    grilleA.avance(1, 2, True)
    grilleB.avance(3, 4, False)


    grilleattaque_joeur1 = Grille()
    grillebateau_joeur1 = Grille()
    grilleattaque_joeur2 = Grille()
    grillebateau_joeur2 = Grille()

 


def creation():
    BateauJoueur={}
    for _ in range(2):
        NomJoueur = input("Entrez votre de pseudo de joueur :" )
        print("\n")
        BateauJoueur[NomJoueur]=[]
        print(f"Joueur {NomJoueur} a vous de paramètrer votre plateau ! ")
        for i in range(0,5):
            print("Bateau numéro :",i+1)
            if i == 0 or i == 1: 
                print("Plaçons les bateaux de taille 2 \n ")
                Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
                x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
                if Horizon_ou_Verti=="H":
                    Horizon_ou_Verti=True
                else:
                    Horizon_ou_Verti=False  
                BateauJoueur[NomJoueur].append(Bateau(x,y,2,Horizon_ou_Verti))

            if i == 2 : 
                print("Plaçons le bateau de taille 3 ")
                Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
                x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
                if Horizon_ou_Verti=="H":
                    Horizon_ou_Verti=True
                else:
                    Horizon_ou_Verti=False  
                BateauJoueur[NomJoueur].append(Bateau(x,y,3,Horizon_ou_Verti))

            if i == 3 : 
                print("Plaçons le bateau de taille 4 ")
                Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
                x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
                if Horizon_ou_Verti=="H":
                    Horizon_ou_Verti=True
                else:
                    Horizon_ou_Verti=False  
                BateauJoueur[NomJoueur].append(Bateau(x,y,4,Horizon_ou_Verti))

            if i == 4 : 
                print("Plaçons les bateau de taille 5 ")
                Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
                x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
                if Horizon_ou_Verti=="H":
                    Horizon_ou_Verti=True
                else:
                    Horizon_ou_Verti=False  
                BateauJoueur[NomJoueur].append(Bateau(x,y,5,Horizon_ou_Verti))
            print("\n")
    return BateauJoueur


        

if __name__ == '__main__':
   main()
   Essai=creation()
   print(Essai)
