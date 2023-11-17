class Bateau:
    def __init__(self, cordonneex=1,cordonneey=1,taille=1,horizontal=True):
        self.cordonneex = int(cordonneex)
        self.cordonneey = int(cordonneey)
        self.taille = int(taille)
        self.horizontal = bool(horizontal)
    def grille(self):
        grillexy = [[0] * 10 for _ in range(9)]
        return(grillexy)
        
        
        


        
