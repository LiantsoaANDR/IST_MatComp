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

        self.A = self.calcul_A()


    
    def calcul_A(self):
        """
        Calcul la matrice A, la matrice de rigidité membrane
        """
        A = np.zeros((3, 3))
        for couche in self.list_monocouches:
            A += couche.Q * couche.epaisseur
        return A
