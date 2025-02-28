from Chevalier import Chevalier
from Dragon import Dragon


class Combat:
    def __init__(self, dragon: Dragon, chevalier: Chevalier):
        self.dragon = dragon
        self.chevalier = chevalier


    def vainqueur(self):
        if self.chevalier.pts_attaque > self.dragon.point_vie:
            return self.chevalier
        else:
            return self.dragon


    def afficher_vainqueur(self):
        return f"Le vainqueur : {self.vainqueur()}"