class Grille:
    def __init__(self):
        self.grillexy = [[0] * 10 for _ in range(9)]

    def __str__(self):
        s = "";
        # Ajoutez les chiffres de la grille (noms de lignes)
        for i in range(9):
            self.grillexy[i][0] = str(i + 1)
        # Ajoutez les lettres de la grille (noms de colonnes)
        for j in range(10) :
            self.grillexy[0][j] = chr(j + ord('A'))
        # Afficher la grille
        for i in range(9):
            s += "|"
            for j in range (10) :
                s +=" " +  str(self.grillexy[i][j])  +" "
            s+="| \n"
        return s
    def avance(self, x, y, touche_bateau):
        if touche_bateau:
            self.grillexy[x][y] = "X"
        else:
            self.grillexy[x][y] = "+"
