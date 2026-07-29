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

    def AjouterEvts8Summum():
        global selecteur_
        
        dateNbJours = 1691 * 365 + 1 # ------------------------------------------------- 1691
        debut_chapitre8 = declencheur.DeclencheurDate(dateNbJours, "debut_chapitre8")
        selecteur_.ajouterDeclencheur(debut_chapitre8)
        
        dateNbJours = 1693 * 365 + 1
        grade_ordre_saint_louis = declencheur.DeclencheurDate(dateNbJours, "grade_ordre_saint_louis")
        selecteur_.ajouterDeclencheur(grade_ordre_saint_louis)

label grade_ordre_saint_louis:
    scene bg ordre saint louis
    with dissolve
    show louisXIV at right
    with moveinright
    louisXIV "Je viens de créer l'ordre de Saint Louis pour les soldats méritants qui ont glorieusement servi la France et ma personne."
    louisXIV "Je compte vous faire l'honneur de vous accepter dans cet ordre eut égard à vos remarquables états de service."
    louisXIV "C'est un très grand honneur mais qui se mérite aussi par l'ascendance noble et j'insiste pour que vous fournissez à mes enquêteurs toutes les preuves de vos titres."
    $ valOrgueil = -situation_.GetValCaracInt(viceVertu.Humble.NOM)
    menu:
        "Après tout ce que j'ai accompli ?Je refuse de me soumettre à ce contrôle humiliant(Destin +1)" if valOrgueil >= 1:
            $ AjouterACarac(trait.Destin.NOM, 1)
            louisXIV "Votre attitude me navre et est peut-être signe de votre ascendance roturière."
            $ RetirerACarac(vauban.Vauban.C_FAVEUR_ROI, 5)
            $ _test_carac = trait.Eloquence.NOM
            $ _test_difficulte = -30
            $ _test_texte_menu = "Vous plaidez tout de même votre cause."
            $ _test_texte_reussi = "À la surprise générale vous convainquez le roi qui reconnaît votre valeur et vous accorde le titre malgré votre insolence."
            $ _test_texte_echoue = "Mais rien n'y fait."
            $ _test_label_reussi = "grade_ordre_saint_louis2"
            call _test_de_carac
            jump fin_cycle
        "Vous vous soumettez aux ordres":
            "Cela aura été bien laborieux et humiliant, mais enfin..."
            jump grade_ordre_saint_louis2

    label grade_ordre_saint_louis2:
        "Vous voila membre de l'ordre de Saint Louis."
        $ situation_.SetValCarac(vauban.Vauban.C_GRADE, vauban.Vauban.GRADE_SAINT_LOUIS)

    jump fin_cycle

label debut_chapitre8:
    "A FAIRE : début chapitre8"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 8)
    jump fin_cycle
