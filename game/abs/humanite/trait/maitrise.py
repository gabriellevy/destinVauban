from game.abs.humanite.trait import trait

# -------------------------------------- Maîtrise -----------------------------------------------------
# Trait représentant la maîtrise d'un domaine particulier 
class TraitMaitrise(trait.Trait):
    # seuils de maîtrises
    MAITRISE_A_PAS = 0      # normal, ne connaît pas, niveau de tout le monde par défaut
    MAITRISE_A = 1          # se débrouille
    MAITRISE_EXPERT = 2     # professionnel exceptionnel
    MAITRISE_LEGENDAIRE = 3 # maîtrise suprême, ne fait même plus de test car il réussit toujours tout

    NOM = u"TraitMaitrise"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitMaitrise" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

    def GetValeurALaNaissance(self):
        return 0

class Architecture(TraitMaitrise):

    NOM = u"Architecture"

    def __init__(self):
        self.eTrait_ = Architecture.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Notions en Architecture"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Architecte"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Expert Architecte"
        else:
            return u""

class Equitation(TraitMaitrise):

    NOM = u"Équitation"

    def __init__(self):
        self.eTrait_ = Equitation.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u"Ne sait pas monter à cheval"
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Cavalier correct"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Bon cavalier"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Cavalier exceptionnel"
        else:
            return u""

class Mathematiques(TraitMaitrise):

    NOM = u"Mathématiques"

    def __init__(self):
        self.eTrait_ = Mathematiques.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Débutant en mathématiques"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Mathématicien"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Expert mathématicien"
        else:
            return u""

class Fortification(TraitMaitrise):

    NOM = u"Fortification"

    def __init__(self):
        self.eTrait_ = Fortification.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Notions en Fortification"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Expert en Fortification"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Maître des fortification"
        else:
            return u""

class Hydraulique(TraitMaitrise):

    NOM = u"Hydraulique"

    def __init__(self):
        self.eTrait_ = Hydraulique.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Notions en Hydraulique"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Expert en Hydraulique"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Maître de l'Hydraulique"
        else:
            return u""

class Poliorcetique(TraitMaitrise):

    NOM = u"Poliorcétique"

    def __init__(self):
        self.eTrait_ = Poliorcetique.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Notions en Poliorcétique"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Expert en Poliorcétique"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Maître de l'Poliorcétique"
        else:
            return u""

class Strategie(TraitMaitrise):

    NOM = u"Stratégie militaire"

    def __init__(self):
        self.eTrait_ = Strategie.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Notions en Stratégie militaire"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Stratège"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Maître de Stratège"
        else:
            return u""

class Carthographie(TraitMaitrise):

    NOM = u"Carthographie"

    def __init__(self):
        self.eTrait_ = Carthographie.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val == TraitMaitrise.MAITRISE_A:
            return u"Notions en Carthographie"
        elif val == TraitMaitrise.MAITRISE_EXPERT:
            return u"Carthographe"
        elif val == TraitMaitrise.MAITRISE_LEGENDAIRE:
            return u"Maître en Carthographie"
        else:
            return u""

class Espagnol(TraitMaitrise):

    NOM = u"Espagnol"

    def __init__(self):
        self.eTrait_ = Espagnol.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Maîtrise : {}. Valeur : {}".format(self.eTrait_, val)

        if val == TraitMaitrise.MAITRISE_A_PAS:
            return u""
        elif val >= TraitMaitrise.MAITRISE_A:
            return u"Parle Espagnol"
        else:
            return u""
   