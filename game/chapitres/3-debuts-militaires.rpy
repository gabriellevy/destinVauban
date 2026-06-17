init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import vauban

    def AjouterEvtRenforcement481_485():
        global selecteur_

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
