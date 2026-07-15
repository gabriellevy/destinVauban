# label pour inifier les tests de carac
# Utilisation : il faut setter toutes les variables suivantes avec d'appeelr le label : 
# $ _test_carac = trait.Mouvement.NOM
# $ _test_difficulte = 20 # 20 est une difficulté standard, simple pour un professionnel
# $ _test_texte_menu = "Comme tout gentilhomme qui se respecte vous prenez très tôt beaucoup de leçons d'équitation."
# $ _test_texte_reussi = "Vous progressez vite."
# $ _test_texte_echoue = "Ce n'est pas votre fort."
# $ _test_action_reussi = lambda: SetValCaracInt(trait.Equitation.NOM, maitrise.TraitMaitrise.MAITRISE_A)
# $ _test_action_echoue = None
# $ _test_label_reussi = "grade_ordre_saint_louis2"
# $ _test_label_echoue = "grade_ordre_saint_louis2"
# $ _test_abandon_possible = False
# $ _test_label_abandon = None
# $ _label_ressurection = "fin_cycle" # label appelé si le perso meurt mais est sauvé par un point de destin

label _test_de_carac:
    $ testCombat = testDeCarac.TestDeCarac(_test_carac, _test_difficulte, situation_)
    menu:
        "[_test_texte_menu][testCombat.affichage_]":
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                jump _test_de_carac_reussi
            else:
                # si le joueur a un point de destin il peut réussir automatiquement
                $ nbDestin = situation_.GetValCaracInt(trait.Destin.NOM)
                if nbDestin > 0:
                    menu:
                        "Raté ! Dépensez vous un point de destin pour réussir ?":
                            $ RetirerACarac(trait.Destin.NOM, 1)
                            jump _test_de_carac_reussi
                        "Ou acceptez vous l'échec":
                            jump _test_de_carac_echec
                else:
                    jump _test_de_carac_echec
        "Renoncer" if _test_abandon_possible:
            if _test_label_abandon:
                $ renpy.jump(_test_label_abandon)
            else:
                jump fin_cycle
    return

label _test_de_carac_echec:
    "[_test_texte_echoue]"
    if _test_action_echoue:
        $ _test_action_echoue()
    if _test_label_echoue:
        $ renpy.jump(_test_label_echoue)
    else:
        jump fin_cycle

label _test_de_carac_reussi:
    "[_test_texte_reussi]"
    if _test_action_reussi:
        $ _test_action_reussi()
    if _test_label_reussi:
        $ renpy.jump(_test_label_reussi)
    else:
        jump fin_cycle
