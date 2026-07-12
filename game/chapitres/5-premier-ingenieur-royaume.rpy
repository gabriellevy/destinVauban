init -5 python:
    import random
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import syagrius
    from chapitres.classes import vauban

    avant493 = condition.Condition(temps.Date.DATE_ANNEES, 493, condition.Condition.INFERIEUR)

    def AjouterEvtBurgondes():
        global selecteur_
        
