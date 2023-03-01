class Joueur:

    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
        
    def marquer_Un_But(self):
        self.buts_marques += 1
        
    def effectuer_UnePasse_Decisive(self):
        self.passes_decisives += 1
        
    def recevoir_Un_Carton_Jaune(self):
        self.cartons_jaunes += 1
        
    def recevoir_Un_Carton_Rouge(self):
        self.cartons_rouges += 1
        
    def afficher_Statistiques(self):
        print(f"{self.nom} ({self.numero}), {self.position}")
        print(f"{self.buts_marques} buts marqués, {self.passes_decisives} passes décisives")
        print(f"{self.cartons_jaunes} cartons jaunes, {self.cartons_rouges} cartons rouges\n")
        

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
        
    def ajouter_un_Joueur(self, joueur):
        self.joueurs.append(joueur)
        
    def afficher_Statistiques_Joueurs(self):
        print(f"Stats {self.nom}")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
            
    def mettreAJour_Statistiques_Joueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "BUT":
                    joueur.marquerUnBut()
                elif action == "Passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "Jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "Rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Action non valable")
                break
                
    def jouerMatch(self, autre_equipe):
        for joueur in self.joueurs:
            action = input(f"Quelle action rélle {joueur.nom} ({joueur.position}) ? (but/passe/jaune/rouge)")
            self.mettreAJourStatistiquesJoueur(joueur.nom, action)
        
        for joueur in autre_equipe.joueurs:
            action = input(f"Quelle action a réalisé {joueur.nom} ({joueur.position}) ? (but/passe/jaune/rouge)")
            self.mettreAJourStatistiquesJoueur(joueur.nom, action)
            
        print("Fin du match ! Score final ! ")