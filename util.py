class Grille:
    def __init__(self):
        self.grillexy = [[0] * 10 for _ in range(9)]

    def __str__(self):
        s = "";
        for i in self.grillexy :
            s += "|"
            for j in i :
                s +=" " + str(j) +" "
            s+="| \n"
        return s