from Bateau import Bateau 
from util import Grille 



def main():
    grilleA = Grille()
    #print(grilleA)
    test=Bateau(1,1,3,True)
    #print(test.est_touche(1,1))
    #print(test.get_x())
    #print(test.get_y())
    #print(test.est_coule())
    batjoueur1=[]
    batjoueur2=[]
    for i in range(0,5):
        print(i)
    # Nous avons un bateau de taille 2, 2 de taille 3 et 1 de 4 et 1 de 5 
    # Boucle pour le joueur 1
    for i in range(0,5):
        print("Joueur 1 a vous de paramètre votre plateau ! ")
        if i == 0 or i == 1: 
            print("Plaçons les bateaux de taille 2 ")
           
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur1.append(Bateau(x,y,2,Horizon_ou_Verti))

        if i == 2 : 
            print("Plaçons le bateau de taille 3 ")
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur1.append(Bateau(x,y,3,Horizon_ou_Verti))

        if i == 3 : 
            print("Plaçons le bateau de taille 4 ")
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur1.append(Bateau(x,y,4,Horizon_ou_Verti))

        if i == 4 : 
            print("Plaçons les bateau de taille 5 ")
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur1.append(Bateau(x,y,5,Horizon_ou_Verti))
            
    for i in range(0,5):
        print("Maintenant au tour du Joueur 2 a vous de paramètre votre plateau ! ")
        if i == 0 or i == 1: 
            print("Plaçons les bateaux de taille 2 ")
           
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur2.append(Bateau(x,y,2,Horizon_ou_Verti))

        if i == 2 : 
            print("Plaçons le bateau de taille 3 ")
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur2.append(Bateau(x,y,3,Horizon_ou_Verti))

        if i == 3 : 
            print("Plaçons le bateau de taille 4 ")
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur2.append(Bateau(x,y,4,Horizon_ou_Verti))

        if i == 4 : 
            print("Plaçons les bateau de taille 5 ")
            Horizon_ou_Verti = input("Voulez vous le mettre Horizontalement ou Verticalement ? (H/V) ?" )
            x,y = map(int,(input("Entrez les coordonnées X Y  de votre bateau  ? (x,y) ?" )).split(','))
            if Horizon_ou_Verti=="H":
                Horizon_ou_Verti=True
            else:
                Horizon_ou_Verti=False  
            batjoueur2.append(Bateau(x,y,5,Horizon_ou_Verti))
            
  

   
            

        
        
   
    
if __name__ == '__main__':
   main()
