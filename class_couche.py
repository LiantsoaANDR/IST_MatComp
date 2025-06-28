from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi


class Couche:
    """
    Classe servant à créer des couches
    """

    __nb_objects = 0
    def __init__(self, id=None, is_uni = True, E_f = 0, u_f = 0, V_f = 0, E_m = 0, u_m = 0, A_1 = None, A_2 = None):
        """Initialize the new object"""
        if id is not None:
            self.id = id
        else:
            Couche.__nb_objects += 1
            self.id = Couche.__nb_objects

        V_m = 1 - V_f

        if is_uni:
            if V_f > 0.4:
                resultat = calcul_melange(E_f, E_m, V_f, V_m, u_m, u_f)
                print("Loi melange uni :")
                print(resultat)
            else :
                resultat = calcul_puck_uni(E_f, E_m, V_f, V_m, u_m, u_f)
                print("Formules de PUCK uni :")
                print(resultat)
                self.E_x = resultat["E_x"]
                self.E_y = resultat["E_y"]
                self.G_xy = resultat["G_xy"]
                self.u_xy = resultat["u_xy"]
                self.u_yx = resultat["u_yx"]
        else :
            print("Formules BI :")
            resultat = calcul_puck_bi(E_f, E_m, V_f, V_m, u_f, u_m, A_1, A_2)
            print(resultat)

  
    def calcul_Q(self):
        """
        Calcul de la matrice de souplesse et son inverse qui est Q
        """
        S = [[0 for i in range(3)] for j in range(3)]
        S[0][0] = 1/Ex





"""
        self.E_f = E_f
        self.u_f = u_f
        self.V_f = V_f
        self.E_m = E_m
        self.u_m = u_m
        self.V_m = 1 - V_f 
"""