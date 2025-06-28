from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi
from class_couche import Couche

def main():

    couche_1 = Couche(is_uni = True, E_f = 73000, u_f = 0.325, V_f = 0.3, E_m = 5200, u_m = 0.38)

    print(couche_1.E_x)

"""
with open("resultat.txt", "w") as f:
    f.write(str(resultat))
"""


if __name__ == "__main__":
    main()