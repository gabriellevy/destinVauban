init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import germains
    from chapitres.classes import vauban

    def AjouterEvts7RuptureEcriture():
        global selecteur_
        dateNbJours = 1688 * 365 # ------------------------------------------------- 1688
        debut_chapitre7 = declencheur.DeclencheurDate(dateNbJours, "debut_chapitre7")
        selecteur_.ajouterDeclencheur(debut_chapitre7)

label debut_chapitre7:
    "A FAIRE debut_chapitre7"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 7)
    jump fin_cycle
