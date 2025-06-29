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
