from loi_melange import calcul_melange
from formules_PUCK_UNI import calcul_puck_uni
from formules_PUCK_BI import calcul_puck_bi
from math import cos, sin, radians

import numpy as np


class Couche:
    """
    Classe servant à créer des couches
    """

    nb_objects = 0
    def __init__(self, id=None, is_uni = True, E_f = 0, u_f = 0, V_f = 0, E_m = 0, u_m = 0, alpha = 0, teta = 0, X_t = 0, X_c = 0, Y_t = 0, Y_c = 0, T = 0, A_1 = None, A_2 = None):
        """Initialize la couche"""
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

                self.E_x = resultat["E_x"]
                self.E_y = resultat["E_y"]
                self.G_xy = resultat["G_xy"]
                self.u_xy = resultat["u_xy"]
                self.u_yx = resultat["u_yx"]

                self.Q = self.calcul_Q()
                self.R = self.calcul_R()

                self.S_prim = self.calcul_S_prim()
                self.E_1 = 1 / self.S_prim[0, 0]
                self.E_2 = 1 / self.S_prim[1, 1]
                self.G_12 = 1 / self.S_prim[2, 2]
                self.u_12 = (-1) * self.S_prim[0, 1] / self.S_prim[0, 0]
                self.u_16 = (-1) * self.S_prim[0, 2] / self.S_prim[0, 0]
                self.u_26 = (-1) * self.S_prim[1, 2] / self.S_prim[1, 1]

                self.FA_prim = self.calcul_FA_prim
                self.FB_prim = self.calcul_FB_prim
                self.sigma_1T =
                self.sigma_1C =
                self.sigma_2T = 
                self.sigma_2C =
                self.sigma_6_plus =
                self.sigma_6_moins =
                self.sigma_b_plus =
                self.sigma_b_moins =
        else :
            print("Formules BI :")
            resultat = calcul_puck_bi(E_f, E_m, V_f, V_m, u_f, u_m, A_1, A_2)
            print(resultat)

  
    def calcul_Q(self):
        """
        Calcul de la matrice de souplesse S et son inverse qui est Q dans le repere d’orthotropie
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
        Calcul de la matrice FA dans le repere d'orthotropie
        """
        F_xx = -1 / (self.X_c * self.X_t)
        F_yy = -1 / (self.Y_c * self.Y_t)
        F_ss = 1 / (T**2)
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