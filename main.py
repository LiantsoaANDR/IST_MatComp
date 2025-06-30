import csv

from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi
from class_couche import Couche
from math import degrees
from class_stratifie import Stratifie

def main():
    """
    Fonction main

    Dans <couches> : on insère des monocouches pour cacluler leurs propriétés individuelles
    Dans <monocouhes_a_0_uni>, etc : on insère les monocouches formant la couche stratifiée composée des <monocouhes_a_0_uni>
    <monocouhes_a_0_uni> peut être <monocouhes_a_15_uni>, <monocouhes_a_0_bidi>, etc

    En output : génère 3 fichiers csv,  1 pour les résultats des caclculs des propriétés individuelles
                                        1 pour les résultats des calculs des propriétés couche stratifiée unidirectionnel
                                        1 pour les résultats des calculs des propriétés couche stratifiée bidirectionnel

    """
    #Création des monocouches pour calculs monocouches, couches est une liste de monocouches
    couches = [
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=0,   X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=10,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=30,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=60,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=90,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=0,   X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=10,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=30,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=60,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=90,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5)
    ]

    #Création des monocouches pour calculs stratifiés, monocouches_a_alpha_uni-ou-dir est une liste de monocouches
    monocouches_a_0_uni = [
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),                        
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),                 
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1)     
    ]
    couche_stratifie_a_0_uni = Stratifie(monocouches_a_0_uni)

    monocouches_a_15_uni = [
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1)
    ]
    couche_stratifie_a_15_uni = Stratifie(monocouches_a_15_uni)

    monocouches_a_30_uni = [
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1)
    ]
    couche_stratifie_a_30_uni = Stratifie(monocouches_a_30_uni)

    monocouches_a_45_uni = [
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=0,   X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1),
        Couche(is_uni=True,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, epaisseur=1)
    ]
    couche_stratifie_a_45_uni = Stratifie(monocouches_a_45_uni)

    monocouches_a_0_bidi = [
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=0,   teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1)
    ]
    couche_stratifie_a_0_bidi = Stratifie(monocouches_a_0_bidi)

    monocouches_a_15_bidi = [
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=15,  teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1)
    ]
    couche_stratifie_a_15_bidi = Stratifie(monocouches_a_15_bidi)

    monocouches_a_30_bidi = [
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=30,  teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1)
    ]
    couche_stratifie_a_30_bidi = Stratifie(monocouches_a_30_bidi)

    monocouches_a_45_bidi = [
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=90,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1),
        Couche(is_uni=False,  E_f=71500, u_f=0.25, V_f=0.345, E_m=2900, u_m=0.4, alpha=45,  teta=45,  X_t=1100, X_c=-700, Y_t=40, Y_c=-140, T=65, A_1 =0.5, A_2=0.5, epaisseur=1)
    ]
    couche_stratifie_a_45_bidi = Stratifie(monocouches_a_45_bidi)



    # Partie mise en forme des resultats de calculs monocouches
    resultat_total = []
    for couche in couches:
        resultat = {
            "ID_couche": couche.id,
            "Uni?" : couche.is_uni,
            "Angle Teta" : degrees(couche.teta),
            "E_1": couche.E_1,
            "E_2": couche.E_2,
            "G_12": couche.G_12,
            "u_12": couche.u_12,
            "u_16": couche.u_16,
            "u_26": couche.u_26,
            "sigma_1T": couche.sigma_1T,
            "sigma_1C": couche.sigma_1C,
            "sigma_2T": couche.sigma_2T,
            "sigma_2C": couche.sigma_2C,
            "sigma_6_plus": couche.sigma_6_plus,
            "sigma_6_moins": couche.sigma_6_moins,
            "sigma_b_plus": couche.sigma_b_plus,
            "sigma_b_moins": couche.sigma_b_moins
        }

        resultat_total.append(resultat)


    # Écriture dans un fichier CSV de resultat mono
    with open("resultats_couches.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=resultat_total[0].keys())
        writer.writeheader()
        writer.writerows(resultat_total)
    print("Fichier resultats_couches.csv genere")

    # Partie mise en forme des resultats de calculs stratifiés UNI
    strats_uni = [
        couche_stratifie_a_0_uni,
        couche_stratifie_a_15_uni,
        couche_stratifie_a_30_uni,
        couche_stratifie_a_45_uni
    ]
    
    resultat_strat_uni = []
    for strat in strats_uni:
        resultat_strat_uni.append({
            "Uni?" : strat.list_monocouches[0].is_uni,
            "alpha": degrees(strat.list_monocouches[0].alpha),
            "sigma_m1C": strat.sigma_m1C,
            "sigma_m1T": strat.sigma_m1T,
            "sigma_m2C": strat.sigma_m2C,
            "sigma_m2T": strat.sigma_m2T,
            "sigma_m6_plus": strat.sigma_m6_plus,
            "sigma_m6_moins": strat.sigma_m6_moins,
            "sigma_mb_plus": strat.sigma_mb_plus,
            "sigma_mb_moins": strat.sigma_mb_moins,
            "E_1m": strat.E_1m,
            "E_2m": strat.E_2m,
            "G_12m": strat.G_12m,
            "u_12m": strat.u_12m,
            "u_16m": strat.u_16m,
            "u_26m": strat.u_26m,
            "E_1f": strat.E_1f,
            "E_2f": strat.E_2f,
            "G_12f": strat.G_12f,
            "u_12f": strat.u_12f,
            "u_16f": strat.u_16f,
            "u_26f": strat.u_26f,
        })
    # Écriture dans un fichier CSV de resultat strat UNI
    with open("resultats_stratifie_uni.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=resultat_strat_uni[0].keys())
        writer.writeheader()
        writer.writerows(resultat_strat_uni)
    print("Fichier resultats_stratifie_uni.csv genere")


    # Partie mise en forme des resultats de calculs stratifiés BIDI
    strats_bidi = [
        couche_stratifie_a_0_bidi,
        couche_stratifie_a_15_bidi,
        couche_stratifie_a_30_bidi,
        couche_stratifie_a_45_bidi
    ]

    resultat_strat_bidi = []
    for strat in strats_bidi:
        resultat_strat_bidi.append({
            "Uni?" : strat.list_monocouches[0].is_uni,
            "alpha": degrees(strat.list_monocouches[0].alpha),
            "sigma_m1C": strat.sigma_m1C,
            "sigma_m1T": strat.sigma_m1T,
            "sigma_m2C": strat.sigma_m2C,
            "sigma_m2T": strat.sigma_m2T,
            "sigma_m6_plus": strat.sigma_m6_plus,
            "sigma_m6_moins": strat.sigma_m6_moins,
            "sigma_mb_plus": strat.sigma_mb_plus,
            "sigma_mb_moins": strat.sigma_mb_moins,
            "E_1m": strat.E_1m,
            "E_2m": strat.E_2m,
            "G_12m": strat.G_12m,
            "u_12m": strat.u_12m,
            "u_16m": strat.u_16m,
            "u_26m": strat.u_26m,
            "E_1f": strat.E_1f,
            "E_2f": strat.E_2f,
            "G_12f": strat.G_12f,
            "u_12f": strat.u_12f,
            "u_16f": strat.u_16f,
            "u_26f": strat.u_26f,
        })
    # Écriture dans un fichier CSV de resultat strat BIDI
    with open("resultats_stratifie_bidi.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=resultat_strat_bidi[0].keys())
        writer.writeheader()
        writer.writerows(resultat_strat_bidi)
    print("Fichier resultats_stratifie_bidi.csv genere")





if __name__ == "__main__":
    main()