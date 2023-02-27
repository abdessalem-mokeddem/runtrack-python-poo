class Point:


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont ({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"Coordonné est {self.x}")
    
    def afficherY(self):
        print(f"La coordonné est {self.y}")
    
    def changerX(self, nouveau_x):
        self.x = nouveau_x
    
    def changerY(self, nouveau_y):
        self.y = nouveau_y
