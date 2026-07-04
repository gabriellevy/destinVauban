from game.abs.humanite.trait import trait

# Trait représentant un vice (-1 : vicieux à -3 malade mental) ou une vertu (+1 vertu à +3 : insupportable)
class ViceVertu(trait.Trait):
    # seuils de maîtrises
    VICIEUX_MALADE_MENTAL = -3
    VICIEUX_TRES = -2
    VICIEUX = -1
    VERTUEUX = 1
    VERTUEUX_TRES = 2
    VERTUEUX_MALADE_MENTAL = 3

    NOM = u"ViceVertu"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description ViceVertu" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

    def GetValeurALaNaissance(self):
        return 0
    
class Humble(ViceVertu):

    NOM = u"Cupidité"

    def __init__(self):
        self.eTrait_ = Humble.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Orgueilleux"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Orgueilleux"
        elif val == ViceVertu.VICIEUX:
            return u"Orgueilleux"
        elif val == ViceVertu.VERTUEUX:
            return u"Humble"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Humble"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Humble"
        else:
            return u""
