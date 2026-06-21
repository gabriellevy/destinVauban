init -5 python:
    import random
    from spe import dec_vauban
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from game.abs.humanite.trait import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import syagrius
    from chapitres.classes import vauban
    
    chapitre4 = condition.Condition(vauban.Vauban.CHAPITRE, 4, condition.Condition.EGAL)

    def AjouterEvtsChapitre4():
        global selecteur_
        
        dateNbJours = 1660 * 365 + 1 # ------------------------------------------------- 1660 A FAIRE : préciser date
        debut_chapitre4 = declencheur.DeclencheurDate(dateNbJours, "debut_chapitre4")
        selecteur_.ajouterDeclencheur(debut_chapitre4)
        
        dateNbJours = 1667 * 365 + 1 # ------------------------------------------------- 1667 A FAIRE : préciser date
        grade_lieutenance_aux_gardes = declencheur.DeclencheurDate(dateNbJours, "grade_lieutenance_aux_gardes")
        selecteur_.ajouterDeclencheur(grade_lieutenance_aux_gardes)

label debut_chapitre4:
    "A FAIRE : début chapitre4"
    $ situation_.SetValCarac(vauban.Vauban.CHAPITRE, 4)
    jump fin_cycle

label grade_lieutenance_aux_gardes:
    # A FAIRE : faire ça via un perso Louis XIV ou Louvois et avec plus de decorum : 
    scene bg honneur
    with dissolve
    "Le roi compte vous faire l'honneur de vous nommer Lieutenant aux gardes."
    "Cela n'est possible que pour un noble, ce que vous êtes bien sûr."
    "Mais devant la tendance des roturiers aisés à revendiquer la noblesse pour bénéficier su prestige et des exemptions fiscales, le roi a décidé de lancer des Réformations, c'est à dire des contrôles."
    "Vous êtes tenus de fournir de nombreux formulaires et documents prouvant votre ascendance."
    "Enfin, la nomination tant attendue arrive."
    $ situation_.SetValCarac(vauban.Vauban.C_GRADE, vauban.Vauban.GRADE_LIEUTENANT)
    jump fin_cycle

label invasion_syagrius:
    "Votre armée est maintenant bien avancée en territoire ennemi et vous savez que Syagrius a fini de lever la sienne."
    menu:
        "Si vous suivez la coutume franque de le défier sur le champs de bataille de son choix.":
            "Syagrius accepte le défi et choisit un champs près de sa capitale Soissons."
            "Vos hommes sont pressés d'en venir aux mains et sont heureux que vous ayez respecté les lois de Wotan. Thor et les walkyrie vous soutiendront."
            $ AjouterACarac(trait.Gloire.NOM, 1)
            $ RetirerACarac(vauban.Vauban.C_USURPATION, 1)
        "Si vous vous dirigez vers sa capitale Soissons pour l'écraser le plus tôt possible.":
            "Syagrius semble vouloir éviter un siège et vient à votre rencontre. Heureusement pour vous car la prise de ville n'est pas la spécialité de vos guerrier."
        "Si vous avancez lentement et prenez le temps de piller le pays.":
            "Les terres romaines sont bien plus riches que les vôtres. Vous faites un grand butin de richesse et d'esclaves. Vos hommes sont satisfaits."
            "Syagrius quitte Soissons pour venir vous arrêter. Heureusement pour vous car la prise de ville n'est pas la spécialité de vos guerrier."
            $ AjouterACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(syagrius.Syagrius.C_PILLAGE, 2)
            $ RetirerACarac(vauban.Vauban.C_USURPATION, 1)
    $ situation_.AvanceDeXMois(2)
    jump bataille_soisson

