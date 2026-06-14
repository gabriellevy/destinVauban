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
    from chapitres.classes import germains
    from chapitres.classes import vauban

    # conditions clotilde
    decision_mariage_clotildePasFaite = condition.Condition("decision_mariage_clotilde", 1, condition.Condition.DIFFERENT)
    infos_sur_clotildePasFaite = condition.Condition("infos_sur_clotilde", 1, condition.Condition.DIFFERENT)
    infos_sur_clotildeFaite = condition.Condition("infos_sur_clotilde", 1, condition.Condition.EGAL)

    fiance_a_clotilde = condition.Condition(vauban.Vauban.C_FIANCE_CLOTHILDE, 1, condition.Condition.EGAL)
    marie_a_clotilde = condition.Condition(vauban.Vauban.C_MARIE_CLOTHILDE, 1, condition.Condition.EGAL)
    pas_marie_a_clotilde = condition.Condition(vauban.Vauban.C_MARIE_CLOTHILDE, 1, condition.Condition.DIFFERENT)

    gloireAuMoins5 = condition.Condition(trait.Gloire.NOM, 5, condition.Condition.SUPERIEUR_EGAL)

    # enfants :
    a0enfants = condition.Condition(vauban.Vauban.C_NB_ENFANTS, 0, condition.Condition.EGAL)
    a1enfants = condition.Condition(vauban.Vauban.C_NB_ENFANTS, 1, condition.Condition.EGAL)
    a2enfants = condition.Condition(vauban.Vauban.C_NB_ENFANTS, 2, condition.Condition.EGAL)
    a3enfants = condition.Condition(vauban.Vauban.C_NB_ENFANTS, 3, condition.Condition.EGAL)
    a4enfants = condition.Condition(vauban.Vauban.C_NB_ENFANTS, 4, condition.Condition.EGAL)

    def AjouterEvtsClothilde():
        global selecteur_
        # premiers echos sur Clothilde
        infos_sur_clotilde = dec_vauban.DecVaubanU(proba.Proba(0.7, True), "infos_sur_clotilde", 99999999490)
        selecteur_.ajouterDeclencheur(infos_sur_clotilde)
        # décision du mariage
        decision_mariage = dec_vauban.DecVaubanU(proba.Proba(0.7, True), "decision_mariage", 99999999492)
        decision_mariage.AjouterCondition(gloireAuMoins5)
        decision_mariage.AjouterCondition(infos_sur_clotildeFaite)
        selecteur_.ajouterDeclencheur(decision_mariage)
        # soutien de Clotilde
        soutienDeClotilde = declencheur.Declencheur(proba.Proba(0.1, True), "soutienDeClotilde")
        soutienDeClotilde.AjouterCondition(marie_a_clotilde)
        selecteur_.ajouterDeclencheur(soutienDeClotilde)
        # 2ème enfant
        enfant2 = dec_vauban.DecVaubanU(proba.Proba(0.3, True), "enfant2", 99999999495)
        enfant2.AjouterCondition(marie_a_clotilde)
        enfant2.AjouterCondition(a1enfants)
        selecteur_.ajouterDeclencheur(enfant2)
        # 3ème enfant
        enfant3 = dec_vauban.DecVaubanU(proba.Proba(0.3, True), "enfant3", 99999999497)
        enfant3.AjouterCondition(marie_a_clotilde)
        enfant3.AjouterCondition(a2enfants)
        selecteur_.ajouterDeclencheur(enfant3)
        # 4ème enfant
        enfant4 = dec_vauban.DecVaubanU(proba.Proba(0.3, True), "enfant4", 99999999498)
        enfant4.AjouterCondition(marie_a_clotilde)
        enfant4.AjouterCondition(a3enfants)
        selecteur_.ajouterDeclencheur(enfant4)
        # 5ème enfant
        enfant5 = dec_vauban.DecVaubanU(proba.Proba(0.3, True), "enfant5", 99999999500)
        enfant5.AjouterCondition(marie_a_clotilde)
        enfant5.AjouterCondition(a4enfants)
        selecteur_.ajouterDeclencheur(enfant5)

label enfant2:
    "Enfin ! Votre deuxième fils, Clodomir, est né."
    "Cette fois encore Clothilde prend l'initiative de le baptiser sans vous en informer malgré la mort d'Ingomer après son baptème il y a deux ans."
    "C'est un coup dur quand vous apprenez que Clodomir aussi est tombé malade peu de temps après son baptème."
    show clotilde at right
    with moveinright
    cl "Il ne peut pas lui arriver autre chose que ce qui est survenu à son frère ; baptisé au nom de votre Christ il mourra aussitôt."
    "Les jours qui suivent sont pénibles, vous vivez dans l'inquiétude et l'impuissance tandis que Clotilde prie du matin au soir avec ferveur."
    "Enfin, Clodomir reprend des forces et des couleurs. Il est sauvé et devient rapidement robuste. Christ n'est peut-être pas un tueur d'enfant."
    jump fin_cycle

label enfant3:
    "Votre troisième fils Childebert est né."
    jump fin_cycle

label enfant4:
    "Votre quatrième fils Clotaire est né."
    jump fin_cycle

label enfant5:
    "Votre fille Clothilde est née."
    jump fin_cycle

'''
démo tmp : arrivée d'image
label soutienDeClotilde:
    show clotilde at right
    with moveinright
    "Par sa douceur, sa bonté et sa patience Clotilde adoucit vos dures journées de roi."
    jump fin_cycle
'''

label mariage_paien:
    "PAS FAIT : mariage païen avec Clotilde"
    jump fin_cycle

label mariage_catholique:
    "PAS FAIT : mariage_catholique avec Clotilde"
    jump fin_cycle

label infos_sur_clotilde:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac("infos_sur_clotilde", 1)
    show clotilde at right
    with dissolve
    clot "A FAIRE Coucou Vauban !"
    jump fin_cycle

label decision_mariage:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac("decision_mariage_clotilde", 1)

    show clotilde at right
    with dissolve
    "Vous êtes maintenant un roi craint et renommé dans toutes la Gaulle. Un mariage prestigieux est tout ce qui vous manque pour vous hisser au niveau des grands roi germaniques."
    "L'évèque Rémi vous vante la beauté et la vertu de la princesse Clotilde, nièce du roi des burgondes Gondebaud."
    "Le fait qu'elle soit catholique est sans doute la raison pour laquelle il vous la recommande tant mais enfin il a raison : "
    "le lignage de Clotilde est ancien et prestigieux, bien supérieur au vôtre qui ne doit sa renommée qu'à la gloire militaire de votre père. Et les burgondes sont des voisins puissants dont le soutien vous serait précieux."
    menu:
        "Demandez-vous la main de Clotilde à son oncle Gondebaud ?"
        "Non. Il est hors de question d'épouser une catholique.":
            jump fin_cycle
        "Oui":
            "Vous envoyez un émissaire chargé de cadeaux pour demander la main de la princesse Clotilde."
            "Gondebaud tergiverse beaucoup car en tant que chrétien arien et surtout en tant que meurtrier des parents il a de bonnes raisons de se méfier d'elle."
            "Cependant sa position est très mauvaise entre les puissants royaumes gothiques et il n'ose pas vous opposer de refus au risque de se faire un dangereux ennemi de plus."
            "Il promet de vous envoyer Clotilde très prochainement."
            $ situation_.SetValCarac(vauban.Vauban.C_FIANCE_CLOTHILDE, 1)
    jump fin_cycle
