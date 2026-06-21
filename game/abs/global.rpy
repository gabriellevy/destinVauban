init -2 python:
    from abs import carac
    # from spe import situation_fondateur
    from game.abs.humanite.trait import trait
    # from geographie import quartier
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite.sante import pbsante
    # from spe.peuple import peuple
    # from spe.region import region
    # from spe.civilisation import civ
    import random

    # text fade system
    time_ = 2.0 # seconds of fade
    x_debut = 100
    y_debut = 10
    x_fin = 650
    y_fin = 10

    # affiche la description de la maîtrise concernée au lieu de juste un chiffre
    def SetValMaitrise(nomMaitrise, num):
        global situation_
        valCourant = situation_.GetValCaracInt(nomMaitrise)
        if num > valCourant:
            situation_.AjouterACarac(nomMaitrise, num - valCourant)
            textChangtCarac = u"{}".format(situation_.collectionTraits[nomMaitrise].GetDescription(situation_))
            renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#4f4", size=24, alpha=1.0)
            renpy.pause(time_)
            renpy.hide_screen("fading_text")
        elif num < valCourant:
            situation_.AjouterACarac(nomMaitrise, num - valCourant)
            textChangtCarac = u"{}".format(situation_.collectionTraits[nomMaitrise].GetDescription(situation_))
            renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#e11", size=24, alpha=1.0)
            renpy.pause(time_)
            renpy.hide_screen("fading_text")
            situation_.RetirerACarac(nomMaitrise, num)

    def SetValCarac(caracId, num):
        global situation_
        valCourant = situation_.GetValCaracInt(caracId)
        if num > valCourant:
            AjouterACarac(caracId, num - valCourant)
        elif num < valCourant:
            RetirerACarac(caracId,num - valCourant)

    def AjouterACarac(caracId, num):
        global situation_
        textChangtCarac = u"{} + {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#4f4", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.AjouterACarac(caracId, num)

    def GetValCarac(caracId):
        """
        simple raccourci
        """
        global situation_
        return situation_.GetValCarac(caracId)

    def GetValCaracInt(caracId):
        """
        simple racourci
        """
        global situation_
        return situation_.GetValCaracInt(caracId)

    def RetirerACarac(caracId, num):
        global situation_
        textChangtCarac = u"{} - {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#e11", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.RetirerACarac(caracId, num)

    def InterfaceSuivante():
        global interfaceMode_, nbInterfaceMode_
        interfaceMode_ = interfaceMode_ + 1
        if interfaceMode_ >= nbInterfaceMode_:
            interfaceMode_ = 0
        print(interfaceMode_)
