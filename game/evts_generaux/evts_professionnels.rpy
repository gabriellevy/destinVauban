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
    
    def AjouterEvtsProfessionnels():
        global selecteur_
        entrainementGuerrier = declencheur.Declencheur(proba.Proba(0.1, True), "entrainementGuerrier")
        entrainementGuerrier.AjouterCondition(estPasGuerrierNivEleve)
        entrainementGuerrier.AjouterCondition(auMoinsAdolescent)
        selecteur_.ajouterDeclencheur(entrainementGuerrier)
        
        entrainementChasse = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementChasse")
        entrainementChasse.AjouterCondition(auMoinsAdolescent)
        entrainementChasse.AjouterCondition(estPasPerceptionNivEleve)
        selecteur_.ajouterDeclencheur(entrainementChasse)

label entrainementChasse:
    # entrainement chasse
    scene bg chasse
    with dissolve
    $ niveauExpertise = situation_.GetValCaracInt("entrainementChasseNiv")
    if niveauExpertise == 0:
        $ situation_.SetValCarac("entrainementChasseNiv", 1)
        "Vous chassez aussi souvent que possible comme tout noble français se doit de le faire."
    elif niveauExpertise == 1:
        $ situation_.SetValCarac("entrainementChasseNiv", 2)
        "Quand ce n'est pas à la guerre que vous menez vos leudes c'est à la chasse. Car la chasse en plus de vous ravitailler en viande et cuir est un bon entrainement à la guerre."
    elif niveauExpertise == 2:
        $ situation_.SetValCarac("entrainementChasseNiv", 3)
        "Aujourd'hui vous avez tué un énorme sanglier à la chasse."
    elif niveauExpertise == 3:
        $ situation_.SetValCarac("entrainementChasseNiv", 4)
        "Aujourd'hui vous avez tué un superbe cerf à la chasse dans la gigantesque forêt des ardennes."
    elif niveauExpertise == 4:
        $ situation_.SetValCarac("entrainementChasseNiv", 5)
        "Aujourd'hui vous avez tué un buffle massif après uen chasse mémorable dans les vosges."
    elif niveauExpertise == 5:
        $ situation_.SetValCarac("entrainementChasseNiv", 6)
        $ nomCourtisan = gaulois_.CreerPrenom(True)
        "Un courtisan nommé [nomCourtisan] venant de l'est des royaumes francs vous a offert un arc remarquable fait de plusieurs matériaux avec des extrémités en os."
        "Il appelle cela un 'arc rélexe' et affirme que c'est l'arc de prédilection des huns et des avars."
        "Il est bien plus puissant que les arcs francs. Vous récompensez chaudement [nomCourtisan] et allez immédiatement vous entraîner pour la prochaine chasse."
        $ AjouterACarac(metier.Guerrier.NOM, 1)
    else:
        "Vous chassez aussi souvent que possible comme tout noble français se doit de le faire."
    $ AjouterACarac(trait.Animaux.NOM, 1)
    $ AjouterACarac(trait.Perception.NOM, 1)
    jump fin_cycle

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
