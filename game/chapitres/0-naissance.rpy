init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import testDeCarac
    from abs import condition
    from game.abs.humanite.trait import trait
    from game.abs.humanite.trait import viceVertu
    from spe.humanite import pnj_roi_vauban
    from abs.univers import temps
    # from geographie import quartier
    from abs.humanite import identite
    from chapitres.classes import vauban
    from abs.religions import religion

    def genererDateNaissance(situation, ageActuel=15):
        nbJoursDateNaissance = situation[temps.Date.DATE] - 365*ageActuel
        situation[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    def genererVauban(situation, tousLesTraits):
        """
        caracs de base de Vauban quand il est tout jeune
        """
        # ------------ compétences de base brigandyne/Wh
        situation[trait.Animaux.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Volonte.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Endurance.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Mouvement.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Habilete.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Habilete.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Eloquence.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Intelligence.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Evaluation.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Force.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Commandement.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Perception.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Discretion.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.ArmesCorpsACorps.NOM] = trait.Trait.CARAC_FAIBLE
        situation[trait.Tir.NOM] = trait.Trait.CARAC_FAIBLE

        # A FAIRE : changer tout ça, ce n'est ni sa personnalité ni ses caracs
        situation[trait.Opportunisme.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Observation.NOM] = trait.Trait.SEUIL_A
        situation[trait.Cupidite.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Franchise.NOM] = trait.Trait.SEUIL_A_PAS
        # ----- vices et vertus -------------
        situation[viceVertu.Humble.NOM] = viceVertu.ViceVertu.VICIEUX # orgueilleux
        situation[viceVertu.Casanier.NOM] = viceVertu.ViceVertu.VICIEUX # aventureux
        situation[viceVertu.Valeureux.NOM] = viceVertu.ViceVertu.VERTUEUX # Valeureux

        situation[metier.Metier.C_METIER] = u"Prince de sang"

        # compétences professionnelles
        # A FAIRE : changer tout ça, ce n'est ni sa personnalité ni ses caracs
        situation[metier.Politique.NOM] = trait.Trait.SEUIL_A
        situation[metier.Guerrier.NOM] = trait.Trait.SEUIL_A
        situation[metier.Chasseur.NOM] = trait.Trait.SEUIL_A
        situation[metier.Stratege.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques
        situation[vauban.Vauban.CHAPITRE] = 1
        situation[vauban.Vauban.C_EXPLOITS] = 0
        situation[vauban.Vauban.C_USURPATION] = 0
        situation[vauban.Vauban.C_MILITAIRE] = 0 # pas d'armée par défaut
        situation.SetValCarac(religion.Religion.C_RELIGION, religion.Paien.NOM)
        situation.SetValCarac(trait.Gloire.NOM, 0)

        # famille

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        situation[identite.Identite.C_NOM] = vauban.Vauban.C_NOM_VAUBAN

        situation[vauban.Vauban.CARTE_ACTUELLE] = "bg carte481"
        return

label naissance:
    $ genererDateNaissance(situation_, 11)
    $ genererVauban(situation_, traits_)
    jump intro
    #jump grade_ordre_saint_louis # tmp
