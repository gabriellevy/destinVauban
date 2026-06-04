init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from spe import dec_vauban

    def AjouterEvtsFamille():
        global selecteur_
        # naissance de Charlotte
        dateNbJours = 5*30 + 1661 * 365 + 1 # juin 1661
        naissanceCharlotte = dec_vauban.DecVaubanU(proba.Proba(10, True), "naissanceCharlotte", dateNbJours)
        selecteur_.ajouterDeclencheur(naissanceCharlotte)

label naissanceCharlotte:
    scene bg naissance
    "[situation_.AffichageDate()] : Votre fille Charlotte vient de naître."
    jump fin_cycle
