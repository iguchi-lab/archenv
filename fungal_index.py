imoport numpy as np

############################################################################################################################
#Fungal Index
############################################################################################################################

def calc_fungal_index(h, t):
    a  = - 0.3
    b  = 0.685
    c1 = 0.95
    c2 = 0.07
    c3 = 25
    c4 = 7.2 
    
    x = (h - c1) / c2
    y = (t - c3) / c4

    FI = 187.25 * np.exp((((x ** 2) - 2 * a * x * y + (y ** 2)) ** b) /(2 * (a ** 2) - 2)) - 8.25

    return FI
