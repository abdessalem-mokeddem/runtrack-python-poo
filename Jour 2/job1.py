class Rectangle:

    def __init (self , longueur = 10 , largeur = 5):

        self.longueur = longueur 
        self.largeur = largeur

def get_longueur(self):
        return self.__longueur
    
def set_longueur(self, longueur):
        self.__longueur = longueur
        
def get_largeur(self):
        return self.__largeur
    
def set_largeur(self, largeur):
        self.__largeur = largeur
        
mon_rectangle = Rectangle(10, 5)


print("Longueur:", mon_rectangle.get_longueur())
print("Largeur:", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(8)
mon_rectangle.set_largeur(3)

print("Longueur :", mon_rectangle.get_longueur())
print("Largeur ", mon_rectangle.get_largeur())

