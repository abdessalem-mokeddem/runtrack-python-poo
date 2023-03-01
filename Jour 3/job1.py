class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def get_population(self):
        return self.__population

    def ajouter_population(self):
        self.__population += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self):
        self.__ville.ajouter_population()


paris = Ville("Paris", 1000000)


print("Nombre d'habitants à Paris :", paris.get_population())

marseille = Ville("Marseille", 861635)


print("Nombre d'habitants à Marseille :", marseille.get_population())


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

print("Nombre d'habitants de Paris après l'arrivée de John et Myrtille :", paris.get_population())
print("Nombre d'habitants de Marseille après l'arrivée de Chloé :", marseille.get_population())

