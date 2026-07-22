# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from abs.univers import temps

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(0.05, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = [
        "evtRien1", 
        ]
        scenesParDefaut = []
        musiquesAEnquiller = []

        # religion
        evtsVides_.append("evtRien_saints")
        scenesParDefaut.append("bg crucifixion")
        musiquesAEnquiller.append("musique/journeytoabsolution.ogg")

        # enfant
        if situation_.GetValCaracInt(vauban.Vauban.CHAPITRE) == 1:
            evtsVides_.append("evtRien_enfance1")
            evtsVides_.append("evtRien_enfance2")
            evtsVides_.append("evtRien_enfance3")

        # dans le morvan
        if situation_.GetValCaracInt(vauban.Vauban.CHAPITRE) == 1:
            evtsVides_.append("evtRien_morvan1")
            evtsVides_.append("evtRien_morvan2")
            evtsVides_.append("evtRien_morvan3")
            evtsVides_.append("evtRien_morvan4")

        # étudiant # environ 1646 à 1651
        if situation_.GetValCaracInt(vauban.Vauban.CHAPITRE) == 2:
            evtsVides_.append("evtRien_etudiant1")
            evtsVides_.append("evtRien_etudiant2")
            evtsVides_.append("evtRien_etudiant3")
            if situation_.GetValCaracInt(temps.Date.DATE_ANNEES) < 1649:
                evtsVides_.append("evtRien_fronde1_barricades")
            if situation_.GetValCaracInt(temps.Date.DATE_ANNEES) == 1649:
                evtsVides_.append("evtRien_fronde2_siege_paris")

        if auMoinsJeuneAdulte:
            evtsVides_.append("evtRien_auMoinsJeuneAdulte")

        # saison
        saison = situation.GetDateDuJour().GetSaison()
        if saison == temps.Date.PRINTEMPS:
            evtsVides_.append("evtRien1_printemps")
            musiquesAEnquiller.append("musique/Sea Season.ogg")
        if saison == temps.Date.HIVER:
            musiquesAEnquiller.append("musique/Dark Season.ogg")
        if saison == temps.Date.ETE:
            musiquesAEnquiller.append("musique/Fire Season.ogg")
        if saison == temps.Date.AUTOMNE:
            evtsVides_.append("evtRien1_automne")
            evtsVides_.append("evtRien2_automne")
            evtsVides_.append("evtRien3_automne")

        # -----------------------------------------------------------------------------
        if len(evtsVides_) == 0:
            evtsVides_ = ["evtRien1", "evtRien2" ]

        if len(scenesParDefaut) == 0:
            sceneParDefaut = "bg morvan"

        # ajoute une musique à la file au hasard :
        if len(musiquesAEnquiller) != 0:
            renpy.music.queue(random.choice(musiquesAEnquiller), clear_queue=False)

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(random.choice(scenesParDefaut))
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label evtRien_morvan1:
    scene bg morvan
    "Les paysans morvandiaux sont grands et assez bien faits, surement grâce au bon air de ce pays et au travail dans les forêts."
    jump fin_cycle

label evtRien_morvan2:
    scene bg morvan
    "Les paysans morvandiaux vivent de pain d'ordre et d'avoine mêlés, dont ils n'otent même pas le son."
    "Plus de mauvais fruits, la plupart sauvages, et de quelque peu d'herbes potagères de leurs jardin, cuites à l'eau, avec un peu d'huile de noix ou de navette, le plus souvent sans, ou avec très peu de sel."
    jump fin_cycle

label evtRien_morvan3:
    scene bg morvan
    "Malgré le rude climat les paysans morvandiaux vaquent à leurs occupations vêtus hiver comme été de toile à demi pourrie et déchirée, et chaussés de sabots, dans lesquels ils ont le pied nu tout l'année."
    jump fin_cycle

label evtRien_morvan4:
    scene bg morvan
    "La guerre de 30 ans bat son plein et des rumeurs de batailles et d'épidémies arrivent souvent à vos oreilles."
    "Dieu merci elle semble se cantonner à la plaine de Saône et ne pas atteindre le Morvan mais les paysans demeurent tendus : les guerres de religions ne sont pas si loin."
    "À l'époque le seul moyen d'échapper aux ravages des soldats était de fuir dans la forêt pour s'y cacher."
    jump fin_cycle

label evtRien1_automne:
    "C'est l'époque des semailles d'orge."
    jump fin_cycle

label evtRien2_automne:
    "C'est l'époque des semailles de froment."
    jump fin_cycle

label evtRien3_automne:
    "C'est l'époque des semailles de seigle."
    jump fin_cycle

label evtRien1_printemps:
    "C'est l'époque des semailles d'avoine."
    jump fin_cycle

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)

