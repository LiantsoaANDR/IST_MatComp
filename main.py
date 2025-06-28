import csv

from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi
from class_couche import Couche

def main():

    couche_1 = Couche(is_uni = True, E_f = 71000, u_f = 0.20, V_f = 0.353, E_m = 3000, u_m = 0.4, alpha = 0, teta = 0, X_t = 1000, X_c = -650, Y_t = 30, Y_c = -100, T = 50)

    print(couche_1.S_prim)

    resultat_1 = {
        "ID couche = ": couche_1.id,
        "E_1": couche_1.E_1,
        "E_2": couche_1.E_2,
        "G_12": couche_1.G_12,
        "u_12": couche_1.u_12,
        "u_16": couche_1.u_16,
        "u_26": couche_1.u_26,
        "sigma_1T": couche_1.sigma_1T,
        "sigma_1C": couche_1.sigma_1C,
        "sigma_2T": couche_1.sigma_2T,
        "sigma_2C": couche_1.sigma_2C,
        "sigma_6_plus": couche_1.sigma_6_plus,
        "sigma_6_moins": couche_1.sigma_6_moins,
        "sigma_b_plus": couche_1.sigma_b_plus,
        "sigma_b_moins": couche_1.sigma_b_moins
        }
    
    print(resultat_1)

    print("Le nombre de couche est : {} ".format(Couche.nb_objects))


    with open("resultats_couche.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=resultat_1.keys())
        writer.writeheader()
        writer.writerow(resultat_1)


if __name__ == "__main__":
    main()