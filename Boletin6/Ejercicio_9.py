"""
Escribir un programa que almacene os vectores (1,2,3) e
(-1,0,2) en duas listas e mostre por pantalla o seu
producto escalar.
"""

def prod_esc():

    vector1 = [1,2,3]

    vector2 = [-1,0,2]

    parte1 = vector1[0] * vector2[0]
    parte2 = vector1[1] * vector2[1]
    parte3 = vector1[2] * vector2[2]

    productoe = parte1 + parte2 + parte3

    print(f"El producto escalar es {productoe}")





prod_esc()