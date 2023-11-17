class Bateau:
    def __init__(self, cordonneex=1,cordonneey=1,taille=1,horizontal=True):
        self.cordonneex = int(cordonneex)
        self.cordonneey = int(cordonneey)
        self.taille = int(taille)
        self.horizontal = bool(horizontal)
        self.boollist_element=self.element()

    def grille(self):
        grillexy = [[0] * 10 for _ in range(9)]
        return(grillexy)
    
    def element(self):
        boollist_element=[False]*self.taille
        return(boollist_element)
    def get_x(self):

        return(self.cordonneex)
      
    def get_y(self):
        return(self.cordonneey)

    def est_coule(self):
        count=0
        for i in range(self.taille):
            if self.boollist_element[i] == True:
                count+=1
        if count==self.taille:
            return(True)
        else:
            return(False)




