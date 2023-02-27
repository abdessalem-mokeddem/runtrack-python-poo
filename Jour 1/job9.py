class Produit:
    def __init__(self, nom, prix_HT, TVA):
        self.nom = nom
        self.prixHT = prix_HT
        self.TVA = TVA
    
    def calculer_Prix_TTC(self):
        return self.prixHT * (1 + self.TVA/100)
    
    def afficher(self):
        infos = self.Informations()
        for info in infos:
            print(info)
    
    def Nom(self):
        return self.nom
    
    def Nom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def Prix_HT(self):
        return self.prixHT
    
    def Prix_HT(self, nouveau_prix_HT):
        self.prixHT = nouveau_prix_HT
    
    def TVA(self):
        return self.TVA
    
    def TVA(self, nouvelle_TVA):
        self.TVA = nouvelle_TVA
    
    def Informations(self):
        return [
            "Nom : {}".format(self.nom),
            "Prix HT : {}€".format(self.prixHT),
            "TVA : {}%".format(self.TVA),
            "Prix TTC : {}€".format(self.calculer_Prix_TTC())
        ]


produit1 = Produit("Chaise", 20, 20)
produit2 = Produit("Table", 100, 10)

produit1.afficher()
produit2.afficher()

produit1.setNom("Fauteuil")
produit1.setPrixHT(30)

produit2.setNom("Bureau")
produit2.setPrixHT(150)

print("Nouveau prix du", produit1.Nom(), ":", produit1.calculer_Prix_TTC(), "€")
print("Nouveau prix du", produit2.Nom(), ":", produit2.calculer_Prix_TTC(), "€")
