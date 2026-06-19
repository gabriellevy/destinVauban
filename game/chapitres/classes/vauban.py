class Vauban:
    CHAPITRE = u"Chapitre actuel"

    # caracs personnelles spécifiques de Vauban
    C_GRADE = u"Grade" 
    GRADE_LIEUTENANT = u"Lieutenant aux gardes"
    GRADE_SAINT_LOUIS = u"Ordre de Saint Louis"
    C_EXPLOITS = u"Exploits"

    # titres
    C_SEIGNEUR_BAZOCHES = u"Seigneur de Bazoches"
    
    C_FAVEUR_ROI = u"Faveur du roi"
    # métiers utilisés (dans abs.humanite.metier):
    # ????? A FAIRE : supprimer le concept de métier ? il a peu d'intérêt dans le nouveau système...
    # de son armée quand il est en campagne
    C_MILITAIRE = u"Puissance de l'Armée"

    # C_USURPATION plus c'est élevé plus Vauban risque d'être chassé du pouvoir => cf evts_usurpation.rpy
    # 0 ou moins = aucun danger
    # 1 à 2 tensions
    # 5+ très grand danger !
    C_USURPATION = u"Risque d'ursupation"
    # $ AjouterACarac(vauban.Vauban.C_USURPATION, 1)
    # $ RetirerACarac(vauban.Vauban.C_USURPATION, 1)
    # plus c'est élevé plus ss serfs sont fidèles à Vauban 
    # A FAIRE : voire si ça vaut le coup de gérer ça sachant que sa femme gère son domaine
    C_FIDELITE_SERFS = u"Fidélité des serfs" 

    # événements spéciaux

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
