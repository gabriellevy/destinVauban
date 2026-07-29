init -5 python:
    import random
    from abs.religions import religion
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite.trait import trait
    from abs.humanite import metier

    def AjouterEvtsHistoire():
        global selecteur_
        # Pour les événements généraux importants à l'échelle mondiale mais juste informatifs à l'échelle du jeu
