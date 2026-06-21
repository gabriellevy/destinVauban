import random

"""
A FAIRE : convertir tout ça en caractéristiques brigandyne/warhammer
"""
class Trait(object):
    """
    ce qui a rapport aux traits descriptif d'un personnage. Ils peuvent aussi bien être psychologiques que physiques.
    Tous ces traits sont définis par des entiers mais ils sont de plusieurs types : 
    - Souvent ils sont binaires par souci de simplification (0 oumoins signifie pas de trait, 1 ou plus signifie possède le trait)
    - les maîtrises peuvent avoir des valeurs de 0 (n'y connaît rien) à 3 (maître légendaires)
    - les compétences vont de 1 à 100
    - les vices et vertus qui vont de -3 à 3
    """

    # A FAIRE : supprimer les 4 seuils suivants
    SEUIL_A = 1 # valeur à partir de laquelle (et au dessus) on est considéré comme ayant le trait
    SEUIL_A_EXTREME = 11 # valeur à partir de laquelle (et au dessus) on est considéré comme ayant le trait à un niveau héroïque
    SEUIL_A_PAS = -3 # valeur à partir de laquelle (et en dessous) on est considéré comme ayant le trait en négatif
    SEUIL_A_PAS_EXTREME = -13 # valeur à partir de laquelle (et en dessous) on est considéré comme ayant le trait en très très négatif

    # seuils de caracs
    CARAC_TRES_FAIBLE = 15
    CARAC_FAIBLE = 25 # personne normale quand très jeune
    CARAC_NORMAL = 35
    CARAC_ELEVE = 50
    CARAC_EXCEPTIONNEL = 70
    CARAC_EXTREME = 100

    def __init__(self, eTrait):
        self.eTrait_ = eTrait # enum Trait qui servira à identifier le trait pour lui affecter des caracs secondaires

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)
        return "Valeur de description non trouvée pour : Trait : {}. Valeur : {}".format(self.eTrait_, val)

    def GetVal(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        return val

    def PeutEtrePrisALaNaissance(self):
        """
        Renvoie true si il s'agit d'un trait qui peut être choisi dès la création du personnage
        Renvoie false si c'est un trait uniquement 'acquis'
        """
        return True

    def GetValeurALaNaissance(self):
        """
        Doit être overridée
        """
        return -99999

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Trait : {}".format(self.eTrait_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{}".format(self.eTrait_)

class TraitBinaire(Trait):

    NOM = u"TraitBinaire"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitBinaire" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

    def GetValeurALaNaissance(self):
        return 1

class TraitTernaire(Trait):

    NOM = u"TraitTernaire"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitTernaire" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

    def GetValeurALaNaissance(self):
        """
        50% de chance en négatif, 50% de chance en positif
        """
        if random.randint(0,1) == 0:
            return Trait.SEUIL_A_PAS
        else:
            return Trait.SEUIL_A

# Trait graduel == compétence qui va de 1 à 100
class TraitGraduel(Trait):

    NOM = u"TraitGraduel"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitGraduel" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

    def GetValeurALaNaissance(self):
        return random.randint(0,10) + random.randint(0,10) + 20

class Destin(Trait):

    NOM = u"Destin"

    def __init__(self):
        self.eTrait_ = Destin.NOM

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        val = situation[self.eTrait_]
        if val == "":
            val = self.GetValeurALaNaissance()
            situation[self.eTrait_] = val
        return u"Destin : {}".format(val)

    def GetValeurALaNaissance(self):
        return 5

# -------------------------------------- Vice et vertus -----------------------------------------------------
# Trait représentant un vice (-1 : vicieux à -3 malade mental) ou une vertu (+1 vertu à +3 : insupportable)
class ViceVertu(Trait):
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
    
class Cupidite(TraitTernaire):

    NOM = u"Cupidité"

    def __init__(self):
        self.eTrait_ = Cupidite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Prodigue"
        elif val >= Trait.SEUIL_A:
            return u"Cupide" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Franchise(TraitTernaire):

    NOM = u"Franchise"

    def __init__(self):
        self.eTrait_ = Franchise.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Sournois"
        elif val >= Trait.SEUIL_A:
            return u"Franc" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

# intellectuel, // intelligent à priori mais a surtout tendance à intellectualiser tout, à conceptualiser, à aimer l'abstrait et la discussion
# à l'inverse les pragmatiques ne voient que le concret et l'action. Peut être intelligent mais tendace à utiliser son intelligence de manière concrère et direct : plutôt terre à terre
class Intellectualisme(TraitTernaire):

    NOM = u"Intellectualisme"

    def __init__(self):
        self.eTrait_ = Intellectualisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Pragmatique"
        elif val >= Trait.SEUIL_A:
            return u"Intellectuel" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Pragmatisme(TraitTernaire):

    NOM = u"Pragmatisme"

    def __init__(self):
        self.eTrait_ = Pragmatisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Idéaliste"
        elif val >= Trait.SEUIL_A:
            return u"Pragmatique" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Prudence(TraitTernaire):

    NOM = u"Prudence"

    def __init__(self):
        self.eTrait_ = Prudence.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Aventureux"
        elif val >= Trait.SEUIL_A:
            return u"Prudent" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Patriarcat(TraitTernaire):

    NOM = u"Rapport entre les sexes"

    def __init__(self):
        self.eTrait_ = Patriarcat.NOM

    def PeutEtrePrisALaNaissance(self):
        return False

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Matriarcal"
        elif val >= Trait.SEUIL_A:
            return u"Patriarcal" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Serenite(TraitTernaire):

    NOM = u"Sérénité"

    def __init__(self):
        self.eTrait_ = Serenite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Angoissé"
        elif val >= Trait.SEUIL_A:
            return u"Serein" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Opportunisme(TraitBinaire):

    NOM = u"Opportunisme"

    def __init__(self):
        self.eTrait_ = Opportunisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val >= Trait.SEUIL_A:
            return u"Opportuniste"
        else:
            return ""

class Observation(TraitTernaire):

    NOM = u"Sens de l'observation"

    def __init__(self):
        self.eTrait_ = Observation.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Distrait"
        elif val >= Trait.SEUIL_A:
            return u"Observateur" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Spiritualite(TraitTernaire):

    NOM = u"Spiritualité"

    def __init__(self):
        self.eTrait_ = Spiritualite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Matérialiste"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Mystique"
            return u"Spirituel" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Nature(TraitTernaire):
    """
    Aime la nature, s'y sent bien, s'y débrouille bien
    """

    NOM = u"Nature"

    def __init__(self):
        self.eTrait_ = Nature.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Antinaturaliste "
        elif val >= Trait.SEUIL_A:
            return u"Naturophile " # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

# Suit un code de l'honneur, ou agit par instinct (différence entre Loyal et Chaotique)
# respecte ses pairs et sa famille...
class Honorabilite(TraitGraduel):

    NOM = u"Honorabilité"

    def __init__(self):
        self.eTrait_ = Honorabilite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Chaotique"
            return u"Instinctif"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Très Honorable"
            return u"Honorable"
        else:
            return ""

# prends très au sérieux sa réputation, ne ment jamais
# inclut aussi la sincérité vs l'hypocrisie etc
class Sincerite(TraitGraduel):

    NOM = u"Sincérité"

    def __init__(self):
        self.eTrait_ = Sincerite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Mythomane"
            return u"Menteur"
        elif val >= Trait.SEUIL_A:
            return u"Sincère"
        else:
            return ""

class ArmesCorpsACorps(TraitGraduel):

    NOM = u"Armes de Corps à Corps"

    def __init__(self):
        self.eTrait_ = ArmesCorpsACorps.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Très mauvais combattant"
            return u"mauvais combattant"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Maître d'armes"
            return u"Combattant exceptionnel"
        else:
            return ""
        
class Tir(TraitGraduel):

    NOM = u"Tir"

    def __init__(self):
        self.eTrait_ = Tir.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Très mauvais tireur"
            return u"mauvais tireur"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Tireur d'élite"
            return u"Excellent tireur"
        else:
            return ""
        
class Eloquence(TraitGraduel):

    NOM = u"Éloquence"

    def __init__(self):
        self.eTrait_ = Eloquence.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Incohérent"
            return u"Balbutiant"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Très éloquent"
            return u"Éloquent"
        else:
            return ""

class Intelligence(TraitGraduel):

    NOM = u"Intelligence"

    def __init__(self):
        self.eTrait_ = Intelligence.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Stupide"
            return u"Bête"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Surdoué"
            return u"Intelligent"
        else:
            return ""

class Volonte(TraitGraduel):

    NOM = u"Volonté"

    def __init__(self):
        self.eTrait_ = Volonte.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Poltron"
            return u"Lâche"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Courageux"
            return u"Imperurbable"
        else:
            return ""

class Assurance(TraitGraduel):
    """
    plus ou moins confiance du personnage en lui-même
    caractéristique très variable
    a des effets sur le charme et la mise en avant du personnage par exemple
    """

    NOM = u"Assurance"

    def __init__(self):
        self.eTrait_ = Assurance.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Aucune confiance en lui"
            return u"Doute de lui"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Sûr de lui"
            return u"Confiant"
        else:
            return ""

class Altruisme(TraitGraduel):

    NOM = u"Altruisme"

    def __init__(self):
        self.eTrait_ = Altruisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Cruel"
            return u"Égoïste"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Altruiste"
            return u"Généreux"
        else:
            return ""

# Est-ce que le personnage est indivisualiste ou est-ce qu'il aime agir en groupe
# estt-ce qu'il est prêt à se sacrifier pour les autres ?..
class Individualisme(TraitGraduel):

    NOM = u"Altruisme"

    def __init__(self):
        self.eTrait_ = Altruisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Sens du sacrifice"
            return u"Collectisme"
        elif val >= Trait.SEUIL_A:
            return u"Individualisme"
        else:
            return ""

class Sexualite(TraitGraduel):
    """
    intérêt pour le sexe
    """

    NOM = u"Sexualité"

    def __init__(self):
        self.eTrait_ = Sexualite.NOM

    def PeutEtrePrisALaNaissance(self):
        """
        Renvoie true si il s'agit d'un trait qui peut être choisi dès la crréation du personnage
        Renvoie false si c'est un trait uniquement 'acquis'
        """
        return False

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Abstinent"
            return u"Indifférent"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Pervers"
            return u"Obsédé"
        else:
            return ""

# industrieux == travailleur, aime produire...
class Industrie(TraitGraduel):

    NOM = u"Industrie"

    def __init__(self):
        self.eTrait_ = Industrie.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Paresseux"
        elif val >= Trait.SEUIL_A:
            return u"Industrieux"
        else:
            return ""

class Sensibilite(TraitGraduel):

    NOM = u"Sensibilité"

    def __init__(self):
        self.eTrait_ = Sensibilite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Indifférent"
            return u"Insensible"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Ultrasensible"
            return u"Sensible"
        else:
            return ""

class Violence(TraitGraduel):

    NOM = u"Violence"

    def __init__(self):
        self.eTrait_ = Violence.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Pacifique"
            return u"Doux"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Ultraviolent"
            return u"Violent"
        else:
            return ""

class Ascetisme(TraitGraduel):

    NOM = u"Ascétisme"

    def __init__(self):
        self.eTrait_ = Ascetisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Sybarite"
            return u"Jouisseur"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Ascète"
            return u"Abstinent"
        else:
            return ""

class Courage(TraitGraduel):

    NOM = u"Courage"

    def __init__(self):
        self.eTrait_ = Courage.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Poltron"
            return u"Lâche"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Héroïque"
            return u"Courageux"
        else:
            return ""

class Rancune(TraitGraduel):

    NOM = u"Rancune"

    def __init__(self):
        self.eTrait_ = Rancune.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Magnanime"
            return u"Oublieux"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Implacable"
            return u"Rancunier"
        else:
            return ""

class Ambition(TraitGraduel):

    NOM = u"Ambition"

    def __init__(self):
        self.eTrait_ = Ambition.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Sans ambition"
        elif val >= Trait.SEUIL_A:
            return u"Ambitieux"
        else:
            return ""

class Force(TraitGraduel):

    NOM = u"Force"

    def __init__(self):
        self.eTrait_ = Force.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Anémique"
            return u"Faible"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Herculéen"
            return u"Fort"
        else:
            return ""

class Constitution(TraitGraduel):

    NOM = u"Constitution"

    def __init__(self):
        self.eTrait_ = Constitution.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Chétif"
            return u"Fragile"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Indestructible"
            return u"Résistant"
        else:
            return ""

class Poids(TraitGraduel):

    NOM = u"Poids"

    def __init__(self):
        self.eTrait_ = Poids.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Famélique"
            return u"Maigre"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Obèse"
            return u"Gros"
        else:
            return ""

class Taille(TraitGraduel):

    NOM = u"Taille"

    def __init__(self):
        self.eTrait_ = Taille.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Nain" # gretchin, gnome...
            return u"Petit"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Géant"
            return u"Grand"
        else:
            return ""

class Beaute(TraitGraduel):

    NOM = u"Beauté"

    def __init__(self):
        self.eTrait_ = Beaute.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Hideux"
            return u"Laid"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Apollon"
            return u"Beau"
        else:
            return ""
        
class Animaux(TraitGraduel):

    NOM = u"Soin des animaux"

    def __init__(self):
        self.eTrait_ = Animaux.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Détesté par les animaux"
            return u"Fait fuir les animaux"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Parle à l'oreille des Animaux"
            return u"Doué avec les animaux"
        else:
            return ""
        
class Discretion(TraitGraduel):

    NOM = u"Discrétion"

    def __init__(self):
        self.eTrait_ = Discretion.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Très facile à repérer"
            return u"Facile à repérer"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Quasi invisible"
            return u"Discret"
        else:
            return ""
        
class Endurance(TraitGraduel):

    NOM = u"Endurance"

    def __init__(self):
        self.eTrait_ = Endurance.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Débile"
            return u"Malingre"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Très résistant"
            return u"Endurant"
        else:
            return ""
        
class Habilete(TraitGraduel):

    NOM = u"Habileté"

    def __init__(self):
        self.eTrait_ = Habilete.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Très maladroit"
            return u"Maladroit"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Très habile"
            return u"Habile"
        else:
            return ""
        
class Perception(TraitGraduel):

    NOM = u"Perception"

    def __init__(self):
        self.eTrait_ = Perception.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Myope"
            return u"Peu attentif"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Très perceptif"
            return u"perceptif"
        else:
            return ""

class Mouvement(TraitGraduel):

    NOM = u"Agileté, course"

    def __init__(self):
        self.eTrait_ = Mouvement.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.CARAC_FAIBLE:
            if val <= Trait.CARAC_TRES_FAIBLE:
                return u"Lent et pataud"
            return u"Pataud"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Très agile et rapide"
            return u"Agile et rapide"
        else:
            return ""

class Charme(TraitGraduel):

    NOM = u"Charme"

    def __init__(self):
        self.eTrait_ = Charme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val < Trait.SEUIL_A_PAS:
            if val < Trait.SEUIL_A_PAS_EXTREME:
                return u"Très Déplaisant"
            return u"Déplaisant"
        elif val >= Trait.CARAC_ELEVE:
            if val >= Trait.CARAC_EXCEPTIONNEL:
                return u"Très Charmant"
            return u"Charmant"
        else:
            return ""

class Richesse(TraitGraduel):

    NOM = u"Richesse"

    def __init__(self):
        self.eTrait_ = Richesse.NOM

    def PeutEtrePrisALaNaissance(self):
        return True

    # tmp : numéro affiché pour raison de débug
    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Misérable"
            return u"Pauvre"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Incroyablement riche"
            return u"Très riche"
        else:
            return u""
            # return u"Classe moyenne {}".format(val)

class Gloire(TraitGraduel):

    NOM = u"Gloire"

    def __init__(self):
        self.eTrait_ = Gloire.NOM

    def PeutEtrePrisALaNaissance(self):
        return True

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.CARAC_TRES_FAIBLE:
            return u"Inconnu"
        elif val <= Trait.CARAC_FAIBLE:
            return u"Peu connu"
        elif val <= Trait.CARAC_NORMAL:
            return u"Connu"
        elif val <= Trait.CARAC_ELEVE:
            return u"Très connu"
        elif val <= Trait.CARAC_EXCEPTIONNEL:
            return u"Très célèbre" 
        else:
            return u"Légende vivante"
