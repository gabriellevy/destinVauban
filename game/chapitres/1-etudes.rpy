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
    mathematiques0 = condition.Condition(trait.Mathematiques.NOM, 0, condition.Condition.EGAL)
    fortification0 = condition.Condition(trait.Fortification.NOM, 0, condition.Condition.EGAL)
    hydraulique0 = condition.Condition(trait.Hydraulique.NOM, 0, condition.Condition.EGAL)

    def AjouterEvtEtudes():
        global selecteur_
        dateNbJours = 1646 * 365 + 1 # 13 ans
        debut_des_etudes = dec_vauban.DecVaubanU(proba.Proba(0.4, False), "debut_des_etudes", dateNbJours)
        debut_des_etudes.AjouterCondition(estPasEtudiant)
        selecteur_.ajouterDeclencheur(debut_des_etudes)

        # ------------- apprentissage des maîtrises
        apprentissageMathematiques = declencheur.Declencheur(proba.Proba(0.1), "apprentissageMathematiques")
        apprentissageMathematiques.AjouterCondition(estEtudiant)
        apprentissageMathematiques.AjouterCondition(mathematiques0)
        selecteur_.ajouterDeclencheur(apprentissageMathematiques)
        
        apprentissageFortification = declencheur.Declencheur(proba.Proba(0.1), "apprentissageFortification")
        apprentissageFortification.AjouterCondition(estEtudiant)
        apprentissageFortification.AjouterCondition(fortification0)
        selecteur_.ajouterDeclencheur(apprentissageFortification)
        
        apprentissageHydraulique = declencheur.Declencheur(proba.Proba(0.1), "apprentissageHydraulique")
        apprentissageHydraulique.AjouterCondition(estEtudiant)
        apprentissageHydraulique.AjouterCondition(hydraulique0)
        selecteur_.ajouterDeclencheur(apprentissageHydraulique)

label apprentissageFortification:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "Vos études vous donnent une assez bonne teinture de fortifications."
    $ AjouterACarac(trait.Fortification.NOM, 1)
    jump fin_cycle

label apprentissageMathematiques:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "Vos études vous donnent une assez bonne teinture de mathématiques."
    $ AjouterACarac(trait.Mathematiques.NOM, 1)
    jump fin_cycle

label debut_des_etudes:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "En tant qu'enfant de la noblesse il est indispensable que vous fassiez des études secondaires."
    "Vous les commencez au collège de Semur parmi d'autres fils de nobles et officiers. Plus aussi quelques fils de marchands, laboureurs et artisans aisés. "
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 1)
    jump fin_cycle

label apprentissageHydraulique:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "Vos études vous donnent une assez bonne teinture d'hydraulique."
    $ AjouterACarac(trait.Hydraulique.NOM, 1)
    jump fin_cycle
