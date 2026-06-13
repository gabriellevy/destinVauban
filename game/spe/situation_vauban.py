from abs.religions import religion
from chapitres.classes import syagrius
from chapitres.classes import vauban
from spe.humanite import portrait_roi_vauban
from abs.humanite import portrait
from spe.humanite import pnj_roi_vauban
from abs import situation
from abs.humanite import metier
from abs.humanite import pnj
from abs.humanite import trait
import random

class SituationVauban(situation.Situation):

    def __init__(self):
        dateNbJours = 4*30 + 1646 * 365 + 1 # 1er mai 1633 + 13
        situation.Situation.__init__(self, dateNbJours)

    # ------------------------------------------------AFFICHAGE---------------------------------------
    def AffichageArmee(self):
        global debug_
        # armée de vauban
        str = u""
        val = self.GetValCaracInt(vauban.Vauban.C_MILITAIRE)
        if val <= 0:
            str = u"" # pas d'armée
        elif val <= 2:
            str = u"Armée faible"
        elif val <= 4:
            str = u"Bonne armée"
        elif val <= 7:
            str = u"Armée puissante"
        elif val <= 10:
            str = u"Armée redoutable"
        else:
            str = u"Armée invincible"
        if self.debug_:
            return u"{} ({})".format(str, val)
        return str
    
    def AffichageGloire(self):
        if self.debug_:
            return u"Gloire : {}".format(val)
        return self.collectionTraits[trait.Gloire.NOM].GetDescription(self)

    def AffichageUsurpation(self):
        val = self.GetValCarac(vauban.Vauban.C_USURPATION)
        if self.debug_:
            return u"Risques d'usurpation : {}".format(val)
        return u""

    def AffichageRichesse(self):
        strRichesse = self.collectionTraits[trait.Richesse.NOM].GetDescription(self)
        if ( trait.Richesse.NOM not in self.caracs_):
            if self.debug_:
                strRichesse = u"Riche (0)"
            strRichesse = u"Riche"

        val = self.GetValCarac(trait.Richesse.NOM)
        if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
            strRichesse = u"Misérable" # val <= -13
        elif val <= -8:
            strRichesse = u"Pauvre" # -8 >= val > -13
        elif val <= trait.Trait.SEUIL_A_PAS:
            strRichesse = u"En difficulté financière" # -3 >= val > -8
        elif val <= trait.Trait.SEUIL_A:
            strRichesse = u"Riche" # 1 >= val > -3
        elif val <= 6:
            strRichesse = u"Très Riche" # 6 >= val > 1
        elif val <= trait.Trait.SEUIL_A_EXTREME:
            strRichesse = u"Incroyablement riche" # 11 >= val > 1
        else:
            strRichesse = u"Fabuleusement riche" # val > 11

        if strRichesse == "":
            strRichesse = u"Riche"
        if self.debug_:
            strRichesse = u"{} ({})".format(strRichesse, self.collectionTraits[trait.Richesse.NOM].GetVal(self))
        return strRichesse

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_roi_vauban.PortraitRoiVauban()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self, True)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    # -------------------------------------------------- temps -------------------------------------------------

    def TourSuivant(self):
        """
        Passage au "tour" suivant c'est à dire grosso modo à un mois et demi un peu randomisé
        """
        nbJoursPasses = 38 + random.randint(0, 20)
        self.AvanceDeXJours(nbJoursPasses)
