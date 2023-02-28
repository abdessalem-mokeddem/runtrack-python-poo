class Student:
    def __init__(self, nom, prenom, etudiant):
        self.nom = nom
        self.prenom = prenom
        self.num_etudiant = etudiant
        self.credits = 0
        self.level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.credits += credits

    
        elif self.credits >= 70:
            return "Bien"
        elif self.credits >= 60:
       

            def student_Info(self):
                print("Nom :", self.nom)
                print("Prénom :", self.prenom)
                print("Identifiant :", self.num_etudiant)
                print("Niveau :", self.level)

john = Student("Doe", "John", 145)


john.add_credits(30)
john.add_credits(40)
john.add_credits(20)

john.student_Info()
