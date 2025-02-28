class Dragon:
    def __init__(self, type_dragon:str, point_vie:int, point_attaque:int):
        self.type_dragon = type_dragon
        self.point_vie = point_vie
        self.point_attaque = point_attaque
        self.attaques = []


    def __str__(self):
        return f"Type de dragon: {self.type_dragon}\nPoints de vie: {self.point_vie}\nPoints d'attaque{self.point_attaque}"