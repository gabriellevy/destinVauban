init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import vauban

    chapitre3 = condition.Condition(vauban.Vauban.CHAPITRE, 3, condition.Condition.EGAL_NUMERIQUE)
    fortification1plus = condition.Condition(maitrise.Fortification.NOM, 1, condition.Condition.SUPERIEUR_EGAL)

    def AjouterEvts3DebutsMilitaires():
        global selecteur_
        # ---------------- évéements à date fixe
        dateNbJours = 1651 * 365 + 31 * 2 +17 # ------------------------------------------------- 17 mars 1651
        debut_chapitre3 = declencheur.DeclencheurDate(dateNbJours, "debut_chapitre3")
        selecteur_.ajouterDeclencheur(debut_chapitre3)
        dateNbJours = 1651 * 365 + 31 * 11 + 4 # ------------------------------------------------- hiver 1651
        construction_clermont_en_argonne = declencheur.DeclencheurDate(dateNbJours, "construction_clermont_en_argonne")
        construction_clermont_en_argonne.AjouterCondition(fortification1plus)
        selecteur_.ajouterDeclencheur(construction_clermont_en_argonne)
        dateNbJours = 1652 * 365 + 31 * 3 +17 # ------------------------------------------------- 17 avril 1652
        mort_pere = declencheur.DeclencheurDate(dateNbJours, "mort_pere")
        selecteur_.ajouterDeclencheur(mort_pere)
        dateNbJours = 1652 * 365 + 31 * 6 + 2 # ------------------------------------------------- 2 juillet 1652
        defaites_conde = declencheur.DeclencheurDate(dateNbJours, "defaites_conde")
        selecteur_.ajouterDeclencheur(defaites_conde)
        dateNbJours = 1652 * 365 + 31 * 9 + 12 # ------------------------------------------------- octobre 1652
        fuite_conde = declencheur.DeclencheurDate(dateNbJours, "fuite_conde")
        selecteur_.ajouterDeclencheur(fuite_conde)
        dateNbJours = 1652 * 365 + 31 * 10 + 12 # ------------------------------------------------- novembre 1652
        siege_sainte_menehould = declencheur.DeclencheurDate(dateNbJours, "siege_sainte_menehould")
        selecteur_.ajouterDeclencheur(siege_sainte_menehould)
        dateNbJours = 1653 * 365 + 31 * 3 + 12 # ------------------------------------------------- avril 1653
        capture_en_reconnaissance = declencheur.DeclencheurDate(dateNbJours, "capture_en_reconnaissance")
        selecteur_.ajouterDeclencheur(capture_en_reconnaissance)
        dateNbJours = 1653 * 365 + 31 * 9 + 20 # ------------------------------------------------- 20 octobre 1653
        siege_sainte_menehould_2 = declencheur.DeclencheurDate(dateNbJours, "siege_sainte_menehould_2")
        selecteur_.ajouterDeclencheur(siege_sainte_menehould_2)
        dateNbJours = 1654 * 365 + 31 * 6 + 1 # ------------------------------------------------- 1er juillet 1654
        siege_stenay = declencheur.DeclencheurDate(dateNbJours, "siege_stenay")
        selecteur_.ajouterDeclencheur(siege_stenay)
        dateNbJours = 1654 * 365 + 31 * 10 + 7 # ------------------------------------------------- novembre 1654
        siege_Clermont_en_Argonne = declencheur.DeclencheurDate(dateNbJours, "siege_Clermont_en_Argonne")
        selecteur_.ajouterDeclencheur(siege_Clermont_en_Argonne)

        # ------------------ événements génériques
        # aura besoin des maths : chances de les apprendre si ce n'est pas encore le cas : 
        apprentissageMathematiques2 = declencheur.Declencheur(proba.Proba(0.2), "apprentissageMathematiques2")
        apprentissageMathematiques2.AjouterCondition(chapitre3)
        apprentissageMathematiques2.AjouterCondition(mathematiques0)
        selecteur_.ajouterDeclencheur(apprentissageMathematiques2)
        # sinon il a des missions de base pour apprendre les bases
        apprentissageFortification2 = declencheur.Declencheur(proba.Proba(0.1), "apprentissageFortification2")
        apprentissageFortification2.AjouterCondition(chapitre3)
        apprentissageFortification2.AjouterCondition(fortification0)
        selecteur_.ajouterDeclencheur(apprentissageFortification2)

        apprentissageSurLeTas = declencheur.Declencheur(proba.Proba(0.05), "apprentissageSurLeTas")
        apprentissageSurLeTas.AjouterCondition(chapitre3)
        selecteur_.ajouterDeclencheur(apprentissageSurLeTas)

