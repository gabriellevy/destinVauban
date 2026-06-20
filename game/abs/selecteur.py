import random
from abs.univers import temps
from abs import declencheur

class Selecteur:
    """
    Objet qui contient tous les déclencheurs et le système de sélection selon les proba
    """

    def __init__(self):
        self.declencheurs_ = []
        self.declencheursDate_ = [] # uniquement pour les déclencheurs à date fixe

    def ajouterDeclencheur(self, pdeclencheur):
        if isinstance(pdeclencheur, declencheur.DeclencheurDate):
            self.declencheursDate_.append(pdeclencheur)
        else:
            self.declencheurs_.append(pdeclencheur)
        declencheur.selecteur_ = self

    def determinationEvtDate(self, dateActuelle):
        global erreur_
        for ldeclencheur in self.declencheursDate_:
            if ldeclencheur.date_ == dateActuelle:
                return ldeclencheur.executer(self)
            
        return None


    def determinationEvtCourant(self, situation):
        global erreur_
        probaCompleteRel = 0 # total des probas relatives
        probaCompleteAbs = 0 # total des probas absolues
        probaTmp = 0
        for declencheur in self.declencheurs_:
            proba = declencheur.calculerProba(situation)
            if declencheur.proba_.relative_:
                probaCompleteRel = probaCompleteRel + proba
            else:
                probaCompleteAbs = probaCompleteAbs + proba

        # proba absolues (où le total des proba absolues ne peut pas dépasser 1.0 car une proba de 0.5 est VRAIMENT une proba de 50%
        resProba = random.uniform(0, 1.0)
        if resProba <= probaCompleteAbs:
            #if probaCompleteAbs > 1.0: # sécurité désactivée temporairement pour tester -> le mieux serait de gérer les dates proprement
            #    return "probaAbsoluesSup100"
            for declencheur in self.declencheurs_:
                if not declencheur.proba_.relative_:
                    proba = declencheur.calculerProba(situation)
                    if proba > 0:
                        probaTmp = probaTmp + proba
                        if resProba <= probaTmp:
                            return declencheur.executer(self)

        # si pas de proba absolue validée, on passe aux relatives :
        # probas relatives
        resProba = random.uniform(0, probaCompleteRel)

        # déterminer évt final
        for declencheur in self.declencheurs_:
            if declencheur.proba_.relative_:
                proba = declencheur.calculerProba(situation)
                if proba > 0:
                    probaTmp = probaTmp + proba
                    if resProba <= probaTmp:
                        return declencheur.executer(self)

        return "pas_evt_trouve"
