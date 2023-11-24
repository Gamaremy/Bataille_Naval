class Bateau:
    def __init__(self, x=0,y=0,taille=1,horizontal=True):
        # check attributs correct type
        if type(x) != int or type(y) != int or type(taille) != int or type(horizontal) != bool:
            raise Exception("Mauvais type de données")
        if x > 10 or y > 10 :
            raise Exception("En dehors de la grille")
        if horizontal==True and x+taille > 10 or  horizontal==False and y+taille > 10 :
            raise Exception("En dehors de la grille")
        self.x = x
        self.y = y
        self.taille = taille
        self.horizontal = horizontal
        self.touche = 0
        # liste en intension de booléen de la taille du bateau
        self.nbTouche=[False for i in range(taille)]

    def grille(self):
        self.grillexy = [[0] * 10 for _ in range(9)]
        return(self.grillexy)

    def print_grille(self):
        for i in self.grillexy :
            print("|",end="")
            for j in i :
                print(" ",j," ", end="")
            print("|")
        
    def est_touche(self, x, y):
       if self.horizontal:
           for i in range(self.taille):
               if self.x + i == x and self.y == y:
                  return True
       else:
           for i in range(self.taille):
               if self.x == x and self.y + i == y:
                  self.get_touche(i)
                  return True
       return False

    def get_touche(self, index):
        self.nbTouche[index] = True
        self.touche += 1
        return "touché" if self.est_coule == False else "coulé"

    def get_x(self):
        return(self.x)
      
    def get_y(self):
        return(self.y)

    def est_coule(self):
        for b in self.nbTouche :
            if not b :  # if b == False
                return False
        return True

    def get_taille(self) :
        return self.taille

    def get_horizontal(self):
        return self.horizontal
    