label evtRien_auMoinsJeuneAdulte:
    with Dissolve(.5)
    "Aujourd'hui vous avez dû rédiger une importante lettre de votre main. Vous scellez la lettre de votre sceau."
    jump fin_cycle

label evtRien1:
    "Sous Louis XIII le nombre d'ingénieur a beaucoup augmenté mais ils n'atteignaient pas encore la centaine, cela reste un poste rare mais de plus en plus précieux."
    "Ler rôle est maintenant très reconnu lors des sièges, que ce soit dans l'attaque ou dans la défense. En plus, bien sûr, de bâtir les places fortes."
    jump fin_cycle

# label evtRien18:
    # with Dissolve(.5)
    # $ femmeFranque = francais_.CreerPrenom(False)
    # "[femmeFranque] a été accusée de vol. Elle a accepté de subir l'ordalie."
    # "Elle a plongé sa main dans un chaudron d'eau bouillante. Supportant la souffrance elle a réussi à saisir l'anneau qui s'y trouvait. Les juges ont ensuite attendu 3 jours et constaté que sa cicatrice est belle et bien formée."
    # "[femmeFranque] est donc déclarée innocente du vol."
    # jump fin_cycle

label evtRien_etudiant1:
    "Pendant vos études vous logez chez le prieur Pierre de Fontaines."
    jump fin_cycle

label evtRien_etudiant2:
    "Depuis que vous étudiez dans la petite de Semur vous adorez vous y promener, surtout pour voir et revoir ses puissantes fortifications médiévales dominant l'Arançon."
    jump fin_cycle

label evtRien_etudiant3:
    "Le paysage ici est bien différent de chez vous. Plus de montagne, seulement des colines et de vastes plaines pleines de champs de céréales."
    jump fin_cycle

label evtRien_enfance1:
    "Vous aidez votre père Urbain Le Prestre à greffer des arbres fruitiers."
    jump fin_cycle

label evtRien_enfance2:
    scene bg rocroi
    with Dissolve(.5)
    "Votre père vous raconte la mort héroïque de vos oncles soldats."
    "Son grand frère Paul a été tué quand vous aviez deux ans à la bataille de Rethel."
    "Quand vous aviez quatre ans c'est son cadet Gabriel qui est mort glorieusement à la bataille d'Honnecourt."
    "Votre père vous rappelle que c'est le devoir d'un noble de se battre et de mourir pour son roi et la patrie."
    "N'importe quand le roi peut appeler le ban et l'arrière ban ; et l'ordre noble guerrier doit se présenter et servir."
    "Vous ne pouvez tout de même pas vous empêcher de penser que c'est bien trise que vos 3 cousins n'aient pas de papa."
    "Heureusement que votre papa à vous s'en est sorti."
    jump fin_cycle

label evtRien_enfance3:
    scene bg rocroi
    with Dissolve(.5)
    "Votre père vous raconte la bataille de Rocroi où le Grand Condé vainquit les espagnols."
    "C'était la première fois que la redoutable infanterie des tercios espagnols, une combinaison de piquiers et mousquetaires, était vaincue."
    "Votre famille -les Le Prestre- appartient à la clientèle des Condé, qui sont gouverneurs de Bourgogne, vos oncles les ont servi à la guerre."
    "La gloire du grand Condé, le plus illustre d'entre eux, rejaillit donc sur vous tous."
    jump fin_cycle

label evtRien_fronde1_barricades:
    scene bg barricades
    with Dissolve(.5)
    "Une grave journée d'émeute a eu lieu à Paris à ce qu'on dit."
    "Le cardinal Mazarin et la reine Anne d'Autriche ont enfermé des conseillers du parlement qui s'opposaient à leurs réformes."
    "Mais les parisiens en ont été furieux et ont dressé des barricades dans toute la ville, et ils ont fait céder le cardinal et la reine."
    "Cette désobéissance des parisiens est grave, mais ont-ils vraiment tort de s'opposer à une arrestation arbitraire décidée par un cardinal italien ?"
    jump fin_cycle

label evtRien_fronde2_siege_paris:
    scene bg barricades
    with Dissolve(.5)
    "Des troubles très graves ont lieu dans le royaume et en particulier autour de Paris."
    "Votre suzerain le grand Condé a mis le siège devant Paris et paraît-il maté les révoltés donc tout devrait rentrer dans l'ordre."
    "Mais depuis le Morvan il est difficile de comprendre tout ce qui se passe."
    jump fin_cycle
