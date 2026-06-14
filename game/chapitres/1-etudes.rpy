
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
    scene bg priere
    with dissolve
    show screen valeurs_traits
    "En tant qu'enfant de la noblesse il est indispensable que vous fassiez des études secondaires."
    "Vous les commencez au collège de Semur parmi d'autres fils de nobles et officiers. Plus aussi quelques fils de marchands, laboureurs et artisans aisés. "
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 1)

    # avènement
    "Vous avez à peine 15 ans mais êtes déjà un adulte digne d'être roi. Vous portez fièrement vos cheveux longs, symbole de votre origine divine."
    "Vous recevez la lance sacrée de votre père, symbole de votre autorité et de votre force. Vous devenez ainsi une vivante figure de Wotan, père et roi des Dieux."
    "Puis vos guerriers vous hissent sur le grand pavois du chef."
    # royaume de Vauban à son avènement
    $ AfficherCarteActuelle()
    with dissolve
    "Votre prestige est grand car votre père a été un grand roi invaincu à la guerre et fidèle à l'empire romain. Mais vous n'êtes que le roi des francs saliens de Tournai."
    "Et même si vos guerriers sont redoutables ils ne sont que quelques milliers ce qui est bien peu."
    "Cependant l'empire romain est en ruines, plein de peuples riches qui ne savent pas se battre. C'est la situation idéale pour qui saura saisir les opportunités."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Roi.NOM)
    jump fin_cycle