label siege_Clermont_en_Argonne:
    "Toujours sous les ordres de Monsieur de Clervilles, vous assiégez Clermont-en-Argonne."
    "Encore une ville où vous avez séjourné précédemment et où vos souvenirs seront précieux."
    $ _test_texte_menu = "Indisposé, Clerville vous charge de travaux d'approche important et de la pose de mines destinées à faire sauter trois points vulérables."
    $ _test_carac = trait.Intelligence.NOM
    $ _test_difficulte = situation_.GetValCaracInt(maitrise.Poliorcetique.NOM) * 20
    $ _test_texte_reussi= "Vous vous rappelez des meilleurs trajets pour s'approcher des murailles en limitant les tirs ennemis."
    $ _test_label_reussi = "siege_Clermont_en_Argonne_fin"
    $ _test_texte_echoue = "L'approche est laborieuse et dangereuse et coûte la vie à de nombreux mineurs."
    $ _test_label_echoue = "siege_Clermont_en_Argonne_fin"
    $ _test_action_reussi = lambda: AjouterACarac(vauban.Vauban.C_EXPLOITS, 1)
    call _test_de_carac

label siege_Clermont_en_Argonne_fin:
    "Vous décidez de laisser les assiégés voir que vous allez mettr eles mines  à feu pour les laisser paniquer et ils finissent par se rendre."
    "Heureusement, car la forteresse est solide, et les mines avaient peu de chances de permettre de la prendre facilement."
    "D'ailleurs, plutôt que de l'occuper, on vous charge juste après al reddition de détruire une forteresse qui a peu d'intérêt pour le roi et risquerait d'encore servir à abriter des rebelles."
    "Après ces multiples fortifications, sièges et destruction, on vous accorde finalement le titre d'ingénieur ordinaire du roi de sa majesté."
    jump fin_cycle

label siege_stenay:
    scene bg siege
    with dissolve
    "Vous êtes bientôt impliqué dans un nouveau siège à la ville de Stenay."
    "Vous êtes chargé de diriger les poseurs de mines qui doivent s'approcher de la muraille en creusant une tranchée puis la faire sauter."
    "C'est certes un honneur qui récompense votre bonne réputation mais c'est aussi un travail très dangereux où vous êtes la cible numéro un des assiégés."
    $ _test_texte_menu = "Alors que vous êtes proche du bastion de gauche et tentez d'y poser une mine les assiégés vous bombardent de bois et de matière inflammable."
    $ _test_carac = trait.Endurance.NOM
    $ _test_difficulte = 20
    $ _test_label_reussi = "siege_stenay_fin"
    $ _test_texte_echoue = "Vous êtes à moitié assomé par un morceau de bois que vous recevez sur la tête et êtes pris dans les flammes. Vous mourez dans d'atroces souffrances."
    $ _test_label_echoue = "mort"
    $ _label_ressurection = "siege_stenay_fin"
    call _test_de_carac

label siege_stenay_fin:
    "Vous êtes touché par des débris et légèrement enflammé mais parvenez à vous mettre à l'abri."
    "Le feu que les assiégés parviennent finalement à allumer repousse les sapeurs et fait s'éterniser le siège qui dure plus d'un mois pendant lequel vous vous remettez de votre blessure."
    "Ils finissent tout de même par capituler, à court de vivres et de munitions."
    "Vous êtes nommé capitaine en récompense de vos services."
    $ situation_.SetValCarac(vauban.Vauban.C_GRADE, vauban.Vauban.GRADE_CAPITAINE)
    "Les techniques employées par les assiégés ainsi que la créativité du Maréchal Favert qui relie astucieusement les tranchées d'approche pour faciliter l'attaque sont très instructives."
    if situation_.GetValCaracInt(maitrise.Poliorcetique.NOM) < 3:
        $ _test_texte_menu = "Vous tachez d'en tirer des leçons."
        $ _test_carac = trait.Intelligence.NOM
        $ _test_difficulte = 0
        $ _test_texte_reussi = "Vous apprenez à une vitesse étonnante."
        $ _test_action_reussi = lambda: AjouterACarac(maitrise.Poliorcetique.NOM, 1)
        $ _test_label_reussi = "fin_cycle"
        $ _test_label_echoue = "fin_cycle"
        call _test_de_carac
    jump fin_cycle

