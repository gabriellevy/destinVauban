from game.abs.humanite.trait import trait
from game.abs.humanite.trait import maitrise
from game.abs.humanite.trait import viceVertu
import random

class CollectionTraits:

    def __init__(self):
        self.lTraits_ = dict()
        # ---------------- compétences de bases brigandyne/warhammmer
        animaux = trait.Animaux()
        self.SetTrait(trait.Animaux.NOM, animaux)
        armesCorpsACorps = trait.ArmesCorpsACorps()
        self.SetTrait(trait.ArmesCorpsACorps.NOM, armesCorpsACorps)
        habilete = trait.Habilete()
        self.SetTrait(trait.Habilete.NOM, habilete)
        eloquence = trait.Eloquence()
        self.SetTrait(trait.Eloquence.NOM, eloquence)
        endurance = trait.Endurance()
        self.SetTrait(trait.Endurance.NOM, endurance)
        intelligence = trait.Intelligence()
        self.SetTrait(trait.Intelligence.NOM, intelligence)
        evaluation = trait.Evaluation()
        self.SetTrait(trait.Evaluation.NOM, evaluation)
        mouvement = trait.Mouvement()
        self.SetTrait(trait.Mouvement.NOM, mouvement)
        perception = trait.Perception()
        self.SetTrait(trait.Perception.NOM, perception)
        discretion = trait.Discretion()
        self.SetTrait(trait.Discretion.NOM, discretion)
        tir = trait.Tir()
        self.SetTrait(trait.Tir.NOM, tir)
        volonte = trait.Volonte()
        self.SetTrait(trait.Volonte.NOM, volonte)

        # ----- spécifiques assez courantes pour que je les garde ici : 
        destin = trait.Destin()
        self.SetTrait(trait.Destin.NOM, destin)    
        gloire = trait.Gloire()
        self.SetTrait(trait.Gloire.NOM, gloire)

        # A FAIRE : voir ce que je garde ci après
        richesse = trait.Richesse()
        self.SetTrait(trait.Richesse.NOM, richesse)
        charme = trait.Charme()
        self.SetTrait(trait.Charme.NOM, charme)
        observation = trait.Observation()
        self.SetTrait(trait.Observation.NOM, observation)
        beaute = trait.Beaute()
        self.SetTrait(trait.Beaute.NOM, beaute)
        taille = trait.Taille()
        self.SetTrait(trait.Taille.NOM, taille)
        poids = trait.Poids()
        self.SetTrait(trait.Poids.NOM, poids)
        resistance = trait.Constitution()
        self.SetTrait(trait.Constitution.NOM, resistance)
        force = trait.Force()
        self.SetTrait(trait.Force.NOM, force)
        patriarcat = trait.Patriarcat()
        self.SetTrait(trait.Patriarcat.NOM, patriarcat)
        sexualite = trait.Sexualite()
        self.SetTrait(trait.Sexualite.NOM, sexualite)
        cupidite = trait.Cupidite()
        self.SetTrait(trait.Cupidite.NOM, cupidite)
        sincerite = trait.Sincerite()
        self.SetTrait(trait.Sincerite.NOM, sincerite)
        opp = trait.Opportunisme()
        self.SetTrait(trait.Opportunisme.NOM, opp)
        ind = trait.Industrie()
        self.SetTrait(trait.Industrie.NOM, ind)
        franch = trait.Franchise()
        self.SetTrait(trait.Franchise.NOM, franch)
        prag = trait.Pragmatisme()
        self.SetTrait(trait.Pragmatisme.NOM, prag)
        intel = trait.Intellectualisme()
        self.SetTrait(trait.Intellectualisme.NOM, intel)
        sensi = trait.Sensibilite()
        self.SetTrait(trait.Sensibilite.NOM, sensi)
        ascetisme = trait.Ascetisme()
        self.SetTrait(trait.Ascetisme.NOM, ascetisme)
        prud = trait.Prudence()
        self.SetTrait(trait.Prudence.NOM, prud)
        serenite = trait.Serenite()
        self.SetTrait(trait.Serenite.NOM, serenite)

        # --------------- Maîtrise
        architecture = maitrise.Architecture()
        self.SetTrait(maitrise.Architecture.NOM, architecture)
        equitation = maitrise.Equitation()
        self.SetTrait(maitrise.Equitation.NOM, equitation)
        mathematiques = maitrise.Mathematiques()
        self.SetTrait(maitrise.Mathematiques.NOM, mathematiques)
        fortification = maitrise.Fortification()
        self.SetTrait(maitrise.Fortification.NOM, fortification)
        hydraulique = maitrise.Hydraulique()
        self.SetTrait(maitrise.Hydraulique.NOM, hydraulique)
        poliorcetique = maitrise.Poliorcetique()
        self.SetTrait(maitrise.Poliorcetique.NOM, poliorcetique)
        espagnol = maitrise.Espagnol()
        self.SetTrait(maitrise.Espagnol.NOM, espagnol)
        strategie = maitrise.Strategie()
        self.SetTrait(maitrise.Strategie.NOM, strategie)
        carthographie = maitrise.Carthographie()
        self.SetTrait(maitrise.Carthographie.NOM, carthographie)

        # ------------- Vices et vertus
        humble = viceVertu.Humble()
        self.SetTrait(viceVertu.Humble.NOM, humble)
        casanier = viceVertu.Casanier()
        self.SetTrait(viceVertu.Casanier.NOM, casanier)
        placide = viceVertu.Placide()
        self.SetTrait(viceVertu.Placide.NOM, placide)
        bienveillant = viceVertu.Bienveillant()
        self.SetTrait(viceVertu.Bienveillant.NOM, bienveillant)
        prodigue = viceVertu.Prodigue()
        self.SetTrait(viceVertu.Prodigue.NOM, prodigue)
        desinteresse = viceVertu.Desinteresse()
        self.SetTrait(viceVertu.Desinteresse.NOM, desinteresse)
        sobre = viceVertu.Sobre()
        self.SetTrait(viceVertu.Sobre.NOM, sobre)
        cartesien = viceVertu.Cartesien()
        self.SetTrait(viceVertu.Cartesien.NOM, cartesien)
        reflechi = viceVertu.Reflechi()
        self.SetTrait(viceVertu.Reflechi.NOM, reflechi)
        valeureux = viceVertu.Valeureux()
        self.SetTrait(viceVertu.Valeureux.NOM, valeureux)
        chaste = viceVertu.Chaste()
        self.SetTrait(viceVertu.Chaste.NOM, chaste)
        naif = viceVertu.Naif()
        self.SetTrait(viceVertu.Naif.NOM, naif)
        artificialiste = viceVertu.Artificialiste()
        self.SetTrait(viceVertu.Artificialiste.NOM, artificialiste)
        travailleur = viceVertu.Travailleur()
        self.SetTrait(viceVertu.Travailleur.NOM, travailleur)
        discipline = viceVertu.Discipline()
        self.SetTrait(viceVertu.Discipline.NOM, discipline)
        empathique = viceVertu.Empathique()
        self.SetTrait(viceVertu.Empathique.NOM, empathique)
        sociable = viceVertu.Sociable()
        self.SetTrait(viceVertu.Sociable.NOM, sociable)
        loyal = viceVertu.Loyal()
        self.SetTrait(viceVertu.Loyal.NOM, loyal)
        esthete = viceVertu.Esthete()
        self.SetTrait(viceVertu.Esthete.NOM, esthete)

    def getTraitAleatoire(self):
        return random.choice(list(self.lTraits_.values()))

    def __getitem__(self, idTrait):
        if not idTrait in self.lTraits_:
            self.CreerTrait(idTrait)
        return self.lTraits_[idTrait]

    def __setitem__(self, idTrait, ptrait):
        self.SetTrait(idTrait, ptrait)

    def SetTrait(self, idTrait, ptrait):
        # si la carac n'existe pas encore, la créer
        if not idTrait in self.lTraits_:
            self.CreerTrait(idTrait)

        self.lTraits_[idTrait] = ptrait

    def CreerTrait(self, idTrait):
        ptrait = trait.Trait(idTrait)
        self.lTraits_[idTrait] = ptrait

    def __len__(self):
        return len(self.lTraits_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lTraits_) == 0:
            return "Aucun trait."
        str = u"Liste de tous les traits : "
        for trait in self.lTraits_:
            str = str + trait + ","
        return str