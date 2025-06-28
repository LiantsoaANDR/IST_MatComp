from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi


def main():
    V_f = 0.3
    V_m = 0.7

    E_f = 73000
    E_m = 5200

    u_f = 0.325
    u_m = 0.38

    is_uni = True
    A_1 = 0.5
    A_2 = 0.5

    if not(V_f + V_m == 1):
        print("Error : V_f + V_m != 1")
        return

    if V_f < 0.1:
        print("Error : Le Vf est inferieur a 0.1")
        return


    if is_uni:
        if V_f > 0.4:
            resultat = calcul_melange(E_f, E_m, V_f, V_m, u_m, u_f)
            print("Loi melange uni :")
            print(resultat)
        else :
            resultat = calcul_puck_uni(E_f, E_m, V_f, V_m, u_m, u_f)
            print("Formules de PUCK uni :")
            print(resultat)
    else :
        print("Formules BI :")
        resultat = calcul_puck_bi(E_f, E_m, V_f, V_m, u_f, u_m, A_1, A_2)
        print(resultat)

"""
with open("resultat.txt", "w") as f:
    f.write(str(resultat))
"""


if __name__ == "__main__":
    main()