label siege_sainte_menehould_2:
    scene bg siege
    with dissolve
    "Ironie du sort : vous qui avez pris la ville de Saint Menehould sous les ordres de Condé, vous êtes chargé de la reprendre à ce dernier sous les ordres du chevalier de Clerville !"
    "Monsieur de Clerville est un ingénieur expérimenté et éminent qui mène les opérations de siège."
    $ _test_texte_menu = "Comme vous avez déjà séjourné récemment dans la ville fortifiée, Monsieur de Clerville compte sur votre mémoire et sens de l'observation pour faciliter le siège."
    $ _test_carac = trait.Intelligence.NOM
    $ _test_difficulte = 20
    $ _test_label_reussi = "siege_sainte_menehould_2_memoire"
    $ _test_texte_reussi = "Vous vous rappelez exceptionnellement bien de toutes les fortifications et proposez un plan détaillé à Monsieur de Clerville, ce qui facilite énormément la capture."
    $ _test_texte_echoue = "Vous aidez du mieux que vous pouvez mais vos indications sont bien imprécises."
    $ _test_label_echoue = "siege_sainte_menehould_2_prise"
    $ _test_action_reussi = lambda: AjouterACarac(vauban.Vauban.C_EXPLOITS, 1)
    call _test_de_carac

label siege_sainte_menehould_2_prise:
    "Sous les ordres de Monsieur de Clerville vous conduisez les lignes, tranchées, et sapes aussi efficacement que possible."
    $ situation_.AvanceDeXJours(34)
    "Le siège dure tout de même 34 jours et finit par la reddition de Montal, gouverneur depuis l’année précédente."
    "Il rend les armes en présence du jeune Louis, roi de France."
    "Celui ci est très satisfait et distribue les récompenses et titres. Vous êtes fait Lieutenant au régiment de Bourgogne infanterie."
    $ situation_.SetValCarac(vauban.Vauban.C_GRADE, vauban.Vauban.GRADE_LIEUTENANT_BOURGOGNE)
    jump siege_sainte_menehould_2_reparation

label siege_sainte_menehould_2_reparation:
    "Vous êtes chargé de réparer les fortifications de la ville durant l'hiver."
    if situation_.GetValCaracInt(maitrise.Fortification.NOM) < 1:
        "Malheureusement vos compétences sont insuffisantes et un ingénieur plus expérimenté est chargé de diriger l'essentiel du travail. Vous apprenez néanmoins beaucoup à son contact."
        $ SetValMaitrise(maitrise.Fortification.NOM, maitrise.TraitMaitrise.MAITRISE_A)
        $ situation_.AvanceDeXJours(34)
        jump fin_cycle
    else:
        $ _test_texte_menu = "Vous passez des mois à recontrsuire des fortifications épuisées par 2 sièges successifs."
        $ _test_carac = trait.Intelligence.NOM
        $ _test_difficulte = -10 + situation_.GetValCaracInt(maitrise.Fortification.NOM) * 20
        $ _test_texte_reussi = "Vous améliorez grandement les fortifications et à peu de frais."
        $ _test_texte_echoue = "Vos réparations sont techniquement bonnes, sans plus."
        $ _test_action_reussi = lambda: AjouterACarac(vauban.Vauban.C_EXPLOITS, 1)
        call _test_de_carac

label apprentissageSurLeTas:
    scene bg siege
    with dissolve
    menu choix_apprentissage_militaire:
        "La vie au camps est rude mais vous donne beaucoup d'occasions de faire vos preuves et vous améliorer."
        "Vous entrainez durement vos hommes":
            $ AjouterACarac(trait.Commandement.NOM, 1)
        "Vous vous entrainez plutôt au tir":
            $ AjouterACarac(trait.Tir.NOM, 1)
        "Vous observez les fortifications et en dessinez les plans":
            $ AjouterACarac(trait.Habilete.NOM, 1)
        "Vous tentez de comprendre le fonctionnement d'un camps militaire, sa position, sa logistique...":
            $ AjouterACarac(trait.Evaluation.NOM, 1)
    jump fin_cycle

