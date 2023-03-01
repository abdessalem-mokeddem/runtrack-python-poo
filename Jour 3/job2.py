class CompteBanquaire:

    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.numero}")
        print(f"Nom du client: {self.nom}")
        print(f"Prénom du client: {self.prenom}")
        print(f"Solde : {self.solde}")

    def afficher_Solde(self):
        print(f"Votre solde est de: {self.solde}")

    def versement(self, montant):
        self.solde += montant
        print(f"{montant} argent ajouté.")
        self.afficher_Solde()

    def retrait(self, montant):
        if self.solde - montant < 0 and not self.decouvert:
            print("Solde insuffisant.")
        else:
            self.solde -= montant
            print(f"{montant} euros ont été retirés du compte.")
            self.afficher_Solde()
            if self.solde < 0:
                self.agios()

    def agios(self):
        print("Ajout.")
        self.solde *= 1.05
        self.afficher_Solde()

    def virement(self, compte_destinataire, montant):
        if self.solde - montant < 0 and not self.decouvert:
            print("Solde insuffisant.")
        else:
            self.solde -= montant
            compte_destinataire.versement(montant)
            self.afficher_Solde()
            compte_destinataire.afficher_Solde()
    
