class Couche:
    """
    Classe servant à créer des couches
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize the new object"""
        if id is not None:
            self.id = id
        else:
            Couche.__nb_objects += 1
            self.id = Couche.__nb_objects

    