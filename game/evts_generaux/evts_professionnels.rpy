init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from abs.humanite import metier

    estPasGuerrierNivEleve = condition.Condition(trait.ArmesCorpsACorps.NOM, trait.Trait.CARAC_ELEVE, condition.Condition.INFERIEUR)
    estPasPolitiqueNivExtreme = condition.Condition(metier.Politique.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.INFERIEUR)
    estPasStrategeNivExtreme = condition.Condition(metier.Stratege.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.INFERIEUR)
    estPasPerceptionNivEleve = condition.Condition(trait.Perception.NOM, trait.Trait.CARAC_ELEVE, condition.Condition.INFERIEUR)
    estPasGrandPretre = condition.Condition(metier.Pretre.NOM, 5, condition.Condition.INFERIEUR)

    auMoinsAdolescent = condition.Condition(vauban.Vauban.CHAPITRE,2, condition.Condition.SUPERIEUR_EGAL)
    auMoinsJeuneAdulte = condition.Condition(vauban.Vauban.CHAPITRE,3, condition.Condition.SUPERIEUR_EGAL)
    
    def AjouterEvtsProfessionnels():
        global selecteur_
        entrainementGuerrier = declencheur.Declencheur(proba.Proba(0.1, True), "entrainementGuerrier")
        entrainementGuerrier.AjouterCondition(estPasGuerrierNivEleve)
        entrainementGuerrier.AjouterCondition(auMoinsAdolescent)
        selecteur_.ajouterDeclencheur(entrainementGuerrier)

label entrainementGuerrier:
    # s'entraîne au combat
    scene bg morvan
    with dissolve
    $ niveauExpertise = situation_.GetValCaracInt("entrainementGuerrierNiv")
    if niveauExpertise == 0:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 1)
        "Il est capital pour un noble de savoir manier l'épée, symbole royal par excellence de votre classe et de votre statut."
    else:
        "Vous vous entrainez au combat."
    $ AjouterACarac(trait.ArmesCorpsACorps.NOM, 4)
    jump fin_cycle
