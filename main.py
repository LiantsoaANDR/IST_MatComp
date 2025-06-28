from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi
from class_couche import Couche

def main():

    couche_1 = Couche(is_uni = True, E_f = 71000, u_f = 0.20, V_f = 0.353, E_m = 3000, u_m = 0.4, alpha = 0, teta = 0)

    print(couche_1.Q)

"""
with open("resultat.txt", "w") as f:
    f.write(str(resultat))
"""


if __name__ == "__main__":
    main()