label capture_en_reconnaissance:
    $ capture_en_reconnaissance_diff_poursuite=0
    $ capture_en_reconnaissance_diff_combat=-10
    "Vous êtes en reconnaissance avec trois compagnon quand vous êtes apperçus par une troupe d'au moins 10 cavaliers royaux."
    menu:
        "Vous sortez vos pistolets et les attaquez de face":
            jump capture_en_reconnaissance_combat
        "Vous tournez bride et fuyez":
            jump capture_en_reconnaissance_poursuite
        "Vous attendez de voir ce qu'ils vont faire":
            "Ils n'hésitent qu'un instant et foncent vers vous. Ils sont bien 15 contre vous 4."
            $ capture_en_reconnaissance_diff_poursuite=-10
            menu:
                "Vous sortez vos pistolets et les attaquez de face":
                    jump capture_en_reconnaissance_combat
                "Vous tournez bride et fuyez":
                    jump capture_en_reconnaissance_poursuite
        "Vous vous rendez":
            jump capture_en_reconnaissance_reddition
    jump fin_cycle

label capture_en_reconnaissance_combat:
    $ _test_carac = trait.Tir.NOM
    $ _test_difficulte = capture_en_reconnaissance_diff_combat
    $ _test_label_reussi = capture_en_reconnaissance_victoire
    $ _test_texte_reussi = "Vous abattez net leur officier et blessez gravement un autre tandis que vos compagnons, armés de mousquets, abattent eux aussi deux cavaliers."
    $ _test_texte_echoue = "Impossible de les prendre de vitesse ils sont maintenant juste derrière vous."
    $ _test_label_echoue = "mort"
    call _test_de_carac

label capture_en_reconnaissance_poursuite:
    $ _test_carac = trait.Habilete.NOM
    $ _test_difficulte = capture_en_reconnaissance_diff_poursuite-10
    $ _test_texte_menu = "Ces militaires sont entrainés et ont de bons chevaux."
    $ _test_texte_reussi = "Vous les prenez de vitesse et réussissez à rentrer sain et sauf au camps."
    $ _test_texte_echoue = "Impossible de les prendre de vitesse ils sont maintenant juste derrière vous."
    $ _test_label_echoue = "capture_en_reconnaissance_rattrape"
    call _test_de_carac

label capture_en_reconnaissance_rattrape:
    $ capture_en_reconnaissance_diff_combat-=10
    menu:
        "Vous sortez vos pistolets et les attaquez de face":
            jump capture_en_reconnaissance_combat
        "Vous vous rendez en demandant les honneurs de la guerre":
            jump capture_en_reconnaissance_reddition
    jump fin_cycle

label capture_en_reconnaissance_reddition:
    "En tant que noble vous devez vous rendre avec honneur et courage pour mériter votre titre."
    "Vous dégainez votre pistolet et visez le chef ennemi."
    vaub "Je n'accepterai de me rendre que si je peux garder mes armes et que vous ne me forcez pas à mettre pied à terre"
    $ _test_carac = trait.Eloquence.NOM
    $ _test_difficulte = 40
    $ _test_texte_menu = "Il faut que vous respectiez parfaitement les usages."
    $ _test_texte_reussi = "L'officier est impressionné par votre courage, et, étant lui-même gentilhomme, accepte vos termes."
    $ _test_label_reussi = "capture_en_reconnaissance_reddition_reussi"
    $ _test_texte_echoue = "Vous tremblez, perdez vos mots, et un de vos compagnons craque et ouvre le feu."
    $ _test_label_echoue = "capture_en_reconnaissance_combat"
    call _test_de_carac

