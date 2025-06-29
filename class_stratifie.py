import numpy as np

from class_couche import Couche


class Stratifie:
    """
    Class servant aux calculs de couches stratifies
    Cree un objet Stratifie qui est un ensemble de couches

    _ list_monocouches : la liste des monocouches
    """
    def __init__(self, list_monocouches):
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