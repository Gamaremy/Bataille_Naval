from Bateau import Bateau 



def main():
    test=Bateau(1,1,3,True)
    grille=test.grille()
    print(grille)
    print(test.est_touche(2, 1))


    
if __name__ == '__main__':
	main()
