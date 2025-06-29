def calcul_puck_bi(E_f, E_m, V_f, V_m, u_f, u_m, A_1, A_2):
    """
    _ E_f : module d'Young des fibres
    _ V_f : fraction volumique des fibres
    _ E_m : module d'Young de la matrice
    _ V_m : fraction volumique de la matrice
    _ u_f : coefficient de poisson des fibres
    _ u_m : coefficient de poisson de la matrice
    _ A_1 : proportion des fibres suivant (0X)
    _ A_2 : proportion des fibres suivant (0Y)
    """
    E_x = E_f * V_f + E_m * V_m
    E_o = E_m / (1 - (u_m ** 2))
    E_y = (E_o * (1 + 0.85)**2) / ((1 - V_f)**(1.25) + (V_f * E_o / E_f))

    u_xy = u_f * V_f + u_m * V_m
    u_yx = u_xy * E_y / E_x

    G_m = (0.5 * E_m)/(1 + u_m)
    G_f = (0.5 * E_f)/(1 + u_f)
    G_xy = (G_m * (1 + 0.6 * (V_f ** 0.5))) / (((1 - V_f) ** (1.25)) + (V_f * G_m / G_f))

    A_3 = (E_y * (u_xy ** 2) / E_x)
    P = (A_1 * E_x + A_2 * E_y) / (1 - A_3)
    Q = (A_2 * E_x + A_1 * E_y) / (1 - A_3)
    R = (u_xy * E_y) / (1 - A_3)
    
    E_x0 = P - R/Q
    E_y0 = Q - R/P

    u_xy_0 = R/Q

    return {"E_x" : E_x0, "E_y" : E_y0, "G_xy" : G_xy, "u_xy" : u_xy_0}