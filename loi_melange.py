def calcul_melange(E_f, E_m, V_f, V_m, u_m, u_f):
    """
    Calcul E_x , E_y à partir de la Loi des mélanges
    _ E_f : module d'Young des fibres
    _ V_f : fraction volumique des fibres
    _ E_m : module d'Young de la matrice
    _ V_m : fraction volumique de la matrice
    _ u_m : coefficient de poisson de la matrice
    _ u_f : coefficient de poisson des fibres
    """
    E_x = E_f * V_f + E_m * V_m
    E_y = (E_f * E_m) / (V_f * E_m + V_m * E_f)

    u_xy = u_f * V_f + u_m * V_m

    G_m = 1
    G_f = 1
    G_xy = (G_f * G_m) / (V_f * G_m + V_m * G_f)
    
    return {"E_x" : E_x, "E_y" : E_y, "u_xy" : u_xy, "G_xy" : u_xy}