label bataille_soisson:
    scene bg morvan
    with dissolve
    $ puissanceArmeeSyagrius = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    "{b}Bataille de Soissons.{/b}"
    "Syagrius a rangé son armée de manière ordonnée à la romaine. Mais la discipline apparente ne vous impressionne pas. La plupart des soldats sont des germains qui combattront sans grand entousiasme."
    menu:
        "D'où allez vous combattre ?"
        "Au premier rang !":
            jump bataille_soisson_combat
        "En soutien au second rang.":
            "Vous faites avancer votre armée en bon ordre. Les soldats sont motivés par votre présence et veulent se faire remarquer par leur bravoure."
            $ testCombat = testDeCarac.TestDeCarac([vauban.Vauban.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
            menu:
                "Les romains se préparent au choc. [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Vos hommes dominent si bien la bataille que votre première ligne semble suffire à repousser les romains."
                        jump bataille_soisson_2
                    else:
                        "La première ligne est enfoncée. Vous allez devoir aller au contact avec votre garde d'honneur pour la soutenir."
                        jump bataille_soisson_combat

        "En retrait pour avoir une vue d'ensemble et rester en sécurité.":
            "De puis une petite colline vous donnez vos ordres pour faire avancer votre infanterie."
            "Vos soldats obéissent restent confiants et disciplinés mais il est clair qu'ils apprécient peu que le descendant des dieux que vous êtes reste à l'arrière."
            $ AjouterACarac(vauban.Vauban.C_USURPATION, 1)
            $ RetirerACarac(trait.Gloire.NOM, 1)
            $ testCombat = testDeCarac.TestDeCarac([vauban.Vauban.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
            menu:
                "Les romains se préparent au choc. [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Vos hommes dominent si bien la bataille que votre première ligne semble suffire à repousser les romains."
                        jump bataille_soisson_2
                    else:
                        "Les pertes sont lourdes mais vos soldats sont meilleurs et plus motivés. Ils prennent l'avantage."
                        $ RetirerACarac(vauban.Vauban.C_MILITAIRE, 1)
                        jump bataille_soisson_2

    label bataille_soisson_combat:
        "Vous formez un groupe compact avec l'élite de vos hommes et avancez droit sur le centre ennemi."
        "Les romains tentent de rester en formation serrée avec leur boucliers levés. Vous ordonnez alors à vos hommes de lancer leurs lourds javelots à crochet."
        "La plupart sont bloqués par les boucliers ennemis mais ils sont si lourds et solides que les romains ne peuvent plus manoeuvrer et peinent à lever leurs boucliers."
        $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 4, situation_)
        menu:
            "C'est le moment de lancer une charge complète.[testCombat.affichage_]":
                $ reussi = testCombat.TesterDifficulte(situation_)
                if not reussi:
                    "Alors que vous atteignez les lignes ennemies un javelot bien lancé vous frappe en plein visage. Votre court règne s'arrête ici."
                    jump mort
                else:
                    "Vous avez repéré un officier empêtré par un javelot dans son bouclier. Vous écartez le bouclier d'un coup de pied dans le javelot et poignardez facilement son corps découvert avec votre scramasax."
                    $ AjouterACarac(trait.Gloire.NOM, 1)
                    $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 7, situation_)
                    menu:
                        "Enhardi vous vous jetez en avant en chantant à la gloire de Wotan.[testCombat.affichage_]":
                            $ reussi = testCombat.TesterDifficulte(situation_)
                            if reussi:
                                "Vous empoignez votre francisque et faites un grand massacre des romains terrifiés et désordonnés."
                                $ AjouterACarac(trait.Gloire.NOM, 1)
                                jump bataille_soisson_2
                            else:
                                "Vous avez été repéré et une volée de javelot s'abat sur vous. Votre bouclier tient le choc mais les pointent le traversent et s'arrêtent à un doigt de votre visage."
                                "Sous le choc, vous êtes heureusement secourus par vos fidèles gardes du corps qui couvrent votre corps de leurs boucliers."
                                jump bataille_soisson_2

    jump bataille_soisson_2

label bataille_soisson_2:
    scene bg morvan
    with dissolve
    $ puissanceArmeeSyagrius = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    $ a_convaincu_chararic = situation_.GetValCaracBool("a_convaincu_chararic")
    if a_convaincu_chararic:
        "Voyant que l'armée ennemie faiblit vous constatez que votre parent Chararic, qui devait vous soutenir avec sa cavalerie, n'intervient pas."
        "Impossible de s'occuper de lui pour l'instant, mais il ne perd rien pour attendre."
        $ RetirerACarac(vauban.Vauban.C_MILITAIRE, 1)

    $ testCombat = testDeCarac.TestDeCarac([vauban.Vauban.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
    menu:
        "Les romains sont prêts à céder."
        "C'est le moment de faire donner les réserves de cavalerie.[testCombat.affichage_]":
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                "Les romains n'avaient plus besoin que de ce choc pour fuir en désordre. Votre cavalerie en massacre un grand nombre durant leur fuite."
            else:
                "Les romains s'obstinent à résister et il faut des heures pour que finalement, brisés de fatigue ils succombent."
                $ RetirerACarac(vauban.Vauban.C_MILITAIRE, 1)
    "Pas trace de Syagrius quand vous pénétrez en arme dans sa capitale Soissons sans que personne n'essaye de vous résister. Soit il est mort, soit il a fui. C'est de toute façon une victoire écrasante dont il ne se remettra pas."
    $ AjouterACarac(trait.Gloire.NOM, 1)
    $ situation_.SetValCarac(vauban.Vauban.CARTE_ACTUELLE, "bg carte486")
    $ AfficherCarteActuelle()
    "Vous vous emparez d'une grande partie de son territoire et en particulier de Reims, Soissons et Paris."
    jump fin_cycle # vase_de_soissons

'''
A FAIRE : gardercet evt comme modèle d'evt complexe tant que nécessaire :
label vase_de_soissons:
    "La ville de Soissons est pillée de fond en comble et vous en tirez, vous et vos hommes, de grandes richesses. En particulier du palais de Syagrius et des églises."
    "Une délégation de prêtres catholiques menés par un évèque vient cependant vous demander humblement de leur restituer un grand et magnifique vase sacré."
    "La règle franque veut que la distribution du butin soit tirée au sort. En tant que roi un cinquième doit vous revenir."
    "Vous n'êtes donc pas sûr de recevoir le vase. Mais il ne s'agit que d'un vase et, en roi victorieux, vous pouvez vous permettre d'exceptionnellement prendre ce vase malgré la règle."
    menu:
        "Que faites vous ?"
        "Refuser et renvoyer l'évèque":
            $ RetirerACarac(vauban.Vauban.C_CHRISTIANISME, 1)
        "Accepter mais seulement si le sort vous accorde le vase.":
            $ unACinq = random.randint(1,5)
            if unACinq == 1:
                "Par chance le tirage au sort vous donne le vase. Vous le rendez aux prêtres qui vous sont très reconnaissants."
                jump fin_cycle
            else:
                "Le tirage au sort ne vous donne pas le vase sacré. Les prêtres repartent les mains vides."
                $ RetirerACarac(vauban.Vauban.C_CHRISTIANISME, 1)
                jump fin_cycle
        "Demander à vos soldats de vous laisser ce vase hors part.":
            "Arrivant à Soissons où toute la masse du butin avait été placée au milieu, vous dites : "
            cl "Je vous prie, ô très valeureux guerriers, de ne pas vous opposer à ce que me soit concédé hors part ce vase."
            "A ces mots ceux qui avaient l'esprit sain répliquent : "
            "{i}Tout ce que nous voyons ici, glorieux Roi, est à toi et nous mêmes sommes soumis à ta domination. Fais donc maintenant ce qui convient à ton bon plaisir.{/i}"
            "Or après qu'ils eurent parlé ainsi, un homme léger, jaloux et frivole, ayant levé sa hache, frappa le vase en criant à voix forte : "
            "{i}Tu n'auras rien ici que ce que le sort t'attribuera vraiment !{/i}"
            $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 5, situation_)
            menu:
                "C'est ce que dit la loi mais un tel affront vous rend furieux."
                "le faire exécuter":
                    "Vos hommes vous obéissent et le misérable est décapité sous vos yeux. Vous voyez bien néanmoins que c'est par peur qu'on vous obéit et que votre mépris des coutumes rend furieux plus d'un franc."
                    $ AjouterACarac(vauban.Vauban.C_USURPATION, 3)
                "L'attaquer immédiatement [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Le combat ne dure qu'un instant. Vous fendez le crâne du misérable à coup de hache et il s'effondre au milieu du butin et de vos hommes ébahis."
                        $ AjouterACarac(trait.Gloire.NOM, 1)
                        "Vous voyez bien néanmoins que c'est par peur qu'on vous obéit et que votre mépris des coutumes rend furieux plus d'un homme."
                        $ AjouterACarac(vauban.Vauban.C_USURPATION, 2)
                    else:
                        "Malgré sa surprise le soldat réagit à la vitesse de l'éclair et sous les yeux de vos hommes ébahis il vous poignarde en plein coeur avec sa scramasaxe."
                        "Mourir de la main de ses propres hommes pour une bête histoire de partage du butin. Quelle fin misérable pour celui qui aurait pu être un grand roi."
                        jump mort
                "Accepter de suivre la coutume":
                    $ situation_.SetValCarac(vauban.Vauban.C_VASE_SOISSONS, 1)
                    "Vous parvenez à contenir votre ressentiment avec une douce patience."
                    "Au moins, le vase qui est en métal n'a pas été brisé et le tirage au sort vous le donne. Ce qui vous permet de le rendre aux envoyés de l'évèque."

    "En prenant en compte les propriétés que vous avez saisies votre part de butin est colossale. Vous n'avez jamais été aussi riche."
    $ AjouterACarac(trait.Richesse.NOM, 6)
    "Vos hommes se sont aussi considérablement enrichis et vous sont plus fidèles que jamais."
    $ RetirerACarac(vauban.Vauban.C_USURPATION, 2)
    $ situation_.SetValCarac(vauban.Vauban.CARTE_ACTUELLE, "bg carte481")
    $ AfficherCarteActuelle()
    "Votre royaume est agrandi sans compter que sans Syagrius les terres vers l'ouest seront sans doute très peu défendues."
    jump fin_cycle
'''
