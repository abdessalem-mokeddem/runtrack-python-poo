import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changer_Rayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def afficher_Infos(self):
        print("Le rayon", self.rayon)
    
    def circonference_cercle(self):
        return 2 * math.pi * self.rayon
    
    def aire(self):
        return math.pi * self.rayon ** 2
    
    def diametre_cercle(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)


cercle1.afficher_Infos()
print("Circonférence du cercle:", cercle1.circonference_cercle())
print("Aire :", cercle1.aire())
print("Diamètre du cercle :", cercle1.diametre_cercle())

cercle2.afficher_Infos()
print("Circonférence du cercle :", cercle2.circonference_cercle())
print("Aire du cercle:", cercle2.aire())
print("Diamètre du cercle :", cercle2.diametre_cercle())
