class Chevalier:
    def __init__(self, nom : str, armes : str, pts_vie : int, pts_attaque : int, protection : str = "bouclier"):
        self.nom = nom
        self.armes = armes
        self.pts_vie = pts_vie
        self.pts_attaque = pts_attaque
        self.protection = protection
