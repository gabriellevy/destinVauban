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
            return u"Désinteressé"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Désinteressé"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Désinteressé"
        else:
            return u""

class Sobre(ViceVertu):

    NOM = u"Sobre"

    def __init__(self):
        self.eTrait_ = Sobre.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Gourmand"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Gourmand"
        elif val == ViceVertu.VICIEUX:
            return u"Gourmand"
        elif val == ViceVertu.VERTUEUX:
            return u"Sobre"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Sobre"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Sobre"
        else:
            return u""

class Cartesien(ViceVertu):

    NOM = u"Cartésien"

    def __init__(self):
        self.eTrait_ = Cartesien.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Imaginatif"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Imaginatif"
        elif val == ViceVertu.VICIEUX:
            return u"Imaginatif"
        elif val == ViceVertu.VERTUEUX:
            return u"Cartésien"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Cartésien"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Cartésien"
        else:
            return u""

class Reflechi(ViceVertu):

    NOM = u"Réfléchi"

    def __init__(self):
        self.eTrait_ = Reflechi.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Impulsif"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Impulsif"
        elif val == ViceVertu.VICIEUX:
            return u"Impulsif"
        elif val == ViceVertu.VERTUEUX:
            return u"Réfléchi"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Réfléchi"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Réfléchi"
        else:
            return u""

class Valeureux(ViceVertu):

    NOM = u"Valeureux"

    def __init__(self):
        self.eTrait_ = Valeureux.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Lâche"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Lâche"
        elif val == ViceVertu.VICIEUX:
            return u"Lâche"
        elif val == ViceVertu.VERTUEUX:
            return u"Valeureux"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Valeureux"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Valeureux"
        else:
            return u""

class Chaste(ViceVertu):

    NOM = u"Chaste"

    def __init__(self):
        self.eTrait_ = Chaste.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Luxurieux"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Luxurieux"
        elif val == ViceVertu.VICIEUX:
            return u"Luxurieux"
        elif val == ViceVertu.VERTUEUX:
            return u"Chaste"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Chaste"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Chaste"
        else:
            return u""

class Naif(ViceVertu):

    NOM = u"Naïf"

    def __init__(self):
        self.eTrait_ = Naif.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Méfiant"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Méfiant"
        elif val == ViceVertu.VICIEUX:
            return u"Méfiant"
        elif val == ViceVertu.VERTUEUX:
            return u"Naïf"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Naïf"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Naïf"
        else:
            return u""

class Artificialiste(ViceVertu):

    NOM = u"Artificialiste"

    def __init__(self):
        self.eTrait_ = Artificialiste.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Naturaliste"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Naturaliste"
        elif val == ViceVertu.VICIEUX:
            return u"Naturaliste"
        elif val == ViceVertu.VERTUEUX:
            return u"Artificialiste"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Artificialiste"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Artificialiste"
        else:
            return u""

class Travailleur(ViceVertu):

    NOM = u"Travailleur"

    def __init__(self):
        self.eTrait_ = Travailleur.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce vice-vertu n'a pas comme valeur un int. ViceVertu : {}. Valeur : {}".format(self.eTrait_, val)

        if val == ViceVertu.VICIEUX_MALADE_MENTAL:
            return u"Extrêmement Paresseux"
        elif val == ViceVertu.VICIEUX_TRES:
            return u"Très Paresseux"
        elif val == ViceVertu.VICIEUX:
            return u"Paresseux"
        elif val == ViceVertu.VERTUEUX:
            return u"Travailleur"
        elif val == ViceVertu.VERTUEUX_TRES:
            return u"Très Travailleur"
        elif val == ViceVertu.VERTUEUX_MALADE_MENTAL:
            return u"Extrêmement Travailleur"
        else:
            return u""
        