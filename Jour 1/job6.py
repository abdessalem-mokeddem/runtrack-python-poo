class Animal:
    def __init__(self):
        self.age_annimal = 0
        self.nom_annimal = ""

    def vieux(self):
        self.age += 1

    def nommage(self, nom):
        self.nom = nom

mon_animal = Animal()
print("L'âge de mon animal est de :", mon_animal.age)


mon_animal.vieillir()
print("L'âge de mon animal est de :", mon_animal.age)


mon_animal.nommer("Félix")
print("Le nom de mon animal est :", mon_animal.nom)
