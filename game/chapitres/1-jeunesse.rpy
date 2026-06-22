init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from game.abs.humanite.trait import maitrise
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from spe import dec_vauban
    from chapitres.classes import vauban

    equitation0 = condition.Condition(maitrise.Equitation.NOM, maitrise.TraitMaitrise.MAITRISE_A, condition.Condition.INFERIEUR)
    hydraulique0Enfance = condition.Condition(maitrise.Hydraulique.NOM, maitrise.TraitMaitrise.MAITRISE_A, condition.Condition.INFERIEUR)
    chapitre1 = condition.Condition(vauban.Vauban.CHAPITRE, 1, condition.Condition.EGAL)
    en_hiver = condition.Condition(temps.Date.SAISON, temps.Date.HIVER, condition.Condition.EGAL)

    def AjouterEvtJeunesse():
        global selecteur_
        apprentissageEquitation = declencheur.Declencheur(proba.Proba(0.2), "apprentissageEquitation")
        apprentissageEquitation.AjouterCondition(equitation0)
        selecteur_.ajouterDeclencheur(apprentissageEquitation)

        apprentissageHydrauliqueEnfance = declencheur.Declencheur(proba.Proba(0.05), "apprentissageHydrauliqueEnfance")
        apprentissageHydrauliqueEnfance.AjouterCondition(hydraulique0Enfance)
        selecteur_.ajouterDeclencheur(apprentissageHydrauliqueEnfance)

        apprentissageEnfance = declencheur.Declencheur(proba.Proba(0.05), "apprentissageEnfance")
        apprentissageEnfance.AjouterCondition(chapitre1)
        selecteur_.ajouterDeclencheur(apprentissageEnfance)
        
        endurcissementEnfance = declencheur.Declencheur(proba.Proba(0.05), "endurcissementEnfance")
        apprentissageEnfance.AjouterCondition(chapitre1)
        endurcissementEnfance.AjouterCondition(en_hiver)
        selecteur_.ajouterDeclencheur(endurcissementEnfance)

label apprentissageHydrauliqueEnfance:
    scene bg morvan
    $ _test_carac = trait.Intelligence.NOM
    $ _test_difficulte = -10
    $ _test_texte_menu = "Le bois du Morvan approvisionne Paris. Il est expédié par flottage sur les fleuves qui se jettent d'abord dans l'Yonne puis la Seine."
    $ _test_texte_reussi = "Les étangs artificiels avec barrages qu'on crée pour stocker puis envoyer les troncs vous passionnent et vous en apprenez vite les subtilités."
    $ _test_action_reussi = lambda: SetValMaitrise(maitrise.Hydraulique.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    call _test_de_carac
    jump fin_cycle

label endurcissementEnfance:
    scene bg morvan
    "L'hiver dans le morvan est particulièrement dur. Cela renforce la patience et la volonté."
    $ AjouterACarac(trait.Volonte.NOM, 1)
    menu:
        "Comment supportez vous l'isolement et le froid ?"
        "Vous vous promenez dans les montagnes malgré le froid":
            $ AjouterACarac(trait.Endurance.NOM, 1)
        "Vous vous occupez des animaux":
            $ AjouterACarac(trait.Animaux.NOM, 1)
        "Vous étudiez":
            $ AjouterACarac(trait.Intelligence.NOM, 1)
    jump fin_cycle

# lieu, époque, enfance au pays
label intro:
    scene bg morvan
    with dissolve
    show screen valeurs_traits
    "Nous sommes en 1620. Vous êtes le jeune Sébastien Le Prestre."
    "Vous êtes de la petite noblesse des confins bourguignons et nivernais."
    "La région froide et assez montagneuse où vous êtes né s'appelle le Morvan, et c'est un rude pays."
    "Vous avez 11 ans, vous avez appris à lire, écrire et compter."
    "Vous êtes aussi instruit en religion car vous avez lu des {i}Vies de Saint{/i} et des {i}Maximes chrétiennes{/i}."
    jump fin_cycle
    # jump grade_ordre_saint_louis # tmp

label apprentissageEnfance:
    scene bg morvan
    menu choix_apprentissage:
        "Que préférez vous faire pour vous amuser ?"
        "Dessiner":
            $ AjouterACarac(trait.Habilete.NOM, 1)
        "Escalader les arbres":
            $ AjouterACarac(trait.Mouvement.NOM, 1)
        "Jouer à cache cache":
            $ AjouterACarac(trait.Perception.NOM, 1)
            $ AjouterACarac(trait.Discretion.NOM, 1)
    jump fin_cycle

label apprentissageEquitation:
    scene bg morvan
    # test d'adresse pour réussir l'apprentissage
    $ _test_carac = trait.Mouvement.NOM
    $ _test_difficulte = 40
    $ _test_texte_menu = "Comme tout gentilhomme qui se respecte vous prenez très tôt beaucoup de leçons d'équitation."
    $ _test_texte_reussi = "Vous progressez vite."
    $ _test_texte_echoue = "Ce n'est pas votre fort."
    $ _test_action_reussi = lambda: SetValMaitrise(maitrise.Equitation.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    call _test_de_carac
    jump fin_cycle
