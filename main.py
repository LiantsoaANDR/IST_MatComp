import csv

from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi
from class_couche import Couche
from math import degrees

def main():
    couches = [
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=0,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=10,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=30,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=60,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=True,  E_f=71000, u_f=0.20, V_f=0.353, E_m=3000, u_m=0.4, alpha=0,   teta=90,  X_t=1000, X_c=-650, Y_t=30, Y_c=-120, T=45),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=0,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=10,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=30,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=60,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5),
        Couche(is_uni=False,  E_f=72000, u_f=0.20, V_f=0.34, E_m=3000, u_m=0.4, alpha=0,   teta=90,  X_t=650, X_c=-650, Y_t=650, Y_c=-650, T=50, A_1 =0.5, A_2=0.5)
    ]

    resultat_total = []

    for i, couche in enumerate(couches, start=1):
        print("--- Couche {} ---".format(i))
        print(couche.S_prim)

        resultat = {
            "ID_couche": couche.id,
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

    print(resultat_total)
    print("Nombre total de couches : {}".format(Couche.nb_objects))


    # Écriture dans un fichier CSV
    with open("resultats_couches.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=resultat_total[0].keys())
        writer.writeheader()
        writer.writerows(resultat_total)


if __name__ == "__main__":
    main()