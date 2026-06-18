init -5 python:
    import random
    from spe import dec_vauban
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import syagrius
    from chapitres.classes import vauban

    def AjouterEvts8Summum():
        global selecteur_
        
        dateNbJours = 1691 * 365 + 1 # ------------------------------------------------- 1691
        debut_chapitre8 = dec_vauban.DecVaubanU(proba.Proba(0.4, False), "debut_chapitre8", dateNbJours)
        selecteur_.ajouterDeclencheur(debut_chapitre8)

label debut_chapitre8:
    "A FAIRE : début chapitre8"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 8)
    jump fin_cycle
