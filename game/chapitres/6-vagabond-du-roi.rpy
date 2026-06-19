init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite.trait import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import syagrius
    from chapitres.classes import vauban
    from spe import dec_vauban

    def AjouterEvtVagabondDuRoi():
        global selecteur_
        
        dateNbJours = 1678 * 365 + 1 # ------------------------------------------------- 1678
        debut_chapitre6 = dec_vauban.DecVaubanU(proba.Proba(0.8, False), "debut_chapitre6", dateNbJours)
        selecteur_.ajouterDeclencheur(debut_chapitre6)
        
        dateNbJours = 1679 * 365 + 1 # ------------------------------------------------- 1679
        seigneur_bazoches = dec_vauban.DecVaubanU(proba.Proba(0.2, False), "seigneur_bazoches", dateNbJours)
        selecteur_.ajouterDeclencheur(seigneur_bazoches)
        
        dateNbJours = 1685 * 365 + 1 # ------------------------------------------------- 1685
        boileau_sur_grade = dec_vauban.DecVaubanU(proba.Proba(0.2, True), "boileau_sur_grade", dateNbJours)
        selecteur_.ajouterDeclencheur(boileau_sur_grade)

label seigneur_bazoches:
    # A FAIRE ? ajouter un choix ? Prix etc ?
    scene bg bazoches
    with dissolve
    "Après de longues négociations vous décidez d'acheter enfin la seigneurie de Bazoches, entre votre village natal et votre manoir d'Épiry."
    "Vous avez maintenant 130 hectares de terre et un très ancien château ayant appartenu à des familles prestigieuses."
    "Voilà qui va accroître votre prestige à la cour."
    $ AjouterACarac(vauban.Vauban.C_FAVEUR_ROI, 1)
    $ SetValCaracInt(vauban.Vauban.C_SEIGNEUR_BAZOCHES, 1)
    jump fin_cycle

label boileau_sur_grade:
    scene bg honneur
    with dissolve
    "Votre ami Boileau fait savoir à tout le monde qu'il est indigne que vous ne soyez pas gradé à votre juste valeur."
    boileau "Je crois qu'il y a plus d'un maréchal de France qui, quand il rencontre Vauban, rougit de se voir maréchal de France."
    "Mais rien ne vient ! Votre naissance trop peu brillante cache votre mérite."
    jump fin_cycle

label debut_chapitre6:
    "A FAIRE : début chapitre6"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 6)
    jump fin_cycle
