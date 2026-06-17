init -5 python:
    import random
    from spe import dec_vauban
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import germains
    from chapitres.classes import vauban

    def AjouterEvtsMarechalImportun():
        global selecteur_
        
        dateNbJours = 1697 * 365 + 1 # ------------------------------------------------- 1697
        debut_chapitre9 = dec_vauban.DecVaubanU(proba.Proba(0.4, False), "debut_chapitre9", dateNbJours)
        selecteur_.ajouterDeclencheur(debut_chapitre9)
        
        dateNbJours = 1705 * 365 + 1
        grade_ordre_saint_louis = dec_vauban.DecVaubanU(proba.Proba(0.4, False), "grade_ordre_saint_louis", dateNbJours)
        selecteur_.ajouterDeclencheur(grade_ordre_saint_louis)

label debut_chapitre9:
    "A FAIRE : début chapitre9"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 9)
    jump fin_cycle

label grade_ordre_saint_louis:
    # A FAIRE : faire ça via un perso Louis XIV ou Louvois et avec plus de decorum : 
    scene bg honneur
    with dissolve
    "[situation_.AffichageDate()]"
    "Le roi compte vous faire l'honneur de vous accepter dans l'ordre de Saint Louis."
    "Ce serait un très grand honneur si on ne vous infligeait encore  de fournir maintes formulaires et documents prouvant votre ascendance noble."
    $ valOrgueil = -situation_.GetValCaracInt(trait.Humble.NOM)
    menu:
        "Vous vous soumettez aux ordres":
            jump grade_ordre_saint_louis2
        "Vous protestez énergiquement et refusez de vous soumettre à ce contrôle (Destin +1)" if valOrgueil >= 1:
            $ AjouterACarac(trait.Destin.NOM, 1)
            "Le roi est particulièrement outré de votre attitude."
            $ RetirerACarac(vauban.Vauban.C_FAVEUR_ROI, 5)
            $ _test_carac = trait.Eloquence.NOM
            $ _test_difficulte = -30
            $ _test_texte_menu = "Vous plaidez tout de même votre cause."
            $ _test_texte_reussi = "À la surprise générale vous convainquez le roi qui reconnaît votre valeur et vous accorde le titre malgré votre insolence."
            $ _test_texte_echoue = "Mais rien n'y fait."
            $ _test_label_reussi = "grade_ordre_saint_louis2"
            call _test_de_carac
            jump fin_cycle

    label grade_ordre_saint_louis2:
        "Cela aura été bien laborieux et humiliant, mais enfin vous voila membre de l'ordre de Saint Louis."
        $ situation_.SetValCarac(vauban.Vauban.C_GRADE, vauban.Vauban.GRADE_SAINT_LOUIS)

    jump fin_cycle
