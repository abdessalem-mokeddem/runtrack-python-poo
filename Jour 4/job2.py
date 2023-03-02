
class Professeur (Eleve):

    def __init__(self , Professeur , Eleve ,):

        self.__Eleve = Eleve                
        self.__Professeur = Professeur
        

        eleve1 = Eleve()
        eleve1.bonjour() 
        eleve1.allerEnCours() 
        eleve1.modifierAge(15)

prof1 = Professeur("Maths")
prof1.modifierAge(40)
prof1.bonjour() 
prof1.enseigner() 
