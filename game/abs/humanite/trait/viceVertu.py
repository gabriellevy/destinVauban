from game.abs.humanite.trait import trait

# Trait représentant un vice (-1 : vicieux à -3 malade mental) ou une vertu (+1 vertu à +3 : insupportable)
# à noter que les vertus sont celles d'un bon citoyen sérieux et productif : 
# ainsi être aventureux est un vice, même si certains peuvent être utilse à une société, les casaniers obéissants routiniers le sont beaucoup plus
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

class Casanier(ViceVertu):

    NOM = u"Casanier"

    def __init__(self):
        self.eTrait_ = Casanier.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Aventureux"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Aventureux"
        elif val == ViceVertu.VICIEUX:
            return u"Aventureux"
        elif val == ViceVertu.VERTUEUX:
            return u"Casanier"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Casanier"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Casanier"
        else:
            return u""

class Placide(ViceVertu):

    NOM = u"Placide"

    def __init__(self):
        self.eTrait_ = Placide.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Colérique"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Colérique"
        elif val == ViceVertu.VICIEUX:
            return u"Colérique"
        elif val == ViceVertu.VERTUEUX:
            return u"Placide"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Placide"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Placide"
        else:
            return u""

class Bienveillant(ViceVertu):

    NOM = u"Bienveillant"

    def __init__(self):
        self.eTrait_ = Bienveillant.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Cruel"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Cruel"
        elif val == ViceVertu.VICIEUX:
            return u"Cruel"
        elif val == ViceVertu.VERTUEUX:
            return u"Bienveillant"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Bienveillant"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Bienveillant"
        else:
            return u""

class Prodigue(ViceVertu):

    NOM = u"Prodigue"

    def __init__(self):
        self.eTrait_ = Prodigue.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Cupide"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Cupide"
        elif val == ViceVertu.VICIEUX:
            return u"Cupide"
        elif val == ViceVertu.VERTUEUX:
            return u"Prodigue"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Prodigue"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Prodigue"
        else:
            return u""

class Desinteresse(ViceVertu):

    NOM = u"Désinteressé"

    def __init__(self):
        self.eTrait_ = Desinteresse.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Envieux"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Envieux"
        elif val == ViceVertu.VICIEUX:
            return u"Envieux"
        elif val == ViceVertu.VERTUEUX:
            return u"Desinteresse"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Desinteresse"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Desinteresse"
        else:
            return u""
        