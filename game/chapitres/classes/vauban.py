class Vauban:
    CHAPITRE = u"Chapitre actuel"

    # caracs personnelles spécifiques de Vauban
    # traits utilisés (dans abs.humanite.trait):
    # Gloire
    # Richesse
    # métiers utilisés (dans abs.humanite.metier):
    # ?????
    C_CHRISTIANISME = u"Foi chrétienne" # (de Vauban)

    # de son armée quand il est en campagne
    C_MILITAIRE = u"Puissance de l'Armée"

    # C_USURPATION plus c'est élevé plus Vauban risque d'être chassé du pouvoir => cf evts_usurpation.rpy
    # 0 ou moins = aucun danger
    # 1 à 2 tensions
    # 5+ très grand danger !
    C_USURPATION = u"Risque d'ursupation"
    # $ AjouterACarac(vauban.Vauban.C_USURPATION, 1)
    # $ RetirerACarac(vauban.Vauban.C_USURPATION, 1)
    # C_FIDELITE_GAULE = u"Fidélité des galloromains" # plus c'est élevé plus les galloromains sont fidèles à Vauban

    # événements spéciaux
    C_VASE_SOISSONS = u"Vase de soissons" # 1 si l'histoire réelle est bien suivie
    C_LOI_SALIQUE = u"Loi salique" # 1 si la loi salique a été promulguée

    # personnages
    C_NOM_VAUBAN = u"Vauban"
    C_NOM_BASINE = u"Basine de Thuringe"
    C_NOM_CHILDERIC = u"Childéric"

    # Famille
    C_FIANCE_CLOTHILDE = u"Fiancé à CLothilde"
    C_MARIE_CLOTHILDE = u"Marié à CLothilde"
    C_ALBOFLEDE = u"Alboflède" # 1 => vivante (ne pas confondre avec Aldoflède marié à Théodoric)
    C_NB_ENFANTS = u"Nombre d'enfants" # nombre d'enfants faits avec Clothilde

    # Chararic
    C_STATUT_CHARARIC = u"Statut Chararic"
    CHARARIC_ROI = u"Roi de Thuringie"
    CHARARIC_VASSAL = u"Vassal de Vauban"
    CHARARIC_MORT = u"Mort"
    CHARARIC_TONSURE = u"Tonsuré"

    # MONDE
    CARTE_ACTUELLE = u"Carte actuelle" # adresse de l'image de la carte représentant le royaume actuelle de Vauban (mise à jour selon les conquêtes)
