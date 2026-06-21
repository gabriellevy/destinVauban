init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from abs.humanite import metier
    from spe import dec_vauban

    def AjouterEvtsFamille():
        global selecteur_
        # naissance de Charlotte
        dateNbJours = 5*30 + 1661 * 365 + 1 # juin 1661
        naissanceCharlotte = declencheur.DeclencheurDate(dateNbJours, "naissanceCharlotte")
        selecteur_.ajouterDeclencheur(naissanceCharlotte)
        # marriage de Charlotte
        dateNbJours = 2*30 + 1680 * 365 + 26 # 26 mars 1680
        marriageCharlotte = declencheur.DeclencheurDate(dateNbJours, "marriageCharlotte")
        selecteur_.ajouterDeclencheur(marriageCharlotte)
        
        # mariage de Jeanne-Françoise
        dateNbJours = 1681 * 365 + 8 # 8 janvier 1681
        marriageJeanneFrançoise = declencheur.DeclencheurDate(dateNbJours, "marriageJeanneFrançoise")
        selecteur_.ajouterDeclencheur(marriageJeanneFrançoise)

label naissanceCharlotte:
    scene bg naissance
    "[situation_.AffichageDate()] : Votre fille Charlotte vient de naître."
    jump fin_cycle

# A FAIRE ? ajouter des gains de richesse, faveur, des néociation, envie de laisser le choix à sa fille ????
label marriageCharlotte:
    scene bg mariage
    "26 mars 1681 : Votre fille Charlotte épouse en l'église d'Epiry, en Morvan, Jacques-Louis de Mesgrigny."
    "C'est le neveu de Jean de Mesgrigny, votre grand ami, compagnon de siège, ingénieur, lieutenant général et gouverneur de la citadelle de Tournai."
    jump fin_cycle

# A FAIRE ? ajouter des gains de richesse, faveur, des néociation, envie de laisser le choix à sa fille ????
label marriageJeanneFrançoise:
    scene bg mariage
    "8 janvier 1681 : Jeanne-Françoise se marie le 8 janvier 1691 en l'église Saint-Roch de Paris, avec Louis II Bernin, marquis de Valentinay, seigneur d'Ussé et de Rivarennes."
    "Il est apparenté au contrôleur général des finances Claude Le Peletier, à deux intendants des finances, à des membres de la cour des comptes et à des trésoriers généraux des finances."
    "Ce mariage vous rapproche du monde des officiers de la finance et des parlementaires. "
    jump fin_cycle
