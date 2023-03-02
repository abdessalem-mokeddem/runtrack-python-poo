class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficher_Age(self):
        print("Age :", self.age)
        
    def bonjour(self):
        print("Hello")
        
    def modifier_Age(self, age):
        self.age = age
        
        
class Eleve(Personne):
    def aller_En_Cours(self):
        print("Le cours va commencer")
        
    def affichageAge(self):
        print("J'ai", self.age, "ans")
        
        
class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")
