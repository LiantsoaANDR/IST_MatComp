import numpy as np

from class_couche import Couche


class Stratifie:
    """
    Class servant aux calculs de couches stratifies
    Cree un objet Stratifie qui est un ensemble de couches
    """
    def __init__(self, list_monocouches):
        """
        _ list_monocouches : la liste des monocouches
        """
        self.list_monocouches = list_monocouches
        self.nb_monocouches = len(list_monocouches)

        position = self.calcul_position()
        self.hauteur = position["hauteur"]
        self.z = position["z"]

        self.A = self.calcul_A()
        self.D = self.calcul_D()
        self.B = self.caclul_B()
        self.Q_m = (1 / self.hauteur) * self.A
        self.S_m = np.linalg.inv(self.Q_m)

        #Les constantes pratiques
        c_prat = self.calcul_cons_pratique()
        self.E_1m = c_prat["E_1m"]
        self.E_2m = c_prat["E_2m"]
        self.G_12m = c_prat["G_12m"]
        self.u_12m = c_prat["u_12m"]
        self.u_16m = c_prat["u_16m"]
        self.u_26m = c_prat["u_26m"]

        self.calcul_UA_UB()
        self.calcul_sigma_mono()

        self.sigma_m1T = min(couche.sigma_m1T for couche in self.list_monocouches)
        self.sigma_m1C = max(couche.sigma_m1C for couche in self.list_monocouches)

        self.sigma_m2T = min(couche.sigma_m2T for couche in self.list_monocouches)
        self.sigma_m2C = max(couche.sigma_m2C for couche in self.list_monocouches)

        self.sigma_m6_plus = min(couche.sigma_m6_plus for couche in self.list_monocouches)
        self.sigma_m6_moins = max(couche.sigma_m6_moins for couche in self.list_monocouches)
        
        self.sigma_mb_plus = min(couche.sigma_mb_plus for couche in self.list_monocouches)
        self.sigma_mb_moins = max(couche.sigma_mb_moins for couche in self.list_monocouches)




    def calcul_position(self):
        """
        Calcul les coordonnées de toutes les couches, et la hauteur
        """
        hauteur = 0
        for couche in self.list_monocouches:
            hauteur += couche.epaisseur

        z = np.zeros((self.nb_monocouches + 1, 1))
        z[0, 0] = -(1/2) * hauteur
        z[self.nb_monocouches, 0] = -z[0, 0]
        i = 1
        while i < self.nb_monocouches:
            z[i, 0] = z[i-1, 0] + self.list_monocouches[i].epaisseur
            i += 1

        return {"hauteur" : hauteur, "z" : z}
    
    def calcul_A(self):
        """
        Calcul la matrice A, la matrice de rigidité membrane
        """
        A = np.zeros((3, 3))
        for couche in self.list_monocouches:
            A += couche.Q * couche.epaisseur
        return A

    def calcul_D(self):
        """
        Calcul de la matrice D, la matrice de rigidité flexion
        """
        D = np.zeros((3, 3))
        i = 0
        for couche in self.list_monocouches:
            D += couche.Q * ((self.z[i+1])**3 - (self.z[i])**3)
            i += 1
        D = (1/3) * D
        return D

    def caclul_B(self):
        """
        Calcul de la matrice B, la matrice de rigididé couplant la membrane et la flexion
        """
        B = np.zeros((3, 3))
        i = 0
        for couche in self.list_monocouches:
            B += couche.Q * ((self.z[i+1])**2 - (self.z[i])**2)
            i += 1
        B = (1/2) * B
        return B
    
    def calcul_cons_pratique(self):
        """
        Calcul des constantes pratiques
        """
        E_1m = 1 / self.S_m[0, 0]
        E_2m = 1 / self.S_m[1, 1]
        G_12m = 1 / self.S_m[2, 2]
        u_12m = (-1) * self.S_m[0, 1] / self.S_m[0, 0]
        u_16m = (-1) * self.S_m[0, 2] / self.S_m[0, 0]
        u_26m = (-1) * self.S_m[1, 2] / self.S_m[1, 1]
        return {"E_1m":E_1m, "E_2m":E_2m, "G_12m": G_12m, "u_12m":u_12m, "u_16m":u_16m, "u_26m":u_26m}
    
    def calcul_UA_UB(self):
        """
        Calcul de UA pour chaque couche
        """
        for couche in self.list_monocouches:
            couche.UA = self.S_m @ couche.GA_prim @ self.S_m
        
        for couche in self.list_monocouches:
            couche.UB = self.S_m @ couche.GB_prim


    def calcul_sigma_mono(self):
        """
        Calcul des résistances en traction et compression admissibles appliquées sur une monocouche
        """
        for couche in self.list_monocouches:
            U_11 = couche.UA[0, 0]
            U_22 = couche.UA[1, 1]
            U_66 = couche.UA[2, 2]
            U_1 = couche.UB[0, 0]
            U_2 = couche.UB[1, 0]
            U_6 = couche.UB[2, 0]
            U_12 = couche.UA[0, 1]
            B_1 = U_11 + U_22 + 2*U_12
            B_2 = U_1 + U_2      

            couche.sigma_m1T = ((-1)*U_1 + (((U_1**2) + 4*U_11)**0.5)) / (2 * U_11)
            couche.sigma_m1C = ((-1)*U_1 - (((U_1**2) + 4*U_11)**0.5)) / (2 * U_11)

            couche.sigma_m2T = ((-1)*U_2 + (((U_2**2) + 4*U_22)**0.5)) / (2 * U_22)
            couche.sigma_m2C = ((-1)*U_2 - (((U_2**2) + 4*U_22)**0.5)) / (2 * U_22)

            couche.sigma_m6_plus = ((-1)*U_6 + (((U_6**2) + 4*U_66)**0.5)) / (2 * U_66)
            couche.sigma_m6_moins = ((-1)*U_6 - (((U_6**2) + 4*U_66)**0.5)) / (2 * U_66)

            couche.sigma_mb_plus = ((-1)*B_2 + (((B_2**2) + 4*B_1)**0.5)) / (2 * B_1)
            couche.sigma_mb_moins = ((-1)*B_2 - (((B_2**2) + 4*B_1)**0.5)) / (2 * B_1)

    