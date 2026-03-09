class Voiture:
    def __init__(self,marque,matricule,couleur):
        self.marque = marque
        self.matricule = matricule
        self.couleur = couleur
    def afficheriInformations(self):
        print(self.marque,self.matricule,self.couleur)
class Parc:
    def __init__(self,identifiant,adresse,capacite):
        self.identifiant = identifiant
        self.adresse = adresse
        self.capacite = capacite
        self.liste = []

