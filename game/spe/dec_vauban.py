from abs import declencheur
from abs.univers import temps
from abs import proba
from abs import modifProba
from abs import condition

class DecVauban(declencheur.Declencheur):

    # dateMin en jours
    def __init__(self, aproba, labelGoTo, dateMin):
        """
        cette version du délencheur inclut 1 paramètre utile en mode "historique" :
         - une date minimum de déclenchement
        """
        declencheur.Declencheur.__init__(self, aproba, labelGoTo)
        self.selecteur_ = None # référence vers le sélecteur qui contient ce déclencheur

        conditionDate = condition.Condition(temps.Date.DATE, dateMin, condition.Condition.SUPERIEUR_EGAL)
        self.AjouterCondition(conditionDate)
