from Chevalier import Chevalier
from Combat import Combat
from Dragon import Dragon

chevalier1 = Chevalier("Rémy", "une épée de feu",10, 15, "un bouclier de magie" )
dragon1 = Dragon("dragon de glace", 12, 8)

combat1 = Combat(dragon1, chevalier1)
print(f"le vainqueur est: {Combat.vainqueur(combat1)}")