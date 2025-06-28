def calcul_puck_uni(E_f, E_m, V_f, V_m, u_m, u_f):
    """
    Calcul E_x et E_y à partir des formules de PUCK
    _ E_f : module d'Young des fibres
    _ V_f : fraction volumique des fibres
    _ E_m : module d'Young de la matrice
    _ V_m : fraction volumique de la matrice
    _ u_m : coefficient de poisson de la matrice
    """
    E_x = E_f * V_f + E_m * V_m

    E_o = E_m / (1 - (u_m ** 2))
    E_y = (E_o * (1 + 0.85 * V_f)**2) / ((1 - V_f)**(1.25) + (V_f * E_o / E_f))

    G_m = (0.5 * E_m)/(1 + u_m)
    G_f = (0.5 * E_f)/(1 + u_f)
    G_xy = (G_m * (1 + 0.6 * (V_f ** 0.5))) / (((1 - V_f) ** (1.25)) + (V_f * G_m / G_f))

    u_xy = u_f * V_f + u_m * V_m
    u_yx = u_xy * E_y / E_x

    return {"E_x" : round(E_x, 2), "E_y" : round(E_y, 2), "G_xy" : round(G_xy, 2), "u_xy" : round(u_xy, 2), "u_yx" : round(u_yx, 2)}