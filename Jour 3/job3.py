class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "Terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(f"{tache.titre} : {tache.description} ({tache.statut})")

    def filterListe(self, statut):
        return [tache for tache in self.taches 
    if tache.statut == statut]
