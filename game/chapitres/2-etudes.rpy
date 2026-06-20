init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite.trait import trait
    from abs.humanite.trait import maitrise
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from spe import dec_vauban
    from chapitres.classes import vauban

    estPasEtudiant = condition.Condition(vauban.Vauban.CHAPITRE, 2, condition.Condition.DIFFERENT)
    estEtudiant = condition.Condition(vauban.Vauban.CHAPITRE, 2, condition.Condition.EGAL)
    mathematiques0 = condition.Condition(maitrise.Mathematiques.NOM, 0, condition.Condition.EGAL)
    fortification0 = condition.Condition(maitrise.Fortification.NOM, 0, condition.Condition.EGAL)
    hydraulique0 = condition.Condition(maitrise.Hydraulique.NOM, 0, condition.Condition.EGAL)
    poliorcetique0 = condition.Condition(maitrise.Poliorcetique.NOM, 0, condition.Condition.EGAL)

    def AjouterEvtEtudes():
        global selecteur_
        dateNbJours = 1646 * 365 + 1 # 13 ans ------------------------------------------------- 1646
        debut_des_etudes = declencheur.DeclencheurDate(dateNbJours, "debut_des_etudes")
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
        
        apprentissagePoliorcetique = declencheur.Declencheur(proba.Proba(0.1), "apprentissagePoliorcetique")
        apprentissagePoliorcetique.AjouterCondition(estEtudiant)
        apprentissagePoliorcetique.AjouterCondition(poliorcetique0)
        selecteur_.ajouterDeclencheur(apprentissagePoliorcetique)
        
        apprentissageGeneral = declencheur.Declencheur(proba.Proba(0.1), "apprentissageGeneral")
        apprentissageGeneral.AjouterCondition(estEtudiant)
        selecteur_.ajouterDeclencheur(apprentissageGeneral)

label apprentissageGeneral:
    menu:
        "Vous étudiez..."
        "la rhétorique":
            $ AjouterACarac(trait.Eloquence.NOM, 1)
        "la logique et les raisonnements abstraits":
            $ AjouterACarac(trait.Intelligence.NOM, 1)
        "l'espagnol":
            $ SetValMaitrise(maitrise.Espagnol.NOM, maitrise.TraitMaitrise.MAITRISE_A)
        "la maîtrise des armes":
            $ AjouterACarac(trait.ArmesCorpsACorps.NOM, 1)
            $ AjouterACarac(trait.Tir.NOM, 1)
        
    jump fin_cycle

label apprentissagePoliorcetique:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "Vos études vous donnent une assez bonne teinture de poliorcétique."
    $ SetValMaitrise(maitrise.Poliorcetique.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    jump fin_cycle

label apprentissageFortification:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "Vos études vous donnent une assez bonne teinture de fortifications."
    $ SetValMaitrise(maitrise.Fortification.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    jump fin_cycle

label apprentissageMathematiques:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "Vos études vous donnent une assez bonne teinture de mathématiques."
    $ SetValMaitrise(maitrise.Mathematiques.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    jump fin_cycle

label apprentissageHydraulique:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "Vos études vous donnent une assez bonne teinture d'hydraulique."
    $ SetValMaitrise(maitrise.Hydraulique.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    jump fin_cycle

label debut_des_etudes:
    scene bg priere # A FAIRE Marjolaine : trouver un tableau pour les études XVIIème
    with dissolve
    "En tant qu'enfant de la noblesse il est indispensable que vous fassiez des études secondaires."
    "Vous les commencez au collège de Semur parmi d'autres fils de nobles et officiers. Plus aussi quelques fils de marchands, laboureurs et artisans aisés. "
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 2)
    jump fin_cycle
