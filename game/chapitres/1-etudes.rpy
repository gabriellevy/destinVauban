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
    from spe import dec_vauban
    from chapitres.classes import vauban

    estPasEtudiant = condition.Condition(vauban.Vauban.CHAPITRE, 1, condition.Condition.DIFFERENT)
    estEtudiant = condition.Condition(vauban.Vauban.CHAPITRE, 1, condition.Condition.EGAL)

    def AjouterEvtEtudes():
        global selecteur_
        dateNbJours = 1646 * 365 + 1 # 13 ans
        debut_des_etudes = dec_vauban.DecVaubanU(proba.Proba(0.4, False), "debut_des_etudes", dateNbJours)
        debut_des_etudes.AjouterCondition(estPasEtudiant)
        selecteur_.ajouterDeclencheur(debut_des_etudes)

label debut_des_etudes:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    show screen valeurs_traits
    "En tant qu'enfant de la noblesse il est indispensable que vous fassiez des études secondaires."
    "Vous les commencez au collège de Semur parmi d'autres fils de nobles et officiers. Plus aussi quelques fils de marchands, laboureurs et artisans aisés. "
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 1)
    jump fin_cycle
