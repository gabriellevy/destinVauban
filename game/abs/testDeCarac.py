import random

class TestDeCarac:
    """
    Classe modélisant un unique test de carac que le joueur doit effectuer

    self.caracs_ : caracs du test. Par exemple le niveau en métier ou en traits.
    Peut être une string ou un tableau de string

    self.difficulte_ : difficulté du test

    Difficulté va de -50 à +60 :
    -50 : impossible
    -30 très difficile
    -20 : 
    -10 : 
    0 : 
    20 : banale
    40 : facile
    60 : très facile
    la valeur de carac va de -20 à 16
    """

    def __init__(self, caracs, difficulte, situation):
        self.caracs_ = caracs
        self.difficulte_ = difficulte
        self.affichage_ = self.Affichage(situation) # cet affichage est stocké pour permettre l'affichage plus facile dans les balises [] de renpy

    def Affichage(self, situation):
        affichageCarac = self.caracs_
        if isinstance(self.caracs_, list):
            affichageCarac = ""
            for carac in self.caracs_:
                if affichageCarac == "":
                    affichageCarac = "{}".format(carac)
                else:
                    affichageCarac = "{}, {}".format(affichageCarac, carac)

        pourcentageReussite = self.CalculerPourcentageReussite(situation)
        if pourcentageReussite <= 0:
            return u" - Réussite impossible, {} trop bas".format(affichageCarac)
        return " ({}% en {})".format(pourcentageReussite, affichageCarac)

    def CalculerPourcentageReussite(self, situation):
        """
        retourne le pourcentage de change que l'action réussisse étant donné la valeur de la carac donnée chez le joueur
        et la difficulté de la tâche à accomplir
        """

        valCarac = 0
        # c'est possible que le test se fasse sur un tableau de caracs au lieu d'une seule, dans ce cas cas on fait la moyenne entre elles
        if isinstance(self.caracs_, list):
            for carac in self.caracs_:
                val = situation.GetValCaracInt(carac)
                valCarac = valCarac + val
            valCarac = valCarac / len(carac)
        else:
            valCarac = situation.GetValCaracInt(self.caracs_)
        print("valCarac : {} ".format(valCarac)) # tmp test
        print("self.difficulte_ : {}".format(self.difficulte_)) # tmp test

        seuil = self.difficulte_ + valCarac
        
        if seuil < 1:
            return 0
        if seuil > 100:
            return 100
        
        return seuil

    def TesterDifficulte(self, situation):
        """
        retourne True si le joueur réussit la tâche de difficulté demandée avec sa valeur en carac idCarac
        False sinon
        """
        return random.randint(1,100) <= self.CalculerPourcentageReussite(situation)

    def TesterDegreReussite(self, situation):
        """
        retourne un chiffre entre -5 et 5 qui est une note de réussite d'un test de difficulté demandée avec sa valeur en carac idCarac
        -4 échec catastrophique
        0 échec passable
        1 réussite médiocre
        5 réussite exceptionnelle
        """
        scorePourcent = random.randint(0,100)
        pourcentageReussi = self.CalculerPourcentageReussite(situation)
        degreReussite = 1
        if scorePourcent <= pourcentageReussi:
            # réussite
            degreReussite = ( pourcentageReussi - scorePourcent )/20 + 1
        else:
            # échec
            degreReussite = ( pourcentageReussi - scorePourcent )/15

        return degreReussite