label capture_en_reconnaissance_reddition_reussi:
    "Vous êtes raccompagné sous bonne escorte mais en ayant la garantie de ne pas être dépouillé."
    "En retour, vous donnez votre parole de gentihomme que vous ne profiterez pas de la faveur qu'on fait à votre noblesse pour fuir traitreusement."
    "Vous êtes tout de même enfermé, mais  dans de bonnes conditions."
    "Quelques jours plus tard vos avez l'insigne honneur d'être reçu par le cardinal Mazarin, premier conseiller du roi !"
    show mazarin at right
    with moveinright
    maz "Votre courage pendant la capture et les connaissances que vous avez montré des fortifications lors de votre interrogatoire ont attiré mon attention."
    maz "Vous n'êtes pas sans savoir que le roi a accordé pardon et amnistie à ceux qui ont fait l'erreur de se rebeller contre lui à condition qu'ils renoncent à servir le rebelle Condé."
    maz "Vous êtes encore jeune, votre erreur de jugement est tout à fait pardonnable, et vous auriez tort de refuser la générosité du roi le plus grand et le plus généreux qui soit."
    maz "S'il vous plaît rejoignez l'arméée royale, aidez nous à mettre fin à cette guerre civile, et vous serez apprécié à votre juste valeur."
    menu:
        "Qu'en dites vous ?"
        "J'accepte de servir le roi":
            # A FAIRE : explication de sa réaffectation ??
            jump fin_cycle
        "Jamais je ne trahirai le Grand Condé !":
            "A FAIRE : que va t'il lui arriver en attendant la fin de Condé ?? en prison jusqu'à sa fuite à Bruxelles ?"
            jump fin_cycle
    jump fin_cycle

label capture_en_reconnaissance_victoire:
    "Les ennemis ripostent mollement puis se débandent et préfèrent abandonner à votre grand soulagement."
    "Vous rentrez sain et sauf au camps qui est rapidement au courant de votre exploit."
    $ AjouterACarac(vauban.Vauban.C_EXPLOITS, 1)
    # A FAIRE : comment VA6T4IL SE RETROUVER au serice du roi si il n'a pas été fait prisonnier
    jump fin_cycle

label siege_sainte_menehould:
    scene bg siege
    with dissolve
    "Fidèle à son caractère agressif le grand Condé ne reste pas sur la défensive. Il ordonne le siège de Sainte Menehould et vous y êtes envoyé."
    "Elle n'est défendue que par des bourgeois et 120 irlandais mais ceux-ci s'avèrent coriaces et déterminés. Ils brûlent vifs nos mineurs père et fils dans leurs trous avec des produits inflammables."
    "De votre côté vous êtes chargé de construire des abris rapprochés pour permettre aux soldats de se rapprocher des murailles à l'abri."
    "Mais le siège traîne et les pertes sont lourdes."
    $ situation_.AvanceDeXJours(6)
    $ _test_carac = trait.Evaluation.NOM
    $ _test_difficulte = 40
    $ _test_texte_menu = "Cette place doit bien avoir une faille."
    $ _test_texte_reussi = "Alors que vous êtes au travail au bord de l'Aisne vous en avez la certitude : en traversant le fleuve à la nage vous serez dans la position idéale pour trouver une meilleur voie d'accès."
    $ _test_label_reussi = "siege_sainte_menehould_nage"
    $ _test_label_echoue = "siege_sainte_menehould_fin"
    call _test_de_carac

label siege_sainte_menehould_nage:
    $ _test_carac = trait.Force.NOM
    $ _test_difficulte = 40
    $ _test_texte_menu = "Il faut juste nager jusqu'à l'autre côté, sous le feu ennemi certes."
    $ _test_texte_reussi = "Quelques balles sifflent aux alentours mais vous êtes bon nageur et parvenez aisément là où vous le souhaitez. Et en effet l'accès par ce côté ci sera plus aisé pour les mineurs."
    $ _test_label_reussi = "siege_sainte_menehould_nage_reussi"
    # A FAIRE : gestion  de l'échec et de la mort ??
    $ _test_label_echoue = "siege_sainte_menehould_fin"
    $ _test_abandon_possible = True
    $ _test_label_abandon = "siege_sainte_menehould_fin"
    call _test_de_carac

label siege_sainte_menehould_nage_reussi:
    "Votre courage et votre ingéniosité ne sont pas passés innaperçus. Vos officiers vous font passer sous-officier."
    $ situation_.SetValCarac(vauban.Vauban.C_GRADE, vauban.Vauban.GRADE_SOUS_OFFICIER)
    $ AjouterACarac(vauban.Vauban.C_EXPLOITS, 1)
    "On vous propose même de devenir enseigne !"
    "C'est un honneur mais cela n'est pas forcément un cadeau, car la solde est maigre et vous êtes sensé recruter et payer vos hommes vous-mêmes."
    menu:
        "Si vous acceptez":
            $ situation_.SetValCarac(vauban.Vauban.C_GRADE, vauban.Vauban.GRADE_ENSEIGNE)
            $ RetirerACarac(trait.Richesse.NOM, 1)
        "Si vous refusez":
            jump siege_sainte_menehould_fin
    jump siege_sainte_menehould_fin

