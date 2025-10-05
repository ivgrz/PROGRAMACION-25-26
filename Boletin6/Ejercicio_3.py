"""
Escribir un programa que almacene nunha lista os
números do 1 o 10 e os mostre por pantalla en orden
inverso separados por comas.
"""
def numsep():
    # Creamos la lista con los números del 1 al 10 usando range
    # range(1, 11) genera del 1 al 10 (el 11 no se incluye)
    nums = list(range(1,11))
    # Invertimos la lista con reverse()
    nums.reverse()

    # - map(str, nums) convierte cada número a string
    # - ", ".join(...) une esos strings en una sola cadena separada por comas
    print(" , ".join(map(str,nums)))
numsep()