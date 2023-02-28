class Commande:
    
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}
        self.__statut = "en préparation"
    
    def ajouter_plat(self, nom_plat, prix):
        self.__plats[nom_plat] = {"prix": prix, "status": "préparation"}
    
    def annuler_commande(self):
        self.__statut = "annulation"
        for plat in self.__plats:
            self.__plats[plat]["status"] = "annulation"
    
    def __calculer_total(self):
        total = 0
        for plat in self.__plats:
            total += self.__plats[plat]["prix"]
        return total
    
    def afficher_commande(self):
        total = self.__calculer_total()
        print("Numéro de commandes ", self.__num_commande)
        print("Liste des plats : ")
        for plat in self.__plats:
            print(plat, " - ", self.__plats[plat]["prix"], " - ", self.__plats[plat]["status"])
        print("Total à payer : ", total)
    
    def calculer_tva(self, taux):
        total = self.__calculer_total()
        tva = total * taux / 100
        return tva
