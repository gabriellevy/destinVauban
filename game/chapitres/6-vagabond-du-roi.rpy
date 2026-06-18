init -5 python:
    import random
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
    from spe import dec_vauban

    def AjouterEvtVagabondDuRoi():
        global selecteur_
        
        dateNbJours = 1684 * 365 + 1 # ------------------------------------------------- 1684
        debut_chapitre6 = dec_vauban.DecVaubanU(proba.Proba(0.8, False), "debut_chapitre6", dateNbJours)
        selecteur_.ajouterDeclencheur(debut_chapitre6)

label debut_chapitre6:
    "A FAIRE : début chapitre6"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 6)
    jump fin_cycle

