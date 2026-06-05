
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
    # from geographie import quartier
    from abs.humanite import identite
    from spe import dec_vauban

    equitation0 = condition.Condition(trait.Equitation.NOM, trait.TraitMaitrise.MAITRISE_A, condition.Condition.INFERIEUR)

    def AjouterEvtJeunesse():
        global selecteur_
        apprentissageEquitation = declencheur.Declencheur(proba.Proba(0.4, False), "apprentissageEquitation")
        apprentissageEquitation.AjouterCondition(equitation0)
        selecteur_.ajouterDeclencheur(apprentissageEquitation)

# lieu, époque, enfance au pays
# A FAIRE série d'évts de jeunesse semi aléatoires
label intro:
    scene bg morvan
    with dissolve
    show screen valeurs_traits
    "[situation_.AffichageDate()]"
    "Nous sommes en 1620. Vous êtes le jeune Sébastien Le Prestre."
    "Vous êtes de la petite noblesse des confins bourguignons et nivernais."
    "La région froide et assez montagneuse où vous êtes né s'appelle le Morvan, et c'est un rude pays."
    jump fin_cycle

label apprentissageEquitation:
    scene bg morvan
    "[situation_.AffichageDate()] : Comme tout gentilhomme qui se respecte vous prenez très tôt beaucoup de leçons d'équitation."
    # A FAIRE : test d'adresse pour ne pas le rater ???
    $ SetValCaracInt(trait.Equitation.NOM, trait.TraitMaitrise.MAITRISE_A)
    jump fin_cycle