label siege_sainte_menehould_fin:
    "La place est finalement capturée après quelques efforts supplémentaires."
    jump fin_cycle

label construction_clermont_en_argonne:
    scene bg siege
    with dissolve
    "Étant donné vs compétences en mathématiques et fortifications vous êtes nommé aspirant ingénieur et chargé de réparer la petite place de Clermont-en-Argonne."
    "Bien que modeste c'est une position clé sur la route de Sainte-Menehould et donc de la Champagne, c'est un honneur qu'il vous soit confié malgré votre faible expérience."
    $ _test_carac = trait.Evaluation.NOM
    $ _test_difficulte = situation_.GetValCaracInt(maitrise.Fortification.NOM) * 20
    $ _test_texte_menu = "Enfin un peu de mise en pratique."
    $ _test_texte_reussi = "Beau travail."
    $ _test_action_reussi = lambda: AjouterACarac(vauban.Vauban.C_EXPLOITS, 1)
    $ _test_texte_echoue = "Ce travail passable ne vous fait pas honneur."
    call _test_de_carac
    jump fin_cycle

label apprentissageFortification2:
    scene bg siege
    with dissolve
    "Vu vos connaissances en mathématiques les ingénieurs décident de vous incorporer à leur équipe pour renforcer les fortifications du camps."
    $ _test_carac = trait.Intelligence.NOM
    $ _test_difficulte = 20
    $ _test_texte_menu = "Enfin un peu de mise en pratique."
    $ _test_texte_reussi = "Vous vous révélez très doué et apprenez très vite."
    $ _test_action_reussi = lambda: SetValMaitrise(maitrise.Fortification.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    call _test_de_carac
    jump fin_cycle

label apprentissageMathematiques2:
    scene bg siege
    with dissolve
    "Vos lacunes en mathématiques sont un vrai frein pour que les ingénieurs vous prennent au sérieux et vous donne des missions sur le terrain."
    $ _test_carac = trait.Intelligence.NOM
    $ _test_difficulte = 0
    $ _test_texte_menu = "Vous essayez de compenser en étudiant chaque fois que vous en avez le temps."
    $ _test_texte_reussi = "Vous vous passionnez bientôt pour la topographie et essayer de comprendre quelle forme exactement a cet étrange paysage."
    $ _test_action_reussi = lambda: SetValMaitrise(maitrise.Mathematiques.NOM, maitrise.TraitMaitrise.MAITRISE_A)
    call _test_de_carac
    jump fin_cycle

label fuite_conde:
    "Le grand Condé doit fuir Paris avec le général Turenne et le roi Louis à ses trousses."
    "C'est maintenant un fugitif condamné à mort qui passe dans le camps de l'Espagne, ennemie jurée du Royaume de France."
    jump fin_cycle

label defaites_conde:
    "Les nouvelles du prince de COndé sont très mauvaises."
    "Le roi Louis a réussi à rallier Turenne, le seul général plus illustre que le prince de Condé, et celui ci l'a vaincu sévèrement."
    "Il est maintenant piégé dans Paris."
    jump fin_cycle

label mort_pere:
    "Une lettre vous apprend une triste nouvelle : votre père vient de mourir."
    "Vous pensez un moment à demander un congé mais vos supérieurs sont catégoriques : hors de question."
    "Louis XIV est maintenant majeur, il a 13 ans, et la guerre contre lui peut s'aggraver à tout moment."
    "De toute façon, vous êtes actuellement cantonné dans la Champagne."
    "Il n'y aurait aucune chance pour que vous arriviez à temps pour les obsèques dans le Morvan."
    jump fin_cycle

label debut_chapitre3:
    "Les Condé sont gouverneurs de Bourgogne et les Le Prestre font partie de leur clientèle."
    "Vous vous engagez donc comme cadet dans la compagnie du sieur d'Arcenay du régiment de Condé."
    "La situation est cependant très tendue : le Grand Condé est en rebellion quasi ouverte contre le Roi."
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 3)
    jump fin_cycle

