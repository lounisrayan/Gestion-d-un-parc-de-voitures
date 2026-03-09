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
    def entrerVoiture(self,voiture):
        if len(self.liste_voitures) < self.capacite:
            self.liste_voitures.append(voiture)
            print("voiture ajoutee au parc.")
        else:
            print("le parc est plein.")
    def sortirVoiture(self,voiture):
        if voiture in self.liste_voitures:
            self.liste_voitures.remove(voiture)
            print("voiture retiree du parc.")
        else:
            print("voiture non trouvee dans le parc.")
    def calculerNbrPlaceslibres(self):
        return self.capacite - len(self.liste_voitures)
parc = Parc(1,"Montreal",3)
voiture = Voiture("Toyota","BB111","Rouge")
voiture = Voiture("Honda","AA222","Bleu")









