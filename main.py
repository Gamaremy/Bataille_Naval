from Bateau import Bateau 
from util import Grille 



def main():
    grilleA = Grille()
    print(grilleA)
    test=Bateau(1,1,3,True)
    print(test.est_touche(1,1))
    print(test.get_x())
    print(test.get_y())
    print(test.est_coule())
   
    
if __name__ == '__main__':
   main()
