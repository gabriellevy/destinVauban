define config.menu_include_disabled = True
define gui.choice_button_text_insensitive_color = "#555"

# Persos
define narrator = Character(color="#fafad8", what_italic=True)
define std = Character('Perso standard...', color="#B22222") # personnage standard remplacé selon les situations. (son nom est mis à jour)
define cl = Character('Vauban', color="#001ba4")

define boileau = Character('Boileau', color="#39055e")

image louisXIV = "perso/louisXIV.png"
define louisXIV = Character('Louis XIV', color="#003ae7")

# A FAIRE : maj les perso pour ajouter Louis XIV, Louvois etc
image clotilde = "perso/clotilde.png"
define clot = Character('Clotilde', color="#800000")

image alboflede = "perso/alboflede.png"
define albo = Character('Alboflède', color="#33cc33")

image gondebaud = "perso/gondebaud.png"
define gond = Character('Gondebaud', color="#006600")

# Musiques
define audio.turexgloriae = "musique/turexgloriae.ogg" # baptème etc
# Musiques de fnd qui tournent en boucle : 
# A FAIRE : remplacer ces muriques par quelque chose d'adapté au XVIIème siècle et de peinard
define audio.christ1 = "musique/journeytoabsolution.ogg"
define audio.youpi_paien = "musique/Quite An Adventure.ogg"
define audio.printemps = "musique/Sea Season.ogg"
define audio.hiver = "musique/Dark Season.ogg"
define audio.ete = "musique/Fire Season.ogg"

init -10 python:
    from abs import selecteur
    import random

    selecteur_ = selecteur.Selecteur()

init -1 python:
    from abs import selecteur
    from chapitres.classes import syagrius
    import random

    # valeurs de bases à initialiser : 
    exploits = 5

    # chapitres
    AjouterEvtJeunesse()
    # autres
    AjouterEvtsProfessionnels()
    AjouterEvtsRoi()
    # usurpation désactivée pour l'instant. Je le remettrai si je vois une application liée à Vauban mais rien pour l'instant
    # AjouterEvtsUsurpation()
    AjouterEvtsRien()
    # AjouterEvtRenforcement481_485()
    AjouterEvtEtudes()
    AjouterEvtsChapitre4()
    AjouterEvtBurgondes()
    AjouterEvtsClothilde()
    AjouterEvtVagabondDuRoi()
    AjouterEvts8Summum()
    AjouterEvtsMarechalImportun()
    AjouterEvtsHistoire()
    AjouterEvtsFamille()

# Le jeu commence ici
label start:
    scene bg priere
    # remise à None de toutes les variables globals de tests
    $ _test_carac = None
    $ _test_difficulte = None
    $ _test_texte_menu = None
    $ _test_texte_reussi = None
    $ _test_texte_echoue = None
    $ _test_action_reussi = None
    $ _test_action_echoue = None
    $ _test_label_reussi = None
    $ _test_label_echoue = None
    # play music musique_menu
    queue music [ printemps, hiver, ete ] # pseudo liste de lecture temporaire
    jump naissance

label debut_cycle:
    show screen valeurs_traits

    $ situation_.TourSuivant()
    $ prochainEvt = selecteur_.determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

label fin_cycle:
    # Fin d'un cycle. remet tout à zéro avant d'en recommencer un
    # jump loi_gombette # tmp test
    
    # remise à None de toutes les variables globals de tests
    $ _test_carac = None
    $ _test_difficulte = None
    $ _test_texte_menu = None
    $ _test_texte_reussi = "Réussi !"
    $ _test_texte_echoue = "Raté !"
    $ _test_action_reussi = None
    $ _test_action_echoue = None
    $ _test_label_reussi = None
    $ _test_label_echoue = None

    if situation_["Santé"] != "Mort":
        jump debut_cycle

label mort:
    menu:
        "Vous êtes mort."
        "ok":
            pass
        # A FAIRE : comment quitter le jeu ??
    return

label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"

label probaAbsoluesSup100:
    "Le total des probas absolues dépasse 100%% !"