'''
exemple d'événement répétitif complexe à garder comme exemple en attendant d'en avoir fait un dans ce projet
A FAIRE : nettoyer ça une fois qu'un événement équivalent (avec modification de proba) aura été ajouté dans Vauban
label miner_le_royaume:
    $ AfficherCarteActuelle()
    with dissolve
    # si Vauban mais ne possède pas encore le royaume de Syagrius
    $ nb_miner_le_royaume = situation_.GetValCaracInt("nb_miner_le_royaume")
    $ a_corrompu_senateurs = situation_.GetValCaracBool("a_corrompu_senateurs")
    $ a_contacte_eveque = situation_.GetValCaracBool("a_contacte_eveque")
    $ a_convaincu_chararic = situation_.GetValCaracBool("a_convaincu_chararic")
    $ a_convaincu_ragnacaire = situation_.GetValCaracBool("a_convaincu_ragnacaire")
    # tmp
    $ C_STABILITE = situation_.GetValCaracInt(syagrius.Syagrius.C_STABILITE)
    $ print("C_STABILITE : {}".format(C_STABILITE))
    $ C_MILITAIRE = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    $ print("C_MILITAIRE : {}".format(C_MILITAIRE))
    $ etatSyag = situation_.GetValCarac(syagrius.Syagrius.C_ETAT)
    $ print("etat Syagrius : {}".format(etatSyag))
    # fin tmp
    if nb_miner_le_royaume == 0:
        $ situation_.SetValCarac("nb_miner_le_royaume", 1)
        "Vos francs sont les meilleurs guerriers du monde, vous en êtes sûr. Avant même la mort de votre père vous saviez déjà que grâce à eux vous pourriez franchir la première marche qui mène à la gloire et la richesse :"
        $ AfficherCarteActuelle()
        "Conquérir le royaume romain de Syagrius."
        "Ce royaume est en apparence grand et riche mais vous savez qu'il est désuni et fragile."
        "Pour l'instant vous n'êtes pas prêt d'autant plus que Syagrius le romain est allié à Euric le puissant roi des Wisigoths. Mais votre destin est déjà tracé."

    menu:
        "Comment allez vous affaiblir Syagrius ?"
        "Convaincre votre parent, le prince franc Chararic, de vous rejoindre" if not a_convaincu_chararic:
            "Chararic accepte l'alliance mais laisse bien clair qu'il s'agit d'une alliance et pas d'une soumission : vous êtes son égal et ne serez jamais son supérieur."
            $ situation_.SetValCarac("a_convaincu_chararic", 1)
            $ AjouterACarac(vauban.Vauban.C_MILITAIRE, 1)
            jump fin_cycle
        "Chercher l'appui de Ragnacaire, le roi franc de Cambrai" if not a_convaincu_ragnacaire:
            "Ragnacaire accepte l'alliance mais laisse bien clair qu'il s'agit d'une alliance et pas d'une soumission : vous êtes son égal et ne serez jamais son supérieur."
            $ situation_.SetValCarac("a_convaincu_ragnacaire", 1)
            $ AjouterACarac(vauban.Vauban.C_MILITAIRE, 1)
            jump fin_cycle
        "Tenter de pactiser avec les sénateurs romains du territoire de Syagrius" if not a_corrompu_senateurs:
            "Les romains semblent avoir peur que vous détruisiez ce qui reste du système romain. Ils préfèrent encore Syagrius à vous et vous n'en tirez rien de bon."
            $ situation_.SetValCarac("a_corrompu_senateurs", 1)
            jump fin_cycle
        "Corrompre ses soldats":
            "Les romains sont comme les autres. Pour un peu d'or et des promesses de pillage ils vous rejoignent."
            $ RetirerACarac(syagrius.Syagrius.C_MILITAIRE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 2)
            $ AjouterACarac(vauban.Vauban.C_MILITAIRE, 1)
            jump fin_cycle
        "Tenter de gagner les faveurs des évèques" if not a_contacte_eveque:
            "À votre grande surprise les évèques vous préfèrent, vous le roi païen, aux autres barbares qui sont des chrétiens ariens hérétiques."
            "Sans doute pensent-ils pouvoir plus facilement vous convertir, vous et vos hommes. Il est vrai que vous les écoutez poliment et êtes souvent touché par leurs arguments religieux."
            "Quoiqu'il en soit, si vous envahissez le royaume ils pousseront le peuple à vous soutenir et à abandonner Syagrius."
            $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 2)
            $ situation_.SetValCarac("a_contacte_eveque", 1)
            jump fin_cycle
        "Vous contenter d'attendre le moment opportun.":
            jump fin_cycle
    jump fin_cycle
'''
