from Bateau import Bateau 



def main():
    test=Bateau(1,1,3,True)
    grille=test.grille()
    print(grille)
    print(test.est_touche(1,1))
    print(test.get_touche())
    print(test.get_x())
    print(test.get_y())
    print(test.element())
    print(test.est_coule())
   
    
if __name__ == '__main__':
   main()
