import numpy as np

from class_couche import Couche


class Stratifie:
    """
    Class servant aux calculs de couches stratifies
    Cree un objet Stratifie qui est un ensemble de couches
    """
    def __init__(self, monocouches):
        self.monocouches = monocouches
        self.nb_monocouches = len(monocouches)