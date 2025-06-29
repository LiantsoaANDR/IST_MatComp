import numpy as np

from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi
from math import cos, sin, radians


class Couche:
    """
    Classe servant à créer des couches
    """

    nb_objects = 0
    def __init__(self, id=None, is_uni = True, E_f = 0, u_f = 0, V_f = 0, E_m = 0, u_m = 0, alpha = 0, teta = 0, X_t = 0, X_c = 0, Y_t = 0, Y_c = 0, T = 0, A_1 = None, A_2 = None):
        """
        Initialise l'object couche
        _ id : son identifiant
        _ E_f : module d'Young des fibres
        _ V_f : fraction volumique des fibres
        _ E_m : module d'Young de la matrice
        _ V_m : fraction volumique de la matrice
        _ u_f : coefficient de poisson des fibres
        _ u_m : coefficient de poisson de la matrice
        _ alpha : l'angle alpha en degre
        _ teta : l'angle teta en degre
        _ X_t : Limite admissible en traction suivant (0,X)
        _ X_c : Limite admissible en compression suivant (0,X)
        _ Y_t : Limite admissible en traction suivant (0,Y)
        _ Y_c : Limite admissible en compression suivant (0,Y)
        _ T : Limite admissible en cisaillement dans (0,1,2)
        _ A_1 : proportion des fibres suivant (0X)
        _ A_2 : proportion des fibres suivant (0Y)
        """
        if id is not None:
            self.id = id
        else:
            Couche.nb_objects += 1
            self.id = Couche.nb_objects

        V_m = 1 - V_f
        self.alpha = radians(alpha)
        self.teta = radians(teta)
        self.beta = self.alpha - self.teta
        self.X_t = X_t
        self.X_c = X_c
        self.Y_t = Y_t
        self.Y_c = Y_c
        self.T = T

        if is_uni:
            if V_f > 0.4:
                resultat = calcul_melange(E_f, E_m, V_f, V_m, u_m, u_f)
                print("Loi melange uni :")
                print(resultat)
            else :
                resultat = calcul_puck_uni(E_f, E_m, V_f, V_m, u_m, u_f)
                print("Formules de PUCK uni :")
        else :
            print("Formules BI :")
            resultat = calcul_puck_bi(E_f, E_m, V_f, V_m, u_f, u_m, A_1, A_2)
            print(resultat)

        self.E_x = resultat["E_x"]
        self.E_y = resultat["E_y"]
        self.G_xy = resultat["G_xy"]
        self.u_xy = resultat["u_xy"]
        #self.u_yx = resultat["u_yx"]

        self.Q = self.calcul_Q()
        self.R = self.calcul_R()

        self.S_prim = self.calcul_S_prim()
        self.E_1 = 1 / self.S_prim[0, 0]
        self.E_2 = 1 / self.S_prim[1, 1]
        self.G_12 = 1 / self.S_prim[2, 2]
        self.u_12 = (-1) * self.S_prim[0, 1] / self.S_prim[0, 0]
        self.u_16 = (-1) * self.S_prim[0, 2] / self.S_prim[0, 0]
        self.u_26 = (-1) * self.S_prim[1, 2] / self.S_prim[1, 1]

        self.FA_prim = self.calcul_FA_prim()
        self.FB_prim = self.calcul_FB_prim()
        F_11 = self.FA_prim[0, 0]
        F_22 = self.FA_prim[1, 1]
        F_66 = self.FA_prim[2, 2]
        F_1 = self.FB_prim[0, 0]
        F_2 = self.FB_prim[1, 0]
        F_6 = self.FB_prim[2, 0]
        F_12 = self.FA_prim[0, 1]

        self.sigma_1T = ((-1)*F_1 + (((F_1**2) + 4*F_11)**0.5)) / (2 * F_11)
        self.sigma_1C = ((-1)*F_1 - (((F_1**2) + 4*F_11)**0.5)) / (2 * F_11)

        self.sigma_2T = ((-1)*F_2 + (((F_2**2) + 4*F_22)**0.5)) / (2 * F_22)
        self.sigma_2C = ((-1)*F_2 - (((F_2**2) + 4*F_22)**0.5)) / (2 * F_22)

        self.sigma_6_plus = ((-1)*F_6 + (((F_6**2) + 4*F_66)**0.5)) / (2 * F_66)
        self.sigma_6_moins = ((-1)*F_6 - (((F_6**2) + 4*F_66)**0.5)) / (2 * F_66)

        B_1 = F_11 + F_22 + 2*F_12
        B_2 = F_1 + F_2
        self.sigma_b_plus = ((-1)*B_2 + (((B_2**2) + 4*B_1)**0.5)) / (2 * B_1)
        self.sigma_b_moins = ((-1)*B_2 - (((B_2**2) + 4*B_1)**0.5)) / (2 * B_1)

  
    def calcul_Q(self):
        """
        Calcul de la matrice de souplesse S et son inverse qui est Q dans le repere d orthotropie
        """
        S = np.zeros((3, 3))
        S[0, 0] = 1 / self.E_x
        S[0, 1] = (-1) * (self.u_xy / self.E_x)
        S[1, 0] = (-1) * (self.u_xy / self.E_x)
        S[1, 1] = 1 / self.E_y
        S[2, 2] = 1 / self.G_xy

        Q = np.linalg.inv(S)

        return Q


    def calcul_R(self):
        """"
        Calcul du tenseur de changement de repere
        """
 
        c = cos(self.beta)
        s = sin(self.beta)

        R = np.zeros((3, 3))
        R[0, 0] = c**2
        R[0, 1] = s**2
        R[0, 2] = 2 * c * s
        R[1, 0] = s**2
        R[1, 1] = c**2
        R[1, 2] = (-2) * c * s
        R[2, 0] = (-1) * c * s
        R[2, 1] = c * s
        R[2, 2] = (c**2) - (s**2)

        return R


    def calcul_S_prim(self):
        """
        Calcul de la matrice de souplesse dans le repere de sollicitations
        """
        Q_prim = self.R @ self.Q @ self.R.T

        S_prim = np.linalg.inv(Q_prim)

        return S_prim


    def calcul_FA_prim(self):
        """
        Calcul de la matrice FA dans le repere d orthotropie
        """
        F_xx = -1 / (self.X_c * self.X_t)
        F_yy = -1 / (self.Y_c * self.Y_t)
        F_ss = 1 / (self.T**2)
        F_xy_prim = (-1/2) * (((self.Y_c * self.Y_t) / (self.X_c * self.X_t))**0.5)
        F_xy = F_xy_prim * ((F_xx * F_yy)**0.5)

        FA = np.zeros((3, 3))
        FA[0, 0] = F_xx
        FA[0, 1] = F_xy
        FA[1, 0] = F_xy
        FA[1, 1] = F_yy
        FA[2, 2] = F_ss

        R_inv = np.linalg.inv(self.R)
        FA_prim = R_inv.T @ FA @ R_inv
        return FA_prim
    

    def calcul_FB_prim(self):
        """
        Calcul de FB dans le repere d'orthotropie
        """
        F_x = (1 / self.X_t) + (1 / self.X_c)
        F_y = (1 / self.Y_t) + (1 / self.Y_c)

        FB = np.zeros((3, 1))
        FB[0, 0] = F_x
        FB[1, 0] = F_y

        R_inv = np.linalg.inv(self.R)
        FB_prim = R_inv.T @ FB

        return FB_prim