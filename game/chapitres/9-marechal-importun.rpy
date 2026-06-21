init -5 python:
    import random
    from spe import dec_vauban
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

    def AjouterEvtsMarechalImportun():
        global selecteur_
        
        dateNbJours = 1697 * 365 + 1 # ------------------------------------------------- 1697
        debut_chapitre9 = declencheur.DeclencheurDate(dateNbJours, "debut_chapitre9")
        selecteur_.ajouterDeclencheur(debut_chapitre9)

label debut_chapitre9:
    "A FAIRE : début chapitre9"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 9)
    jump fin_cycle
