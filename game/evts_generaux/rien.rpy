# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite.trait import trait
    from abs.univers import temps

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(0.05, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = [
        "evtRien1", "evtRien2", "evtRien3", "evtRien4", "evtRien7",
        "evtRien8", "evtRien9", "evtRien10", "evtRien11", "evtRien12",
        "evtRien13", "evtRien14", "evtRien16",
        "evtRien19", "evtRien20"
        ]
        scenesParDefaut = []
        musiquesAEnquiller = []

        # religion
        evtsVides_.append("evtRien_saints")
        scenesParDefaut.append("bg crucifixion")
        musiquesAEnquiller.append("musique/journeytoabsolution.ogg")

        # enfant
        if chapitre1:
            evtsVides_.append("evtRien_enfance1")

        # dans le morvan
        if chapitre1:
            evtsVides_.append("evtRien_morvan1")
            evtsVides_.append("evtRien_morvan2")
            evtsVides_.append("evtRien_morvan3")
            evtsVides_.append("evtRien_morvan4")

        # étudiant
        if estEtudiant:
            evtsVides_.append("evtRien_etudiant1")
            evtsVides_.append("evtRien_etudiant2")
            evtsVides_.append("evtRien_etudiant3")

        if auMoinsAdolescent:
            evtsVides_.append("evtRien5")

        # alboflède
        if situation_.GetValCaracInt(vauban.Vauban.C_ALBOFLEDE) == 1:
            evtsVides_.append("evtRien_alboflede")

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

        # alamans
        if situation_.GetValCarac(germains.Alamans.C_VAINCU) != 1:
            evtsVides_.append("evtRien_alamans")


        # -----------------------------------------------------------------------------
        if len(evtsVides_) == 0:
            evtsVides_ = ["evtRien1", "evtRien2" ]

        if len(scenesParDefaut) == 0:
            sceneParDefaut = "bg cours_merovingienne"

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
    "Les paysans morvandiaux vivent de pain d'ordre et d'avoine mêlés, dont ils n'otent même aps le son."
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

label evtRien_ChristianismeMerovingien_1:
    "Les conciles désapprouvent que les fidèles chantent des chansons d'amour dans les églises. Ils imposent le chant des psaumes."
    jump fin_cycle

label evtRien_paien_Christianisme_1:
    scene bg crucifixion
    "Vous êtes de plus en plus intéressé par le christianisme mais la crucifixion du christ vous semble toujours aussi innaceptable."
    "Si vous et vos francs aviez été là vous auriez vengé cette injure. Alors pourquoi son père, un Dieu soit disant tout puissant n'a-t-il rien fait ?"
    jump fin_cycle

label evtRien_paien_Christianisme_2:
    scene bg crucifixion
    "Le tombeau de Saint Martin de Tours est devenu un lieu de pélerinage très populaire chez les chrétiens. Les miracles y sont nombreux."
    jump fin_cycle

label evtRien_alamans:
    $ AfficherCarteActuelle()
    "Vous recevez régulièrement des rapports et des plaintes pour les exactions des alamans à l'est."
    "Les burgondes et les francs de l'Est les contiennent pour l'instant mais tôt ou tard il faudra les calmer."
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

label evtRien_alboflede:
    scene bg cours_merovingienne
    with dissolve
    show alboflede at right
    with moveinright
    albo "Pas trop de soucis aujourd'hui mon frère ?"
    cl "Non, un jour calme et un temps trop mauvais pour la chasse. Mais par contre idéal pour passer la journée au coin du feu en famille."
    albo "Nous ne sommes donc que votre troisième choix. C'est déjà plutôt honorable je peux m'en contenter."
    "Sa finesse d'esprit et sa douceur font de votre grande soeur Alboflède le meilleur moyen d'illuminer une journée pluvieuse. Vous passez finalement une très bonne journée."
    jump fin_cycle

label evtRien1:
    with Dissolve(.5)
    $ romain = random.randint(0,1)
    $ nomPerso = gaulois_.CreerPrenom(True)
    $ nomFaction = "gaulois"
    if romain == 0:
        $ nomPerso = romains_.CreerPrenom(True)
        $ nomFaction = "romain"
    "[nomPerso], un riche [nomFaction] vient de mourir. Très pieux, il fait don de l'essentiel de sa fortune à l'église. Il a aussi affranchi une grande partie de ses esclaves."
    jump fin_cycle

label evtRien2:
    with Dissolve(.5)
    "La production de cervoise est en plein essor."
    jump fin_cycle

label evtRien3:
    with Dissolve(.5)
    "Aujourd'hui le cuisinier vous a préparé un plat exotique méditerrannéen à base de fruits qu'on appelle dattes."
    jump fin_cycle

label evtRien4:
    with Dissolve(.5)
    "Votre cuisinier prépare le mouton à merveille. Mais le sommet du repas reste le fromage avec le vin."
    jump fin_cycle

label evtRien5:
    with Dissolve(.5)
    "Aujourd'hui vous avez dû rédiger une importante lettre de votre main. Vous scellez la lettre de votre sceau."
    jump fin_cycle

label evtRien7:
    scene bg chasse
    with Dissolve(.5)
    "Vous vous faites construire un palais secondaire en bordure de forêt. Ainsi vous pourrez facilement aller chasser dès que l'envie vous en prendra."
    jump fin_cycle

label evtRien8:
    with Dissolve(.5)
    "Parmi les coutumes romaines les jeux de cirque sont toujours aussi populaires, même chez les francs."
    "Certes ceux qui se donnent en Gaule de nos jours sont loin d'être somptueux comme à Rome. Mais vous avez les moyens d'organiser des courses de char et même des combats de gladiateurs."
    jump fin_cycle

label evtRien9:
    with Dissolve(.5)
    "Les marchands du sud amènent dans vos marchés des machandises exotiques prisées : huile d'olives, soieries, épices..."
    jump fin_cycle

label evtRien10:
    with Dissolve(.5)
    "Les marchands du nord, de plus en plus nombreux, amènent sur vos marchés du bois, des tissus, des esclaves..."
    jump fin_cycle

label evtRien11:
    with Dissolve(.5)
    "Sur le modèle de l'empire romain vos serviteurs tiennent des comptes écris détaillés des opérations financières du royaume."
    jump fin_cycle

label evtRien12:
    with Dissolve(.5)
    "Les pirates esclavagistes ont du avoir de beaux succès en ratissant les côtes de la manche. Il y a une énorme quantité d'esclaves angles et saxons sur les marchés cette année."
    jump fin_cycle

label evtRien13:
    with Dissolve(.5)
    "Pour vous distraire et vous détendre vous vous prenez l'habitude de jouer aux osselets avec votre famille et vos amis."
    jump fin_cycle

label evtRien14:
    scene bg ludus
    with Dissolve(.5)
    "Après les avoir méprisés un temps les francs ont commencé à apprécier les multiples jeux des romains. Vous avez un faible pour le ludus duodecim scriptorum."
    jump fin_cycle

label evtRien16:
    with Dissolve(.5)
    $ nom = francs_.CreerPrenom(True)
    "Comme tous les mois la justice populaire franque est rendue sur le marlberg (tumulus)."
    "[nom], accusé et condamné pour vol, a refusé la sentence et s'est enfui. Il a été maudit par le conseil et tout le monde a maintenant le droit et le devoir de le poursuivre et de planter sa tête sur un pieu."
    jump fin_cycle

# label evtRien18:
    # with Dissolve(.5)
    # $ femmeFranque = francs_.CreerPrenom(False) # A FAIRE : ajouter une création de nom français
    # "[femmeFranque] a été accusée de vol. Elle a accepté de subir l'ordalie."
    # "Elle a plongé sa main dans un chaudron d'eau bouillante. Supportant la souffrance elle a réussi à saisir l'anneau qui s'y trouvait. Les juges ont ensuite attendu 3 jours et constaté que sa cicatrice est belle et bien formée."
    # "[femmeFranque] est donc déclarée innocente du vol."
    # jump fin_cycle

label evtRien19:
    with Dissolve(.5)
    "Depuis que les huns ont été repoussés de Gaule par vos ancêtres ils sont devenus bien moins agressifs et bien plus commerçants."
    "Ils ont introduit dans votre cour des objets d'orphèvrerie que vos propres artisans sont incapables de réaliser. Vous les poussez à apprendre à reproduire ces techniques."
    jump fin_cycle

label evtRien20:
    with Dissolve(.5)
    "La consignation de vos actes royaux et les formulaires de toute sortes nécessitent de fortes importations de papyrus d'Orient."
    jump fin_cycle

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
